import json
from collections import Counter
import matplotlib.pyplot as plt

# cuenta cuantas noticias hay por categoria y por fecha y muestra las tendencias y genera un grafico
def cargaDatos(archivo):
    datos = []
    with open(archivo, "r", encoding="utf-8") as doc:
        for linea in doc:
            try:
                datos.append(json.loads(linea))
            except json.JSONDecodeError as e:
                print(f"no se puede convertir el json: {e}")
    return datos

data = cargaDatos("./data/dataLimpia.json")
print(f"Se cargaron {len(data)} registros correctamente.")

categorias = [item["category"] for item in data]
contadorCategorias = Counter(categorias)
print("Tendencia por categoría:")
for categoria, cantidad in contadorCategorias.most_common():
    print(f"{categoria}: {cantidad} noticias")

fechas = [item["date"] for item in data]
contadorFechas = Counter(fechas)
print("Tendencia por fecha:")
for fecha, cantidad in contadorFechas.most_common(10):
    print(f"{fecha}: {cantidad} noticias")

plt.figure(figsize=(10, 5))
plt.bar(contadorCategorias.keys(), contadorCategorias.values(), color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel("Categoría")
plt.ylabel("Cantidad de Noticias")
plt.title("Tendencia de Noticias por Categoría")
plt.show()

print("Las tres categorías con más noticias son:")
for categoria, cantidad in contadorCategorias.most_common(3):
    print(f"{categoria}: {cantidad} noticias")