def sl(st):
    print(len(st))
    ulta_word = st[::-1]
    print(ulta_word)
    sida_word = ulta_word[::-1]
    print(sida_word)
sen = "whole of words"
print(sl(sen))

def hidden(word):
    key = 0xAA
    try:
        # Encrypt
        ct = bytes([b^key for b in word])
        print(f"plaintext: {word}")
        print(f"plantext hex: {word.hex()}")
        print(f"Chiper txt : {ct}")
        chiper_hidden = ct[::-1]
        print(f"ulta_chiper : {chiper_hidden}")
        print(f"Chiper txt hex: {ct.hex()}")
    except Exception as e:
        print(" kuch gadbad hai: ",e)

fruit =b"Mango"
print(hidden(fruit))
