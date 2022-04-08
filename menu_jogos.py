print('************************')
print('**** Seja bem-vindo ****')
print('************************')

print("-----Escolha seu jogo-----")
print('Adivinhação(1) ou Forca(2)')
escolha = input("Digite seu jogo: ")

while(escolha != "1" and escolha != "2"):
    print('Esse dígito não vale.')
    escolha = input("Digite seu jogo: ")

if(escolha == '1'):
    from advinhacao_refc import jogar
    jogar()
else:
    from forca_refc import jogar
    jogar()
