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