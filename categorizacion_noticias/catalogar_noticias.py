import numpy as np
import tensorflow as tf
import json
import os

# carga lso datos en una lista
def cargaDatos(archivo):
    with open(archivo, "r", encoding="utf-8") as doc:
                return [json.loads(linea) for linea in doc]

data = cargaDatos("./data/data.json")

# limpia los valores repetidos en el archivo y crea un archivo nuevo solo conlos valores unicos
def limpiarDuplicados(archivo):
    dataLimpia = []
    repetidos = set()

    with open(archivo, "r", encoding="utf-8") as doc:
        for line in doc:
            linea = json.loads(line)
            lineaTupla = tuple(linea.items())
            if lineaTupla not in repetidos:
                repetidos.add(lineaTupla)
                dataLimpia.append(linea)

    directorio, _ = os.path.split(archivo)
    archivoNuevo = os.path.join(directorio, "dataLimpia.json")

    with open(archivoNuevo, "w", encoding="utf-8") as doc:
        for linea in dataLimpia:
            doc.write(json.dumps(linea) + "\n")

    print(f"Duplicados eliminados y guardados en {archivoNuevo}")

limpiarDuplicados("./data/data.json")

# imprime las categorias que se ecuentatran en el archivo
categorias = list(set(linea["category"] for linea in data))
print("Categorías:", categorias)

# extrae las categorias y los titulos de las noticias
textos = [linea["headline"] + " " + linea["short_description"] for linea in data]
categoriaSalida = [linea["category"] for linea in data]

# se le da valoreas al texto dentro del rango establecido
tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=50000, oov_token="<OOV>")
tokenizer.fit_on_texts(textos)
secuencias = tokenizer.texts_to_sequences(textos)
padded = tf.keras.preprocessing.sequence.pad_sequences(secuencias, maxlen=100, padding='post', truncating='post')

# convierte el formato
categoria_indices = {cat: i for i, cat in enumerate(categorias)}
etiquetas_numericas = [categoria_indices[cat] for cat in categoriaSalida]
etiquetas_onehot = tf.keras.utils.to_categorical(etiquetas_numericas, num_classes=len(categorias))

# divide los datos en muestra y prueba
num_train = int(len(padded) * 0.8)
X_train, X_test = padded[:num_train], padded[num_train:]
y_train, y_test = etiquetas_onehot[:num_train], etiquetas_onehot[num_train:]

# creacion del modelo
modelo = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=50000, output_dim=32, input_length=50),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(len(categorias), activation='softmax')
])

# optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)
# modelo.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

modelo.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

modelo.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test), verbose=2)

loss, accuracy = modelo.evaluate(X_test, y_test)
print(f"Precisión del modelo: {accuracy:.4%}")

predicciones = modelo.predict(X_test)
predicciones_categorias = np.argmax(predicciones, axis=1)
categorias_reales = np.argmax(y_test, axis=1)
coincidencias = np.sum(predicciones_categorias == categorias_reales)
print(f"Noticias clasificadas correctamente: {coincidencias} de {len(y_test)}")