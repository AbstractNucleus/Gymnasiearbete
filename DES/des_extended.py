from tables import *

def permutate(string, table, output = ""):
    for i in range(len(table)):
        output += str(string[table[i]-1])
    return output

def translate(string, table, output = ""):
    for i in string:
        output += str(table[i])
    return output


M = list(str(1030114186110932))



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
L, R = [M_IP[:32]], [M_IP[32:]]


# Next in the f calculation, we XOR the output E(Rn-1) with the key Kn
# Let + denote XOR addition, (bit-by-bit addition modulo 2). Then for n going from 1 to 16 we calculate

#Ln = Rn-1
#Rn = Ln-1 + f(Rn-1,Kn)

# 1. Permutera Rn-1 med E




E_0_K_1 = ""
for i in range(48):
    if int(E[0][i]) == 1:
        if int(pc_table[1][i]) == 0:
            E_0_K_1 += "1"
        elif int(pc_table[1][i]) == 1:
            E_0_K_1 += "0"
    if int(E[0][i]) == 0:
        if int(pc_table[1][i]) == 0:
            E_0_K_1 += "0"
        elif int(pc_table[1][i]) == 1:
            E_0_K_1 += "1"

E_0_list = []
for i in range(0, 48, 6):
    E_0_list.append(E_0_K_1[i:i+6])


# Nästa steg är att göra E_0
gg = {
    "00": "0",
    "01": "1",
    "10": "2",
    "11": "3",
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "10",
    "1011": "11",
    "1100": "12",
    "1101": "13",
    "1110": "14",
    "1111": "15"
}
r = []
for i in E_0_list:
    r.append(gg[i[0]+i[5]])
    r.append(gg[i[1]+i[2]+i[3]+i[4]])
print(r)

