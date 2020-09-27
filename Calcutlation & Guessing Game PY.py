import random

#addition game
while True:
    try:
        numberOne = int(input("enter first number"))
        numberTwo = int(input("enter second number"))
        break
    except ValueError:
        print("Only numbers allowed!")
        

if(numberTwo == 0):
    operators = ["+", "-", "*"]
else:
    operators = ["+", "-", "/", "*"]
    
randomOperator = random.choice(operators)
calculationLine = "{} {} {}".format(numberOne, randomOperator, numberTwo)
firstGameResult = eval(calculationLine)

superNumberGuessed = False

if(numberOne >= 9 and numberOne <= 12):
    print("You hit the secret number and won!")
    superNumberGuessed = True
else: 
    while(True):
        print("what is: {}".format(calculationLine))
        userCalc = int(input("enter the result"))
        if(userCalc == firstGameResult):
            print("Correct!")
            break
        else: 
            print("Wrong, try again...")
        
# guessing game
print("Guess a number between 0 and 10")
randomNumber = random.randint(0, 10)
anzahlTriesLeft = 10
while(anzahlTriesLeft > 0):
    guess = int(input("guess a number"))
    if(guess > randomNumber):
        print("Too high")
        anzahlTriesLeft -= 1
    elif(guess < randomNumber):
        print("Too low")
        anzahlTriesLeft -= 1
    else:
        print("You won! Congrats :)")
        break        
if(anzahlTriesLeft == 0):
    print("Fail!")