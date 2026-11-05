alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "UYEAD"
 
text = input("Enter message: ").upper()

#encrypt:C=(P+K)mod26
cipher=""
j=0
for ch in text:
    if ch in alphabet:
        p=alphabet.index(ch)
        k=alphabet.index(key[j%5])
        cipher=cipher+alphabet[(p+k)%26]
        j=j+1
    else:
        cipher=cipher+ch
#decrypt:P=(C-K)mod26
plain=""
j=0
for ch in cipher:
    if ch in alphabet:
        c=alphabet.index(ch)
        k=alphabet.index(key[j%5])
        plain=plain+alphabet[(c-k)%26]
        j=j+1
    else:
        plain=plain+ch
print("Encrypted message:", cipher)
print("Decrypted message:", plain)