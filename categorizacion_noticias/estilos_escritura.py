import json

# cataloga las noticias en diferentes estilos y cuenta cuantas noticias hay or estilo
def categoriasArticulos(archivo):

# este json lo cree para facilitar el catalogar las noticias en un estilo de escritura
    categorias = {
        "informativo": ["POLITICS", "WORLD NEWS", "SCIENCE", "TECH", "BUSINESS", "EDUCATION"],
        "humorista": ["COMEDY", "WEIRD NEWS"],
        "satirico": ["MEDIA", "WEIRD NEWS"],
        "serio": ["CRIME", "RELIGION", "MONEY"],
        "diplomatico": ["WOMEN", "LATINO VOICES", "BLACK VOICES"],
        "critico": ["IMPACT", "ENVIRONMENT"],
        "investigativo": ["WORLDPOST", "ARTS & CULTURE"],
        "denuncia": ["DIVORCE", "PARENTS", "HEALTHY LIVING"]
    }
    
    articulos = []
    with open(archivo, 'r', encoding='utf-8') as doc:
        for linea in doc:
            articulos.append(json.loads(linea))
    
    contadorEstilo = {llave: 0 for llave in categorias.keys()}
    
    for articulo in articulos:
        for categoria, keywords in categorias.items():
            if articulo["category"] in keywords:
                articulo["style"] = categoria
                contadorEstilo[categoria] += 1
    
    print("Se categorizaron las noticias:")
    
    for estilo, count in contadorEstilo.items():
        print(f"El estilo {estilo} tiene {count} noticias")

categoriasArticulos("./data/dataLimpia.json")
