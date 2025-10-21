# ip = "10.9.0.222"
# mask = "255.255.255.254"
ip = list(map(int, input("IP = ").split(".")))
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

# for bin in mask:
#     conversao_binario(mask[bin]) # erro
#     inversao = ""
#     for b in bin:
#         if b == "1":
#             b = "0"
#         else:
#             b = "1"
#     inversao = inversao + b

# print(inversao)