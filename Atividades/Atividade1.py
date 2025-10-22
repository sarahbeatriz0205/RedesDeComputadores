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
    
    def ipv4_binario(self):
        binIP = []
        for byte in self.ip:
            bin_endereco = self.conversao_binario(byte)
            binIP.append(bin_endereco)
        return binIP
    
    def mascara_binaria(self):
        binMascara = []
        for byte in self.mask:
            bin_m = self.conversao_binario(byte)
            binMascara.append(bin_m)
        return binMascara

    def conversao_mascara(self):
        mask = self.mascara_binaria()
        inversao = ""
        lista_mascara_convertida = []
        for binarios in mask:
            for b in binarios:
                if b == "1":
                    b = "0"
                    inversao = inversao + b
                else:
                    b = "1"
                    inversao = inversao + b
            lista_mascara_convertida.append(inversao)
        return lista_mascara_convertida
    
    def endereco_de_rede(self):
        endereco_rede = []
        mask = self.mascara_binaria()
        ip = self.ipv4_binario()
        for i in range(len(ip)):
            endereco = ip[i] & mask[i]
        endereco_rede.append(endereco)
        return endereco
    
    def broadcast(self):
        endereco_broadcast = []
        mask = self.conversao_mascara()
        ip = self.ipv4_binario()
        for i in range(len(ip)):
            broadcast = (ip[i] | mask[i])
            endereco_broadcast.append(broadcast)
        return endereco_broadcast
    

# falta consertar o conversao_mascara() de str pra int