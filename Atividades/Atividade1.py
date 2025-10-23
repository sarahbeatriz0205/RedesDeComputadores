class IPAdress:
    def __init__(self, ipv4, mask):
        mask = list(map(str, mask.split(".")))
        ipv4 = list(map(str, ipv4.split(".")))

        self.ipv4 = ipv4
        self.mask = mask

        # endereço de rede
        endereco_rede = []
        mask = self.mascara_binaria()
        ip = self.ipv4_binario()
        for i in range(len(ip)):
            endereco = int(ip[i], 2) & int(mask[i], 2)
            endereco_rede.append(endereco)
        self.rede = endereco_rede

        # endereço de broadcast
        endereco_broadcast = []
        mask = self.conversao_mascara()
        ip = self.ipv4_binario()
        for i in range(len(ip)):
            broadcast = int(ip[i], 2) | mask[i]
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
        return bin
    
    def ipv4_binario(self):
        binIP = []
        for byte in self.ipv4:
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
        conversao = []
        mascara = self.mascara_binaria()
        for octeto in mascara:
            novo_octeto = ""
            for bit in octeto:
                if bit == "1":
                    novo_octeto += "0"
                else:
                    novo_octeto += "1"
            conversao.append(int(novo_octeto, 2))
        return conversao
    
    def mascara_cidr(self):
        mask = self.mascara_binaria()
        qtd_bits_1 = 0
        for octeto in mask:
            for bit in octeto:
                if bit == "1":
                    qtd_bits_1 += 1
        return qtd_bits_1

    
    def pertence_a_rede(self, ip):
        ip = list(ip.split("."))
        binario_recebido = []
        for octeto in ip:
            binario_recebido.append(self.conversao_binario(octeto))
        
        binario_mascara = []
        for oc in self.mask:
            binario_mascara.append(self.conversao_binario(oc))

        pertence_rede = []
        for i in range(4):
            pertence_rede.append(int(binario_recebido[i], 2) & int(binario_mascara[i], 2))
        
        if pertence_rede == self.rede:
            return True
        else:
            return False
        
    def __str__(self):
        return f"Em CIDR = {self.ipv4}/{self.mascara_cidr()}"

# TESTE    
# ip = IPAdress("192.168.1.85", "255.255.255.0")
# print(ip)
# ip = IPAdress("192.168.1.85", "255.255.255.0")
# print("IP:", ip.ipv4)
# print("Máscara:", ip.mask)
# print("Rede:", ip.rede)
# print("Broadcast:", ip.broadcast)
# print("192.168.1.100 pertence à rede?", ip.pertence_a_rede("192.168.1.100"))
# print("192.168.2.1 pertence à rede?", ip.pertence_a_rede("192.168.2.1"))