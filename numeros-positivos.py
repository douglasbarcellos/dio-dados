#TODO: Complete os espaços em branco com uma solução possível para o problema.
counter = 0
for number in range(6):  
    number = float(input())
    if number > 0:
      counter = counter + 1 
      
print("{} valores positivos".format(counter))
