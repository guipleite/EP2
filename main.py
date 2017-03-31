import random
import json

def mostra_ini(ipmon):
	print("Inspermon : {0}".format(ipmon["nome"]))
	
def mostra_ipmon(ipmon):
	print("Inspermon : {0}".format(ipmon["nome"]))
	print("poder = {0}".format(ipmon["poder"]))
	print("vida = {0}".format(ipmon["vida"]))
	print("defesa = {0}\n".format(ipmon["defesa"]))
	
with open('inspermons.json') as arquivo:
		inspermons = json.load(arquivo)
for ipmon in inspermons:
		mostra_ipmon(ipmon)

def main(arquivo,random):
	while True:
		op = str(input("Deseja Passear ou Dormir? "))
		opl = op.lower()
		if opl == "passear" :
			inte = random.randrange(len(d))
			ini = arquivo[inte]
			with open('inspermons.json') as arquivo:
				inspermons = json.load(arquivo)
			for ipmon in inspermons:
				mostra_ini(ipmon)
		
		if opl == "dormir" :
			break
		
		
		else:
			print("Comando errado")

			