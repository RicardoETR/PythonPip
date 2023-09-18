import random

#funcion para cambiar el formato de entrada 
def optionFormat(optionUser):
    if int(optionUser) == 1:
        return 'piedra'
    elif int(optionUser) == 2:
        return 'papel'
    elif int(optionUser) == 3:
        return 'tijeras'
    else:
        return optionUser

#funcion para escoger entre piedra papel o tijeras
def chooseOptions():
    options = ('piedra', 'papel', 'tijeras')
    optionComputer = random.choice(options)
    optionUser = input('1.-piedra, 2.-papel o 3.-tijeras:\n').lower()
    return(optionComputer, optionFormat(optionUser))

#funcion de procesamiento de reglas
def rulesGame(optionComputer, optionUser): 
    if optionUser == optionComputer:
        return 0,0
    elif ((optionUser == 'tijeras' and optionComputer == 'papel') or
        (optionUser == 'papel' and optionComputer == 'piedra') or
        (optionUser == 'piedra' and optionComputer == 'tijeras')):
        return 0,1
    else:
        return 1,0

#funcion para ejecutar el juego, el main
def runGame():
    scoreComputer, scoreUser = 0,0
    print('Juego de Priedra Papel o Tijeras')
    optionComputer, optionUser = chooseOptions()
    scoreComputer, scoreUser = rulesGame(optionComputer, optionUser)
    if scoreComputer == scoreUser:
        print('EMPATE')
    elif scoreUser > scoreComputer:
        print('Gana Usuario')
    else:
        print('Gana Computador')
    print(f"Score Computer: {scoreComputer} and Score User: {scoreUser}")
runGame()