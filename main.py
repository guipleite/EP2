import random
import json
	
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

while True:
	op = str(input("Deseja Passear ou Dormir? \n"))
		
	if op.lower() == "passear" :
		inte = random.randrange(len(inspermons))
		ini = inspermons[inte]
		print("Seu inimigo é: {0}".format(ini["nome"]))
			
		
	if op.lower() == "dormir" :
		break
		
	if op.lower()!="dormir" or op.lower() != "passear":
		print("Comando errado")


			

			
			