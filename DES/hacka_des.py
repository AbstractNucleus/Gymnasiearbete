M="1000000000000001"
SVAR = "0"
import time
start_time = time.time()
while SVAR  != "274880911a4f540a1e7c153f1ff349b2daf3353162ef373e786cf":

    from tables import *


    # En funnktion för att permutera en string med ett table
    def permutate(string, table):
        output = ""
        for i in range(len(table)):
            output += str(string[table[i]-1])
        return output


    # En funktion för att översätta med ett table som är en dictionary
    def translate(string, table):
        output = ""
        for i in string:
            output += str(table[i])
        return output


    # Används för att generera L och R
    def f(r, k):
        r = permutate(r, E_BIT)
        x = xor(r, k, len(r))
        y = []
        for i in range(0,48,6):
            y.append(x[i]+x[i+5])
        c = 0
        for i in range(0, len(x), 6):
            y[c] += x[i+1]+x[i+2]+x[i+3]+x[i+4]
            c += 1
        return permutate(S_1[y[0]]+S_2[y[1]]+S_3[y[2]]+S_4[y[3]]+S_5[y[4]]+S_6[y[5]]+S_7[y[6]]+S_8[y[7]], P)


    # XOR funktion som går att använda med strings
    def xor(a, b, n):
        ans = ""
        for i in range(n):
            if (a[i] == b[i]):
                ans += "0"
            else:
                ans += "1"
        return ans

    M = str(M)



    ip, x = "", ""
    pc_table = ["","","","","","","","","","","","","","","","",""]


    # Konverterar meddelandet till en binär string
    M_BIN = translate(M, DEC_TO_BIN_0_9)


    # Permuterar den binära delen med PC_1 och delar in den i C och D. Sen skapas en lista med C, en med D och en med C + D.
    C, D = permutate(M_BIN, PC_1)[28:], permutate(M_BIN, PC_1)[:28]
    C_LIST, D_LIST, CD_LIST = [C], [D], [C[0] + D[0]]


    # Left-shiftar C och D enligt tabellen och sammanfogar C_n och D_n till 56-bit strings
    n = 0
    for i in LEFT_SHIFTS:
        C_LIST.append(C_LIST[n][i % len(C) : ] + C_LIST[n][ : i % len(C)])
        D_LIST.append(D_LIST[n][i % len(D) : ] + D_LIST[n][ : i % len(D)])
        CD_LIST.append(C_LIST[n]+ D_LIST[n])
        n += 1


    # Ger en lista med K genom att permutera CD_n med PC_2
    K_LIST = []
    for i in range(1, 17):
        K_LIST.append(permutate(CD_LIST[i], PC_2))


    # Permuterar binära M med IP och skapar L_0 och R_0
    M_IP = permutate(M_BIN, IP)
    L, R = M_IP[:32], M_IP[32:]
    L_LIST, R_LIST = [L], [R]


    # Next in the f calculation, we XOR the output E(Rn-1) with the key Kn
    # Ln = Rn-1
    # Rn = Ln-1 + f(Rn-1,Kn)

    for i in range(1, 17):
        L_LIST.append(R_LIST[i-1])
        R_LIST.append(xor(L_LIST[i-1], f(R_LIST[i-1], K_LIST[i-1]), len(L_LIST[i-1])))
    RL = R_LIST[16]+L_LIST[16]
    SVAR = hex(int((permutate(RL, IP_1))))[2:]
    M=int(M)
    M=M+1
    M=str(M)
    print(M)

    if SVAR == "274880911a4f540a1e7c153f1ff349b2daf3353162ef373e786cf":
        print (M)
        print("--- %s seconds ---" % (time.time() - start_time))
    #1030114186110932`