#!/bin/python

import json
import requests
import time
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
________       _____            _________
___  __ \_________(_)__   ____________  /
__  / / /_  ___/_  /__ | / /  _ \  __  / 
_  /_/ /_  /   _  / __ |/ //  __/ /_/ /  
/_____/ /_/    /_/  _____/ \___/\__,_/   

by: _g0nx4
""")
print(logo)
placa=input("Matricula: ")
if len(placa)<6 or len(placa)>6:
	print("placa no valida")
	exit()
else:
	pass
url = (f"https://api.boostr.cl/vehicle/{placa}.json")
config = {"accept": "application/json"}

response = requests.get(url,headers=config)

multas_url=(f"https://api.boostr.cl/vehicle/traffic_tickets/{placa}.json")
mu_res=requests.get(multas_url,headers=config)
mul=json.loads(mu_res.text)
r=json.loads(response.text)
#print(response_json)
time.sleep(0.3)
print(f"Dueño: {r['data']['owner']['fullname']}")
time.sleep(0.3)
print(f"Rut: {r['data']['owner']['documentNumber']}")
time.sleep(0.3)
print(f"Matricula: {r['data']['plate']}")
time.sleep(0.3)
print(f"Multas: {mul['data']['tickets']}")
print(f"Matricula Full: {r['data']['plate']}-{r['data']['dv']}") 
time.sleep(0.3)
print(f"Marca: {r['data']['make']}")
time.sleep(0.3)
print(f"Modelo: {r['data']['model']}")
time.sleep(0.3)
print(f"Año: {r['data']['year']}")
time.sleep(0.3)
print(f"Tipo de Auto: {r['data']['type']}")
time.sleep(0.3)
print(f"Motor: {r['data']['engine']}")


