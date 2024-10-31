import requests

def menu():
    print("Selecciona una opción:")
    print("1. Consulta por equipo")
    print("2. Consulta por nombre de jugador")
    print("3. Listado de ligas")
    print("4. Consulta de una liga específica")
    
    opcion = input("Ingresa el número de la opción: ")
    
    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            consulta_equipo()
        elif opcion == 2:
            consulta_jugador()
        elif opcion == 3:
            listado_ligas()
        elif opcion == 4:
            consulta_liga_especifica()
        else:
            print("Opción no válida.")
    else:
        print("Por favor, ingresa un número válido.")

def consulta_equipo():
    response = requests.get("https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=Barcelona")
    data = response.json()
    print("Nombre del equipo:", data['teams'][0]['strTeam'])
    print("Liga:", data['teams'][0]['strLeague'])
    print("Descripción en español:", data['teams'][0]['strDescriptionES'])
    print("Página oficial:", data['teams'][0]['strWebsite'])
    print("Nombre del estadio:", data['teams'][0]['strStadium'])

def consulta_jugador():
    response = requests.get("https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p=Messi")
    data = response.json()
    print("Nombre completo del jugador:", data['players'][0]['strPlayer'])
    print("Nacionalidad:", data['players'][0]['strNationality'])
    print("Equipo en el que juega:", data['players'][0]['strTeam'])
    print("Lugar de nacimiento:", data['players'][0]['strBirthLocation'])
    print("Cuenta de Facebook:", data['players'][0]['strFacebook'])
    print("Altura:", data['players'][0]['strHeight'])
    print("Peso:", data['players'][0]['strWeight'])

def listado_ligas():
    response = requests.get("https://www.thesportsdb.com/api/v1/json/3/all_leagues.php")
    data = response.json()
    for league in data['leagues']:
        print("ID de la liga:", league['idLeague'], "Nombre de la liga:", league['strLeague'])

def consulta_liga_especifica():
    league_id = input("Ingresa el ID de la liga que deseas consultar: ")
    response = requests.get(f"https://www.thesportsdb.com/api/v1/json/3/lookupleague.php?id={league_id}")
    data = response.json()
    if 'leagues' in data and len(data['leagues']) > 0:
        league = data['leagues'][0]
        print("Nombre de la liga:", league['strLeague'])
        print("Descripción:", league['strDescription'])
        print("Página oficial:", league['strWebsite'])
    else:
        print("No se encontró la liga con ese ID.")

if __name__ == "__main__":
    menu()