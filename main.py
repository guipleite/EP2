arquivo = open("inspermons.json" , "r")
import random

def main(arquivo,random):
	while True:
		op = str(input("Deseja Passear ou Dormir? "))
		opl = op.lower()
		if opl == "passear" :
			ini = arquivo[random.int]
		
		if opl == "dormir" :
			break
		
		
		else:
			print("Comando errado")