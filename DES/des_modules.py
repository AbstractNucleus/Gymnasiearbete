from tables import *
import time


# Översätter binärt till decimal
def bin_to_dec(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


# Decimal to binary conversion
def dec_to_bin(num):
    res = bin(num).replace("0b", "")
    if len(res) % 4 != 0:
        div = len(res) / 4
        div = int(div)
        counter = (4 * (div + 1)) - len(res)
        for i in range(0, counter):
            res = "0" + res
    return res


# Hexadecimal to binary conversion
def hex_to_bin(s):
    bin = ""
    for i in range(len(s)):
        bin += HEX_TO_BIN[s[i]]
    return bin


# Binary to hexadecimal conversion
def bin_to_hex(s):
    hex = ""
    for i in range(0, len(s), 4):
        ch = ""
        ch += s[i]
        ch += s[i + 1]
        ch += s[i + 2]
        ch += s[i + 3]
        hex += BIN_TO_HEX[ch]
    return hex


def left_shift(k, nth_shifts):
    s = ""
    for i in range(nth_shifts):
        for j in range(1, len(k)):
            s += k[j]
        s += k[0]
        k = s
        s = ""
    return k


# XOR funktion som går att använda med strings
def xor(a, b):
    ans = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            ans += "0"
        else:
            ans += "1"
    return ans


# En funnktion för att permutera en string med ett table
def permutate(string, table, n):
    output = ""
    for i in range(0, len(table)):
        output += str(string[table[i] - 1])
    return output


def generate_keys(KEY):
    # Skapar listor för nycklarna
    BIN_KEYS = []

    # Gör nyckeln till 56-bit
    KEY = permutate(KEY, PC_1, 56)

    # Delar upp nyckeln till vänster och höger led
    LEFT, RIGHT = KEY[0:28], KEY[28:56]

    # Genererar sub-keys
    for i in range(16):
        LEFT, RIGHT = left_shift(LEFT, LEFT_SHIFTS[i]), left_shift(
            RIGHT, LEFT_SHIFTS[i]
        )
        COMBINED = LEFT + RIGHT
        BIN_KEYS.append(permutate(COMBINED, PC_2, 48))

    return BIN_KEYS


def encrypt(MSG, KEYS,):
    MSG = hex_to_bin(MSG)
    MSG = permutate(MSG, IP, 64)

    LEFT, RIGHT = MSG[0:32], MSG[32:64]

    for i in range(0, 16):
        RIGHT_EXPAND = permutate(RIGHT, E_BIT, 48)

        XOR_X = xor(RIGHT_EXPAND, KEYS[i])

        S_BOX_STR = ""
        for j in range(0, 8):
            ROW = bin_to_dec(int(XOR_X[j * 6] + XOR_X[j * 6 + 5]))
            COL = bin_to_dec(
                int(
                    XOR_X[j * 6 + 1]
                    + XOR_X[j * 6 + 2]
                    + XOR_X[j * 6 + 3]
                    + XOR_X[j * 6 + 4]
                )
            )
            VAL = S_BOX[j][ROW][COL]
            S_BOX_STR = S_BOX_STR + dec_to_bin(VAL)

        S_BOX_STR = permutate(S_BOX_STR, P, 32)

        LEFT = xor(LEFT, S_BOX_STR)

        if i != 15:
            LEFT, RIGHT = RIGHT, LEFT

        COMBINED = LEFT + RIGHT

    return bin_to_hex(permutate(COMBINED, IP_1, 64))


def decrypt(CIPHER, KEYS):
    KEYS_REVERSED = KEYS[::-1]
    return encrypt(CIPHER, KEYS_REVERSED)


def take_time_gen(KEY):
    t0 = time.time()
    BIN_KEYS = generate_keys(KEY)
    return time.time() - t0


def hack():
    pass
