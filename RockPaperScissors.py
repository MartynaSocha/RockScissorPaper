import random
import sys
import time

choices= ['r','p','s']
userScore = 0       #zmienna do przechowywania wyniku uzytkonika
computerScore=0     #zmienna do przechowywania wyniku komputera

rnd = 1                  #ilosc rund poczatkowa
while True:
    userChoices = input("Please give me your choice: (p)apper, (s)cissore, (r)ock:\n")
    userChoices= userChoices.lower().strip()        #warunek na małe litery i usuniecie białych znaków
    computerChoice = random.choice(choices)
    print(userChoices,computerChoice)

    if userChoices=='w':#jezeli wybierze w to wyjdzie z gry
        print("End of the game")
        break
    if rnd==6:          #jesli liczba rund jest rowna 6 to wtedy wyjdz z gry
        break

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
        print("Invalid type.Try again or click w if you want to exit.")
        continue
    rnd+=1

print("Computer Score = ",computerScore, "User Score = ", userScore)
