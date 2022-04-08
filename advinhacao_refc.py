def jogar():
    import random as rd

    print('\n\n***************************')
    print('Seja bem-vindo à advinhação')
    print('***************************')
    print("Deseja ler as intruções ou ir direto para o jogo?\n")
    print('Desejo ler instruções - 1', 'Quero apenas jogar - 2', sep='\n')
    pergunta = input("Digite uma das opções: ")
    print('*************************\n')

    instrucoes = ['É um jogo de advinhação onde você escolherá sua dificuldade.',
                  'A dificuldade escolhida vai implicar no tamanho da quantidade de possibilidades.',
                  'Você terá de chutar um número e ele terá de ser igual ao gerado pelo programa.',
                  'Existem três dificuldades: Fácil, médio e difícil.',
                  'Caso não encontre a solução, você perderá.',
                  'Existe um sistema de pontuação que será a diferença entre seu chute e o número gerado,',
                  'Sua pontuação variará conforme a dificuldade']

    while(pergunta != '1' and pergunta != '2'):
        print('Não existe essa opção!')
        pergunta = input("Digite uma das opções disponíveis: ")


    if (pergunta == '1'):
        for frase in instrucoes:
            print(frase, sep='\n')
    elif(pergunta == '2'):
        print("Iniciando o jogo\n")

    print("\nEscolha sua dificuldade:", 'Fácil -> 1  Médio -> 2  Difícil -> 3', sep='\n')
    dificuldade_escolhida = int(input('Digite sua dificuldade: '))
    dificuldade = 0

    if(dificuldade_escolhida == 1):
        dificuldade = 10
    elif(dificuldade_escolhida == 2):
        dificuldade = 20
    elif(dificuldade_escolhida == 3):
        dificuldade = 30

    tentativas_totais = 5
    index = 1
    # pontos = 1000

    while (index <= len(range(1, tentativas_totais + 1))):
            print(f'\nVocê está na rodada {index} de {tentativas_totais}\n')
            # print(f'Você tem {pontos} pontos')
            numero_secreto = rd.randrange(1, dificuldade+1)
           # print("número secreto: ", numero_secreto)
            chute = input(f"Chute um número entre 1 e {dificuldade}: ")

            if(chute.isnumeric() == True and int(chute) < 1 or int(chute) > dificuldade):
                print(f'Esse número não é válido. Escolha um número entre 1 e {dificuldade}')
                continue
            elif(chute.isnumeric() == False):
                print('Isto não é um número')
                continue

            if(int(chute) == numero_secreto):
                print('Parabéns, você acertou')
                break
            elif(int(chute) > numero_secreto):
                print('Seu chute é maior que o número secreto')
            elif(int(chute) < numero_secreto):
                print('Seu chute é menor que o número secreto\n')


            index +=1





if (__name__ == '__main__'):
    jogar()
