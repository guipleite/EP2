import random
import json

#from guidi import Combat

# def vidaF(pI, dF):
	# danoF = dF-pI
	# return danoF
# def vidaIni(pF, dI):
	# danoIni = dI-pF
	# return danoIni
	
def mostra_ipmon(ipmon):
	print("Inspermon : {0}".format(ipmon["nome"]))
	print("poder = {0}".format(ipmon["poder"]))
	print("vida = {0}".format(ipmon["vida"]))
	print("defesa = {0}\n".format(ipmon["defesa"]))		
	
def Combat (vF,vI,pF,pI,dF,dI):
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
		
		vI = vI - dI - (pF*mod)
		if vI <= 0 :
			print("YOU WIN \n")
			break
		vF = vF - dF - (pI*mod)
		if vF <= 0:
			print('NO CEU TEM PAO?')
			return gameLoop == False
			#break
			
def CombatF (vF,vI,pF,pI,dF,dI):
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
			break
dex = []
def insperdex (dex):						#INSPERDEX NF
	ld = len(dex)
	for i in range(ld):
		if ini["nome"] in dex:
			continue
		else :
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

	op = str(input("Deseja Passear ou Dormir? \n"))
			
	if op.lower() == "passear" :
		inte = random.randrange(len(inspermons))
		ini = inspermons[inte]
		print("Um {0} selvagem apareceu! \n".format((ini["nome"]).upper()))
		for x in inspermons:
			if x ["nome"] == ini["nome"] :
				inistat=[x["poder"],x["vida"],x["defesa"]]	
		
		af = str(input("\n Deseja FUGIR ou ATACAR? \n"))
		
		if af.lower() == "fugir":
			f = random.randint(0,10)
			if f < 7 :
				gameLoop = False #(?)
			else :
			
				insperdex(dex)
			
				vF = fstat [1]
				vI = inistat [1]
				pF = fstat [0]
				pI = inistat [0]
				dF = fstat [2]
				dI = inistat [2]
			
				CombatF(vF,vI,pF,pI,dF,dI)
				
		if af.lower() == "atacar" :
			
			insperdex(dex)
			
			vF = fstat [1]
			vI = inistat [1]
			pF = fstat [0]
			pI = inistat [0]
			dF = fstat [2]
			dI = inistat [2]
				
			Combat(vF,vI,pF,pI,dF,dI)
						
				
	if op.lower() == "dormir" :
			gameLoop = False
			
	else :
		#print("\n Comando errado")
		continue	
print(' \n OBRIGADO POR JOGAR INSPERMON! \n')
print(dex)