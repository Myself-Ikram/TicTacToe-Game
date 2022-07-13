#importing Random library for computer turns!
from random import randrange
totalMoves = 1
remainingBlocks = [0,1,2,3,5,6,7,8]
#Here the computer starts first
#Computer places the X pon middle block
t = [0,1,2,3,"X",5,6,7,8]
#Defining board 
def tttBoard():
    t = [0,1,2,3,"X",5,6,7,8]
    print("Computer's Turn")
    print("+","-------+" *3,sep="")
    print("|",t[0],"|",t[1],"|",t[2],"|", sep="   ")
    print("+","-------+" *3,sep="")
    print("|",t[3],"|",t[4],"|",t[5],"|", sep="   ")
    print("+","-------+" *3,sep="")
    print("|",t[6],"|",t[7],"|",t[8],"|", sep="   ")
    print("+","-------+" *3,sep="")
#Game Continues using this function
def gameBegin(userMove,computerMove):
    t[userMove] = "O"
    t[computerMove] = "X"
    print("+","-------+" *3,sep="")
    print("|",t[0],"|",t[1],"|",t[2],"|", sep="   ")
    print("+","-------+" *3,sep="")
    print("|",t[3],"|",t[4],"|",t[5],"|", sep="   ")
    print("+","-------+" *3,sep="")
    print("|",t[6],"|",t[7],"|",t[8],"|", sep="   ")
    print("+","-------+" *3,sep="")
# Computer movve is selected here
#It takes remaining blocks as attribute and selects from that list only
# Inorder to avoid same block selection
def cMove(remainingBlocks):
    while True:
        r = randrange(8)
        if r in remainingBlocks:
            remainingBlocks.remove(r)
            return r
tttBoard()   
# I have set the totalMoves 4, as Highest possible moves are not more than the 4(from users side)
while totalMoves <= 4:
    totalMoves +=1
    print(remainingBlocks)
    userMove = int(input("Enter your move :"))
    remainingBlocks.remove(userMove)
    computerMove = cMove(remainingBlocks)
    gameBegin(userMove,computerMove)
    print(userMove,computerMove)
    
#This conditions determines whether the User won /Computer won /It is a Tie
if t[0] == t[4] == t[8] or t[2] == t[4] == t[6] or t[0] == t[3] == t[6] or t[1] == t[4] == t[7] or t[2] == t[5] == t[8] or t[0] == t[1] == t[2] or t[3] == t[4] == t[5] or t[6] == t[7] == t[8]:
    print("Computer won")
elif t[0] == t[3] == t[6] or t[2] == t[5] == t[8] or t[0] == t[1] == t[2] or t[6] == t[7] == t[8]:
    print("You won")
else:
    print("Tie")
