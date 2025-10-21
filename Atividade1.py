class IPAdress:
    def __init__(self, ipv4, mask, ip):
        self.ipv4 = ipv4
        self.mask = mask
    
    def conversorIP(self, ipv4): # ELE VAI VIR COMO STR --> CONVERTA PRA INTEIRO, USE O BIN, ARRUME UMA FORMA DE CRIAR SUBLISTAS COM OS OCTETOS SEPARADOS BIT A BIT, FAÇA O AND DE OCTETO COM CADA OCTETO DA MÁSCARA, GUARDE ESSE VALOR DO AND
        for i in ipv4: # i = valor 
            binarioIP = bin(i)[2:] # número convertido em binário sem o 0b
            binarioIP = binarioIP.zfill(8) # adicionado oito zeros caso não tenham oito bits já
        return binarioIP # str
    
    def conversorMask(self, mask):
        binarioMask = bin(mask)[2:]
        binarioMask = binarioMask.zfill(26)
        return binarioMask # str
    
    def sublistaBinariaIP(self, ipv4):
        ip = ipv4.conversorIP()
        sublistas = []
        for i in ip:
            for j in i:
                sublistas.append(j)
        todos_digitosIP = []
        for sub in sublistas:
            for n in sub:           
                todos_digitosIP.append(int(n))
        return todos_digitosIP
    
    def sublistaBinariaMask(self, mask):
        m = mask.conversorMask()
        sublista = []
        for i in m:
            for j in i:
                sublista.append(j)
        todos_digitosMask = []
        for sub in sublista:
            for n in sub:           
                todos_digitosMask.append(int(n))
        return todos_digitosMask   
        
    # o endereço da rede correspondente ao IP e máscara. (Atributo rede)
    def endereco_rede(self, ipv4, mask):
        ip = ipv4.sublistaBinariaIP()
        m = mask.sublistaBinariaMask()
        operacaoAnd = ip & m # endereço de rede
        return operacaoAnd
        
    # o endereço de broadcast da rede.  (Atributo broadcast)
    def broadcast(self, mask, ipv4):
        m = mask.sublistaBinariaMask()
        ip = ipv4.sublistaBinariaIP()
        for b in m: # na teoria é um complemento de 2
            if b == 1:
                b = 0
            else:
                b = 1   
        operacaoOr = ip or m
        return operacaoOr
    
    # recebe um endereço IP (string) e retorna True se este IP pertencer à mesma rede da instância, ou False caso contrário.
    def pertence_a_rede(self, ip):
        pass



class UI:
    def menu():
        ipv4 = list(map(str, input().split("."))) # recebe o ip em str separado por "." 
        mask = input("Máscara: ")