import random
Choice = random.randint(1, 3)
tentatives=0
while True:
    try:
        print("Choose Rock(1), Paper(2) or Scissors(3)")
        Player = int(input())
        if Player == Choice:
            print("Tie")
            tentatives+=1
        elif Player == 1 and Choice == 2:
            print("You lose the computer chose Paper")
            tentatives+=1
        elif Player == 1 and Choice == 3:
            print("You win the computer chose Scissors")
            tentatives+=1
        elif Player == 2 and Choice == 1:
            print("You win the computer chose Rock")
            tentatives+=1
        elif Player == 2 and Choice == 3:
            print("You lose the computer chose Scissors")
            tentatives+=1
        elif Player == 3 and Choice == 1:
            print("You lose the computer chose Rock")
            tentatives+=1
        elif Player == 3 and Choice == 2:
            print("You win the computer chose Paper")
            tentatives+=1
        else:
            print("Invalid choice")
            tentatives+=1
    except ValueError:
        print("Invalid choice")
        tentatives+=1
    if tentatives==3:
        break