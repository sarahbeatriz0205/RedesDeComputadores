class IPAddress:
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
            endereco = str(endereco)
            endereco_rede.append(endereco)
        concat = endereco_rede[0] + "." + endereco_rede[1] + "." + endereco_rede[2] + "." +  endereco_rede[3]
        self.rede = concat

        # endereço de broadcast
        endereco_broadcast = []
        mask = self.conversao_mascara()
        ip = self.ipv4_binario()
        for i in range(len(ip)):
            broadcast = int(ip[i], 2) | mask[i]
            broadcast = str(broadcast)
            endereco_broadcast.append(broadcast)
        concat = endereco_broadcast[0] + "." + endereco_broadcast[1] + "." + endereco_broadcast[2] + "." + endereco_broadcast[3]
        self.broadcast = concat
    
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
        
        pertence_rede_novo = []
        for rede in pertence_rede:
            string = str(rede)
            pertence_rede_novo.append(string)
        concat = pertence_rede_novo[0] + "." + pertence_rede_novo[1] + "." + pertence_rede_novo[2] + "." + pertence_rede_novo[3]
        
        if concat == self.rede:
            return True
        else:
            return False
        
    def __str__(self):
        ipv4_str = ".".join(self.ipv4)
        return f"Em CIDR = {ipv4_str}/{self.mascara_cidr()}"

ip = IPAddress("192.168.1.10", "255.255.255.0")
print(ip)                                # Saída esperada: "192.168.1.10/24"
print("Endereço de rede = ", ip.rede)                  # "192.168.1.0"
print("Endereço de broadcast = ", ip.broadcast)             # "192.168.1.255"
print(ip.pertence_a_rede("192.168.1.55"))  # True
print(ip.pertence_a_rede("192.168.2.1"))   # False