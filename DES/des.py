if __name__ == "__main__":
    y = ""
    from des_modules import *
    MSG = input("Skriv in 16st siffror inga 0or ")
    try:
        MSG = int(MSG)
        MSG = str(MSG)
    except:
        print("endast siffror")
    for i in range(len(MSG)):
        y += str(MSG[i])
    #print(y)
    while len(y) < 64:
        y += str(0)
    if len(y) > 64:
        y = y[0:64]
    MSG = y
    #MSG = "1030114186110932"
    KEY = "0001001100110100010101110111100110010011001000010000010001010001"
    BIN_KEYS = generate_keys(KEY)
    CIPHER = encrypt(MSG, BIN_KEYS)
    TEXT = decrypt(CIPHER, BIN_KEYS)
    print("ciffret:",CIPHER)
    TEXT2 = ""
    for i in TEXT.split("0"):
        if i:
            TEXT2 += i
    print("decrypterat", TEXT2)