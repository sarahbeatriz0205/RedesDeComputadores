# ip = "10.9.0.222"
# mask = "255.255.255.254"
ip = list(map(str, input("IP = ").split(".")))
mask = list(map(int, input("Máscara = ").split(".")))

binarioIP = []
binarioMask = []

def conversao_binario(num):
    bin = ""
    n = int(num)
    while n > 0:
        bin = bin + str((n%2))
        n = int(n//2) 
    bin = bin[::-1] # inverte a string
    bin = bin.zfill(8)
    return bin

for octeto in ip:
    binarioIP.append(conversao_binario(octeto))
for octeto in mask:
    binarioMask.append(conversao_binario(octeto))


concat = binarioMask[0] + binarioMask[1] + binarioMask[2] + binarioMask[3]
print("Máscara concatenada = ", concat)

 
def conversao_mascara(mask):
        mask = mask.mascara_binaria()
        for binarios in mask:
            inversao = ""
            for b in binarios:
                if b == "1":
                    b = "0"
                else:
                    b = "1"
            inversao = inversao + b
            return inversao
print(conversao_mascara(mask))
    
binIP = []
        
def ipv4_binario(ip):
    for byte in ip:
        bin = conversao_binario(byte)
        binIP.append(bin)
    return binIP




print("IP binário = ", *ipv4_binario(ip))

# print(*binIP)




