import random
import json
	
def mostra_ipmon(ipmon):
	print("Inspermon : {0}".format(ipmon["nome"]))
	print("poder = {0}".format(ipmon["poder"]))
	print("vida = {0}".format(ipmon["vida"]))
	print("defesa = {0}\n".format(ipmon["defesa"]))		
	
def Combat (vF,vI,pF,pI,dF,dI):
	while vF > 0 or vI > 0 :
		
		sorte = random.randint(0,100)    # SISTEMA DE SORTE F
		if sorte <= 100 :
			mod = 1.7
		#	print("É Super efetivo!")
		if sorte < 70 :
			mod = 1
		if sorte < 10 :
			mod = 0.3
			#print('Ataque pouco efetivo')
		
		vI = vI - dI - (pF*mod)
		if vI <= 0 :
			print("YOU WIN \n")
			break
		vF = vF - dF - (pI*mod)
		if vF <= 0:
			print('NO CEU TEM PAO?')
			#return gameLoop == False
			#break
			return 1
			
def CombatF (vF,vI,pF,pI,dF,dI):  #COMBATE SE A FUGA DER RUIM
	while vF > 0 or vI >0 :
		
		sorte = random.randint(0,100)    # SISTEMA DE SORTE F
		if sorte <= 100 :
			mod = 1.7
		#	print("É Super efetivo!")
		if sorte < 70 :
			mod = 1
		if sorte < 10 :
			mod = 0.3
			#print('Ataque pouco efetivo')
		
		vF = vF - dF - (pI*mod)
		if vF <= 0:
			print('NO CEU TEM PAO?')
			return gameLoop == False
		vI = vI - dI - (pF*mod)
		if vI <= 0 :
			print("YOU WIN \n")
			#break
			return 1
dex = []
idex = []
def insperdex (dex,ini):						#INSPERDEX NF

	if ini["nome"] not in dex :
		dex.append(ini["nome"])
	# for z in dex :
		# if dex.count(z) > 1 and z not in idex :
			# dex.append(z)
	
	dex.append(ini["nome"])		
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
combatLoop = True
choiceLoop = True

while gameLoop == True:

	op = str(input("Deseja PASSEAR ou DORMIR? \n"))
			
	if op.lower() == "passear" :
		inte = random.randrange(len(inspermons))
		ini = inspermons[inte]
		print("Um {0} selvagem apareceu! \n".format((ini["nome"]).upper()))
		for x in inspermons:
			if x ["nome"] == ini["nome"] :
				inistat=[x["poder"],x["vida"],x["defesa"]]	
		
		insperdex(dex,ini)
		
		af = str(input("\n Deseja FUGIR ou ATACAR? \n"))
		
		if af.lower() == "fugir":
			f = random.randint(0,10)
			if f < 7 :
				print("Você fugiu")
				#break #(?)
				
			else :
				print("Deu ruim")
				
				pF = fstat [0]
				pI = inistat [0]
				vF = fstat [1]
				vI = inistat [1]
				dF = fstat [2]
				dI = inistat [2]
			
				c = CombatF(vF,vI,pF,pI,dF,dI)
				if c == 1:
					break
				
		if af.lower() == "atacar" :
			
			pF = fstat [0]
			pI = inistat [0]
			vF = fstat [1]
			vI = inistat [1]
			dF = fstat [2]
			dI = inistat [2]
				
			c = Combat(vF,vI,pF,pI,dF,dI)
			if c == 1:
				break
							
				
	if op.lower() == "dormir" :
			gameLoop = False
			
	else :
		#print("\n Comando errado")
		continue	
		
print(' \n OBRIGADO POR JOGAR INSPERMON! \n')
print(dex)



#FOI MAL N DEU PRA ACABAR