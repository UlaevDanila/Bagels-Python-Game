from numberDivider import numberDivider

def gameCycle(gameVariableHandler, dividedSecret, i = 0):
    digitsVariable = 0
    
    while gameVariableHandler:
        userInput = int(input("Введите число: "))
        userDividedInput = numberDivider(userInput)

        rightDigits = 0


        for j in range(len(dividedSecret)):

            for k in range(len(dividedSecret)):

                if userDividedInput[j] == dividedSecret[j]:
                    print("Число ", userDividedInput[j], " стоит правильно")

                    digitsVariable = 0
                    i += 1
                    rightDigits += 1


                elif userDividedInput[j] == dividedSecret[k]:
                    print("Цифра ", userDividedInput[j],  " есть в числе, но стоит она не на своём месте")
                    
                    i += 1
                    digitsVariable = 0


                else:
                    digitsVariable += 1
                    i += 1

        if digitsVariable == len(userDividedInput):
            print("Данных цифр в числе нет")
            digitsVariable = 0


        if rightDigits == len(dividedSecret):
            print("Ты угадал")
            break

        if i == 10:
            print("Ты проиграл")
            break     
