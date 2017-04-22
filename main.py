import random
import json

from guidi import Combat

def mostra_ipmon(ipmon):
	print("Inspermon : {0}".format(ipmon["nome"]))
	print("poder = {0}".format(ipmon["poder"]))
	print("vida = {0}".format(ipmon["vida"]))
	print("defesa = {0}\n".format(ipmon["defesa"]))	
print("Você pode encontrar esses inspermons por aí: \n")	
with open('inspermons.json') as arquivo:
		inspermons = json.load(arquivo)
for ipmon in inspermons:
		mostra_ipmon(ipmon)
fstat = []
		
pokem = str(input("Escolha um inspermon \n"))
poke = pokem.lower()
for i in inspermons:
	if i ["nome"] == poke :
		fstat=[i["poder"],i["vida"],i["defesa"]]
# print (fstat)
gameLoop = True

while gameLoop:
	op = str(input("Deseja Passear ou Dormir? \n"))
		
	if op.lower() == "passear" :
		inte = random.randrange(len(inspermons))
		ini = inspermons[inte]
		print("Um {0} selvagem apareceu! \n".format((ini["nome"]).upper()))
		for x in inspermons:
			if x ["nome"] == ini["nome"] :
				inistat=[x["poder"],x["vida"],x["defesa"]]
		
		while True:
			if combate(inistat, fstat) == -1 :
				break
			
			else:
				gameLoop = False
				
			
	if op.lower() == "dormir" :
		gameLoop = False
		
	else :
		print("Comando errado")
		
if not gameLoop:
	print("No céu tem pão")