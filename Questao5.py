quantidade_aluno = 10
somatoria = 0

for i in range(quantidade_aluno):
    nota = int(input(f'Digite a nota do {i+1}º: '))
    somatoria += nota

media = somatoria/quantidade_aluno

print(f'A media da turma é: {media}')
