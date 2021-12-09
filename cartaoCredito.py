class CartaoCredito :
    __nome = None
    __numCartao = None
    __limite = None

    #Getters (métodos GET)
    def get_Nome(self):
        return self.__nome

    def get_NumCartao(self):
        return self.__numCartao

    def get_Limite(self):
        return self.__limite
    
    #Setters (métodos SET)
    def set_Nome(self, nome):
        self.__nome = nome

    def set_NumCartao(self, numCartao):
        self.__numCartao = numCartao

    def set_Limite(self, limite):
        self.__limite = limite
    
    #Usar Crédito
    def usarCredito(self, sacar):
        if float(sacar) <= self.__limite:
            print('Transação Aprovada')
            self.__limite = self.__limite - sacar
            print('Limite atualizado:', self.__limite, 'R$')
        else:
            print('Operação não autorizada, limite disponível:', self.__limite, 'R$')
    
    #Pagar Fatura
    def pagarFatura(self, pagar):
        self.__limite = self.__limite + float(pagar)
        print('Limite adicionado:', pagar, 'R$', '\n\tLimite atualizado:', self.__limite, 'R$')
        
#####Fim do cartão de crédito####################