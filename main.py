import json
import requests
from bs4 import BeautifulSoup
#========================
# If you can read this, long live open source
#========================

'''
           ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                     
         /@@@                                   @@@                                   
        #@@                                      @@@ 
        @@@           ___             _  _        @@@
        @@@     __ _ / _ \ _ __ __  _| || |       @@&
        @@@    / _` | | | | '_ \\ \/ / || |_      @@&
        @@@   | (_| | |_| | | | |>  <|__   _|     @@&
        @@@    \__, |\___/|_| |_/_/\_\  |_|       @@&
        @@@    |___/                             @@&
        %@@                                     &@@
         (@@@                                  @@@
           /@@@@@@@@@@@@@@@@@@@@@@@        @@@@@@   
                                  @@@@     @@    
                                     @@@@  @@
                                        @@@@@ 
                                           @@
                                    /^\/^\
                                  _|__|  O|
                        \/     /~     \_/ \
                          \____|__________/  \
                                \_______      \
                                        `\     \                 \
                                          |     |                  \
                                         /      /                    \
                                        /     /                       \\
                                      /      /                         \ \
                                     /     /                            \  \
                                   /     /             _----_            \   \
                                  /     /           _-~      ~-_         |   |
                                 (      (        _-~    _--_    ~-_     _/   |
                                  \      ~-____-~    _-~    ~-_    ~-_-~    /
                                    ~-_           _-~          ~-_       _-~
                                       ~--______-~                ~-___-~
'''
logo=("""

     ___________       _____            _________
      _____  __ \_________(_)__   ____________  /
        __  / / /_  ___/_  /__ | / /  _ \  __  /
        _  /_/ /_  /   _  / __ |/ //  __/ /_/ /
        /_____/ /_/    /_/  _____/ \___/\__,_/

                        ________
                     ______/  |_\_
                 ______|  _     _``-.
                     __'-(_)---(_)--'  
""")
print(logo)
placa=input("[+] Patente: ")
if len(placa)<6 or len(placa)>6:
	print("placa no valida")
	exit()
else:
	pass
url = (f"https://api.boostr.cl/vehicle/{placa}.json")
config = {"accept": "application/json"}
response = requests.get(url,headers=config)
r=json.loads(response.text)
print("")
if r['status']=="success":
        rut=r['data']['owner']['documentNumber']
        conversion_patas=(rut[0]+rut[1]+"."+rut[2:5]+"."+rut[5:])
        rut_url=f"https://www.nombrerutyfirma.com/rut?term={conversion_patas}"
        usr={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0'}
        page=requests.get(url=rut_url,headers=usr)
        soup = BeautifulSoup(page.content, 'html.parser')
        nombre=r['data']['owner']['fullname']
        run=r['data']['owner']['documentNumber']
        patente=r['data']['plate']
        patente_full=r['data']['plate']+"-"+r['data']['dv']
        marca=r['data']['make']
        modelo=r['data']['model']
        año=r['data']['year']
        tipo=r['data']['type']
        motor=r['data']['engine']
        tabla = soup.find('tr', tabindex='1')
        if tabla:
                datosTD = tabla.find_all('td')
                name=datosTD[0].get_text()
                gender=datosTD[2].get_text()
                if gender=="VAR":
                        gender="Hombre"
                else:
                        gender="Mujer"                
                addr=datosTD[3].get_text()
                city=datosTD[4].get_text()
                print("[!] Informacion encontrada")
                print(f"""
[*] Nombre: {name}
[*] Rut: {conversion_patas}
[*] Sexo: {gender}
[*] Direccion: {addr}
[*] Ciudad: {city}

[*] Patente: {patente}
[*] Patente Completa : {patente_full}
[*] Marca: {marca}
[*] Modelo: {modelo}
[*] Tipo: {tipo}
[*] Año: {año}
[*] Motor: {motor}
                """)
        else:
                print("[!] el rut asociado no existe! ")
                print(f"""
[*] Dueño: {nombre}
[*] Rut: {run}
[*] Patente: {patente}
[*] Marca: {marca}
[*] Modelo: {modelo}
[*] Tipo: {tipo}
[*] Año: {año}
[*] Motor: {motor}
                """)
else:
        print("[!] Error: patente invalida o no se encuentra en el sistema")
        quit()
