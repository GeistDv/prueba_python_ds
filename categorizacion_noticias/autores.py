import json
from collections import Counter, defaultdict

# lee un archivo json y cuenta cuantas noticias escribe un autor por categoria
def conteoAutores(archivo):
    contadorAutores = Counter()
    categoriaPorAutor = defaultdict(Counter)
    
    with open(archivo, 'r', encoding='utf-8') as doc:
        for linea in doc:
            try:
                data = json.loads(linea)
                autores = data.get("authors", "").strip()
                categorias = data.get("category", "desconocida").strip()
                
                if autores:
                    contadorAutores[autores] += 1
                    categoriaPorAutor[categorias][autores] += 1
            except json.JSONDecodeError:
                print("no se puede convertir en json:", linea)
    
    print("Autores que mas escriben:")
    for author, count in contadorAutores.most_common(10):
        print(f"{author}: {count} noticias")
    
    print("Autores que mas escriben por categoría:")
    for category, authors in categoriaPorAutor.items():
        autoresTop, topContador = authors.most_common(1)[0]
        print(f"{category}: {autoresTop} ({topContador} noticias)")

conteoAutores("./data/dataLimpia.json")
