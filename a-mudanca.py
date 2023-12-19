while True:
    try:

        graus = int(input())
        
        if graus == 360 or graus >= 0 and graus < 90:
          msg = 'Bom Dia!!'
        elif graus >= 90 and graus < 180:
          msg = 'Boa Tarde!!'
        elif graus >= 180 and graus < 270:
          msg = 'Boa Noite!!'
        else :
          msg = 'De Madrugada!!'
        
        print(msg)  


    except EOFError:
        break