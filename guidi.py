def combate(ini,ipmon):
    va = ipmon[1]	
    vi = ini [1]
    while True:
        va = va + ipmon[2] - ini[0]
        vi = vi + ini[2] - ipmon[0]
        if vi <= 0:
            print ("YOU WIN")
            return -1
        if va <= 0:  
            print("No ceu tem pão?")
            break
			
			
def calculavidapok1(ataquepok2, defesapok1):
	delta1 = defesapok1-ataquepok2
	return delta1

def calculavidapok2(ataquepok1, defesapok2):
	delta2 = defesapok2-ataquepok1
	return delta2


# a= allpoke[10]["vida"]
# b= allpoke[11]["vida"]
# c= allpoke[10]["poder"]
# d= allpoke[11]["poder"]
# e= allpoke[10]["defesa"]
# f= allpoke[11]["defesa"]
# while a or b <1:
	# a = a - calculavidapok1(d,e)
	# b = b - calculavidapok2(c,f)
	# if a>1:
		# print("a is the winner")
		# break
	# elif b>1:
		# print("b is the winner")
		# break