if __name__ == "__main__":
    from rsa_modules import *
    #message = 1030114186110932
    message = str(input("Skriv in ditt meddelande. Det ska vara 16 siffror långt inga 0or "))
    while len(message) < 16:
        message += str(0)
    if len(message) > 16:
        message = message[0:16]
    message = int(message)
    p, q, F, n, e, d = key_gen()
    svar = encrypt(message, n, e)
    text = decrypt(svar, n, d)
    TEXT2 = ""
    for i in str(text).split("0"):
        if i:
            TEXT2 += i
    print(svar)
    print(TEXT2)