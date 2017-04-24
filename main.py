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
			print('E MORREU ...')
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
			#print('Não foi muito efetivo')
		
		vF = vF - dF - (pI*mod)
		if vF <= 0:
			print('E MORREU ...')
			return 1
			break
		vI = vI - dI - (pF*mod)
		if vI <= 0 :
			print("YOU WIN \n")
			break
			
dex = []
idex = []
def insperdex (dex):						#INSPERDEX NF
	# for i in dex:
		# if i not in idex:
			# idex.append(i)	
	# print(idex)
	id = list(set(dex))
	return id
	
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
		fstat=[i["poder"],i["vida"],i["defesa"]]  #PASSA OS STATS DO INSPERMON PARA UMA LISTA
# print (fstat)

gameLoop = True
#combatLoop = True
#choiceLoop = True

while gameLoop == True:

	op = str(input("\n Deseja PASSEAR , DORMIR ou ver o INSPERDEX ? \n"))
			
	if op.lower() == "passear" :
		inte = random.randrange(len(inspermons))
		ini = inspermons[inte]
		print("Um {0} selvagem apareceu! \n".format((ini["nome"]).upper()))
		for x in inspermons:
			if x ["nome"] == ini["nome"] :
				inistat=[x["poder"],x["vida"],x["defesa"]]	
		
		dex.append(ini["nome"])
		
		af = str(input("\n Deseja FUGIR ou ATACAR? \n"))
		
		if af.lower() == "fugir":
			f = random.randint(0,10)
			if f < 7 :
				print("Você fugiu \n")
				#break #(?)
				
			else :
				print("Deu ruim")
				
				pF = fstat [0]
				pI = inistat [0]
				vF = fstat [1]
				vI = inistat [1]
				dF = fstat [2]
				dI = inistat [2]
			
				cf = CombatF(vF,vI,pF,pI,dF,dI)
				if cf == 1:
					gameLoop = False
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
						
		else :
			continue
			
	if op.lower() == "insperdex":
		print("Você tem esses INSPERMONS no seu INSPERDEX : \n")
		print(insperdex(dex))
		continue	
		
	if op.lower() == "dormir" :
		gameLoop = False
			
	
	
	else :
		#print("\n Comando errado")
		continue	
		
print (' \n	OBRIGADO POR JOGAR INSPERMON! \n Você encontrou esses INSPERMONS na sua jornada:')
print (insperdex(dex))

