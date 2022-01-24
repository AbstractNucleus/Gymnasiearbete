from tables import *
from collections import deque

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

M = str(int("0x2b2c15c87c47349ebb0a954ab07a00b8f0638fb167cb7c06d9f80", base=16))
M = str(int(M, base=2))


ip, x = "", ""
pc_table = ["","","","","","","","","","","","","","","","",""]


# Konverterar meddelandet till en binär string
M_BIN = translate(M, DEC_TO_BIN_0_9)


# Permuterar den binära delen med PC_1 och delar in den i C och D
'''CD_PRE = permutate(M_BIN, PC_1)
C, D = CD_PRE[:28], CD_PRE[28:]
C_LIST, D_LIST = [deque(C)], [deque(D)]'''


# Left-shiftar C och D enligt tabellen och lägger in dem i varsin lista
'''for n, i in enumerate(LEFT_SHIFTS):
    C_LIST.append(C_LIST[n].copy())
    D_LIST.append(D_LIST[n].copy())
    C_LIST[n+1].rotate(-i)
    D_LIST[n+1].rotate(-i)'''


# Lägger in C och D som strings i nya listor
'''STRING_C_LIST = []
for i in C_LIST:
    res = ""
    for j in i:
        res += j
    STRING_C_LIST.append(res)

STRING_D_LIST = []
for i in D_LIST:
    res = ""
    for j in i:
        res += j
    STRING_D_LIST.append(res)'''


# Lägger ihop C och D och lägger in i en lista med 17 element
#CD_LIST = [STRING_C_LIST[i] + STRING_D_LIST[i] for i in range(17)]


# Ger en lista med K genom att permutera CD_n med PC_2
'''K_LIST = []
for i in range(1, 17):
    K_LIST.append(permutate(CD_LIST[i], PC_2))'''
K_LIST = ['110011010011111111101100111100000110011100101011', '011100111010010110111110001001111101110110010101', '111111001000110010110111000010110000010111110111', '111101111010101000111110110011111100100110000101', '101011101011011010110110010000100100011111011101', '111111100001111001111110110110111001000110001101', '111011101111001001111000110000100101011110101001', '100011101101111101111110010110100011101100101101', '101101111100011111010011001011001100010001110111', '011111110101001110110111100011111110110011000110', '101111111001000111011101101011001100011111010001', '000111110100001011111111100110111100011001000111', '101111110101100110111100110111101100011110000000', '100111100010101111101101100110000110011101001101', '100110110111111000111101111110101111001010000000', '011111011110110010001111000010111010100011111111']


# Permuterar binära M med IP och skapar L_0 och R_0
M_IP = permutate(M_BIN, IP)
L, R = M_IP[:32], M_IP[32:]
L_LIST, R_LIST = [L], [R]


# Next in the f calculation, we XOR the output E(Rn-1) with the key Kn
# Ln = Rn-1
# Rn = Ln-1 + f(Rn-1,Kn)

for i in range(1, 17):
    L_LIST.append(R_LIST[i-1])
    R_LIST.append(xor(L_LIST[i-1], f(R_LIST[i-1], K_LIST[16-i]), 32))
RL = R_LIST[16]+L_LIST[16]
print(int(str(permutate(RL, IP_1)), base=2))

