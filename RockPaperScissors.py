import random
import time

choices= ['r','p','s']
userScore = 0       #zmienna do przechowywania wyniku uzytkonika
computerScore=0     #zmienna do przechowywania wyniku komputera

i=0
while i <2:
    userChoices = input("Please give me your choice: (p)apper, (s)cissore, (r)ock:\n")
    userChoices= userChoices.lower().strip()        #warunek na małe litery i usuniecie białych znaków
    computerChoice = random.choice(choices)
    print(userChoices,computerChoice)
    if len(userChoices)==0:      #sprawdzenie czy użytkownik podal cokolwiek
        print('Try again')
        time.sleep(10)           #czas jaki bedzie czekal na odpowiedz w sekundach
    if userChoices == computerChoice:
        print("Draw")
    elif userChoices == 'r' and computerChoice=='p':
        print("Computer win")
        computerScore+=1
    elif userChoices == 'r' and computerChoice == 's':
        print("User win")
        userScore+=1
    elif userChoices == 'p' and computerChoice == 'r':
        print("User win")
        userScore += 1
    elif userChoices == 'p' and computerChoice == 's':
        print("Computer win")
        computerScore += 1
    elif userChoices == 's' and computerChoice == 'p':
        print("User win")
        userScore += 1
    elif userChoices == 's' and computerChoice == 'r':
        print("Computer win")
        computerScore += 1
    else:
        print("Invalid type.Try again")
        continue
    i+=1
print("Computer Score = ",computerScore, "User Score = ", userScore)
