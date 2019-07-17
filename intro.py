#print('Digite seu nome:')
#nome = input()

# print ('O nome digitado for: '+ nome)

print('Digite sua idade:')
idade = int(input())
if idade <= 20 and idade >= 30:
    print('Idade não permitida')

print('Digite seu salário:')
salario = int(input())
if salario <= 1000 and salario >= 5000:
    print ('Salário não permitido')

print('Digite o valor do empréstimo:')
emprestimo = input()
if emprestimo <= 5*salario:
    print('Emprestimo liberado')
    
        
    