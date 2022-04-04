if __name__ == "__main__":
    from rsa_modules import *
    #message = 1030114186110932
    message = int(input("Skriv in ditt meddelande. Det ska vara 16 bokstäver långt."))
    p, q, F, n, e, d = key_gen(128)
    svar = encrypt(message, n, e)