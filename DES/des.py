if __name__ == "__main__":
    from des_modules import *

    MSG = "1030114186110932"
    KEY = "0001001100110100010101110111100110010011001000010000010001010001"
    BIN_KEYS, HEX_KEYS = generate_keys(KEY)
    CIPHER = encrypt(MSG, BIN_KEYS, HEX_KEYS)
    TEXT = decrypt(CIPHER, BIN_KEYS, HEX_KEYS)
