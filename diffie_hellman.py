#DIFFIE HELLMAN KEY EXCHANGE

P = int(input("Enter Public Key P: ")) 
G = int(input("Enter Public Key G: ")) 

a = int(input("Enter Private Key of A: ")) 
b = int(input("Enter Private Key of B: "))

x = (G ** a) % P
y = (G ** b) % P

print(f"Public Key obtained by A:{x}")
print(f"Public Key obtained by B:{y}")

#Compute symmetric keys-

ka = (y ** a) % P
kb = (x ** b) % P

print(ka)
print(kb)