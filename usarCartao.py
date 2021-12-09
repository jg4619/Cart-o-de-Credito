from cartaoCredito import CartaoCredito

conta1 = CartaoCredito()
conta1.set_Limite(700)
print("Seu limite:", conta1.get_Limite(), 'R$')
print('-----------------------------')

conta1.usarCredito(500)
conta1.usarCredito(400)

conta1.pagarFatura(200)
conta1.usarCredito(400)