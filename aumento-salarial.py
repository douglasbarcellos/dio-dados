# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = float(input()) 

if (salario >= 0 and salario <= 600.00):
  reajuste = salario * 17 / 100
  novoSalario = salario + reajuste
  
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 17 %''')
           
elif (salario > 600.00 and salario <= 900.00):
  reajuste = salario * 13 / 100
  novoSalario = salario + reajuste
    
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 13 %''')

elif (salario > 900.00 and salario <= 1500.00):
  reajuste = salario * 12 / 100
  novoSalario = salario + reajuste
  
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 12 %''')

elif (salario > 1500 and salario <= 2000.00):
  reajuste = salario * 10 / 100
  novoSalario = salario + reajuste
  
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 10 %''' )

else: 
  reajuste = salario * 5 / 100
  novoSalario = salario + reajuste
  
  print(f'''Novo salario: {novoSalario: .2f}
           Reajuste ganho: {reajuste: .2f}
             
           Em percentual: 5 %''')

# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)