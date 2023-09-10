
print('Calculo da media dos alunos\n---------------------------')

alunos = {}
numero_de_notas = 4

while True:

    notas = []
    nome = input('Digite o nome do aluno: ').capitalize()

    ## Se o valor for alpha(letras de A - Z), ele irá retornar "True" na função ".isalpha()", assim
    ## entrando no "if not", ou seja, se não tiver apenas letras de (A - Z) ele irá entrar no if not
    ## pois a função irá retornar "False".
    ## ex:
    ## "Gabriel", irá retornar "True", pois, só tem letras de (A - Z)
    ## "Gabriel123", irá retornar "False", pois, não contém apenas letras de (A - Z).
    if not nome.isalpha():
        print('Por favor, digite um nome válido')

    else:

        ## Irá obter as notas baseado no número de notas definido anteriormente.
        for i in range(numero_de_notas):
            nota = float(input('Digite a nota: '))
            notas.append(nota)

        alunos[nome] = notas

        ## Confirmação para colocar mais alunos ou não.
        print("-----------------------")

        confirm = input("Você deseja continuar?[S/N] ").lower()

        print("-----------------------")

        if confirm == "s":
            continue

        elif confirm == "n":
            break

## O primeiro "for" irá retornar todas as "keys", ou seja, "chaves" do dicionário "alunos"
## o que deveria retornar todos os NOMES.
for aluno in alunos.keys():

    usable_notes = []
    notas_total = 0

    ## O segundo "for", irá obter as notas do aluno do primeiro "for", ou seja, vamos coletar
    ## as notas e armazenar na lista "usable_notes".
    ## Para extrair a média, iremos fazer a soma no for, e a divisão depois.
    for notas in alunos.get(aluno):
        usable_notes.append(notas)
        notas_total += notas

    media = notas_total / numero_de_notas

    ## Se a média for 8, ele irá dizer "aprovado"
    ## Se for maior ou igual que 5/menor que 7, ele irá dizer "recuperação"
    ## Se for menor que 5, ele irá entrar no else e dizer "reprovado"
    if media >= 8:

        print('Aluno: {}\n Nota: {}\n Nota: {}\n Nota: {}\n Nota: {}\n Media: {}\n APROVADO!'.format(aluno,
                                                                                                     usable_notes[0],
                                                                                                     usable_notes[1],
                                                                                                     usable_notes[2],
                                                                                                     usable_notes[3],
                                                                                                     media))
        print("-------------------")

    elif 5 <= media < 7:

        print('Aluno: {}\n Nota: {}\n Nota: {}\n Nota: {}\n Nota: {}\n Media: {}\n RECUPERAÇÃO!'.format(aluno,
                                                                                                        usable_notes[0],
                                                                                                        usable_notes[1],
                                                                                                        usable_notes[2],
                                                                                                        usable_notes[3],
                                                                                                        media))
        print("-------------------")

    else:

        print('Aluno: {}\n Nota: {}\n Nota: {}\n Nota: {}\n Nota: {}\n Media: {}\n REPROVADO!'.format(aluno,
                                                                                                      usable_notes[0],
                                                                                                      usable_notes[1],
                                                                                                      usable_notes[2],
                                                                                                      usable_notes[3],
                                                                                                      media))
        print("-------------------")

        with open('alunos.txt', 'w', newline='') as file:
            for line in alunos:
                file.write(line + os.linesep)
