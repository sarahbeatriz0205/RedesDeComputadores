class IPAdress:
    def __init__(self, ipv4, mask):
        self.ipv4 = ipv4
        self.mask = mask

        # endereço de rede
        endereco_rede = []
        mask = self.mascara_binaria()
        ip = self.ipv4_binario()
        for i in range(len(ip)):
            endereco = ip[i] & mask[i]
            endereco_rede.append(endereco)
        self.rede = endereco_rede

        # endereeço de broadcast
        endereco_broadcast = []
        mask = self.conversao_mascara()
        ip = self.ipv4_binario()
        for i in range(len(ip)):
            broadcast = (ip[i] | mask[i])
            endereco_broadcast.append(broadcast)
        self.broadcast = endereco_broadcast
    
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
            inversao = int(inversao) # convertido pra int?
            lista_mascara_convertida.append(inversao)
        return lista_mascara_convertida
    
    def pertence_a_rede(self, ip):
        ip = list(ip.split("."))
        for octeto in ip:
            bin_ip_recebido = self.conversao_binario(octeto)
        for oc in self.mask:
            bin_mascara = self.conversao_binario(oc)
        for o in self.rede:
            bin_rede = self.conversao_binario(o)
        pertence_rede = bin_ip_recebido & bin_mascara
        if pertence_rede == bin_rede:
            return True
        else:
            return False
        
    def __str__(self):
        return f"Endereço IP no formato CIDR: "