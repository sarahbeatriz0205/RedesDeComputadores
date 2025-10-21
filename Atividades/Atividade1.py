class IPAdress:
    def __init__(self, ipv4, mask):
        self.ipv4 = ipv4
        self.mask = mask
    
    def conversao_binario(self, num):
        bin = ""
        n = int(num)
        while n > 0:
            bin = bin + str((n%2))
            n = int(n//2) 
        bin = bin[::-1] # inverte a string
        bin = bin.zfill(8)
        bin = int(bin)
        return bin
    
    def conversao_mascara(self, mask):
        mask = mask.conversao_binario(mask)
        for binarios in mask:
            inversao = ""
            for b in binarios:
                if b == "1":
                    b = "0"
                else:
                    b = "1"
            inversao = inversao + b

# binarioIP = []
# binarioMask = []
# for octeto in ip:
#     binarioIP.append(conversao_binario(octeto))
# for octeto in mask:
#     binarioMask.append(conversao_binario(octeto))
    
