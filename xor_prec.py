def hex_op():
    pt = b"Malicious this is harm programme"
    key = 0xAA

    # Encryption
    ct = bytes([b^key for b in pt])

    print(f"Plaintext : {pt}")
    print(f"Plaintext hex : {pt.hex()}")
    print(f"Cipher bytes : {ct}")
    print(f"Cipher Hex : {ct.hex()}")
hex_op()


name = input(" what is your name? ")
print(f"Hello {name}")
st = input(f"{name} ! How are you?")
print("Have a good day!")
