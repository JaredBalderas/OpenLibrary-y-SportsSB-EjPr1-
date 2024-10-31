import requests

def linea(simbolo='*', longitud=50):
    print(simbolo * longitud)

def buscar_libro(titulo):
    url = f"https://openlibrary.org/search.json?title={titulo}"
    respuesta = requests.get(url)
    
    if respuesta.status_code != 200:
        print("Error en la solicitud")
        return None
    
    return respuesta.json()

linea()

titulo_libro = ""
while not titulo_libro:
    titulo_libro = input("Ingrese el título del libro: ")

resultado = buscar_libro(titulo_libro)

if resultado and 'docs' in resultado:
    docs = resultado['docs']
    print(f"Se encontraron {len(docs)} documentos para el título '{titulo_libro}':")
    
    for i, doc in enumerate(docs):
        print(f"{i + 1}: {doc.get('title', 'Título no disponible')}")

    seleccion = int(input("Seleccione el número del documento que le interesa: ")) - 1
    
    if 0 <= seleccion < len(docs):
        libro_seleccionado = docs[seleccion]
        print("Información del libro seleccionado:")
        print(f"Título: {libro_seleccionado.get('title', 'Título no disponible')}")
        print(f"Autor(es): {', '.join(libro_seleccionado.get('author_name', ['Autor no disponible']))}")
        print(f"Año de publicación: {libro_seleccionado.get('first_publish_year', 'Año no disponible')}")
    else:
        print("Selección no válida.")
else:
    print("No se encontraron documentos.")