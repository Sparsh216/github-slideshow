import random

i=random.randint(1,100)
# print(i)

print ('''***************************************\n
Welcome to the guess game, Lets play!!!\n
***************************************\n''')
print("Computer has choosen the number its your time to guess it\nlets see how many guess you will take")
try:
    choice=-1
    counter=1
    while (choice!=i):
        choice=int(input("Choose a number between 1 and 100: "))
        if(choice<i):
            print("Oops!, wrong number. Greater number please ")
        elif(choice>i):
            print("Oops!, wrong number. Smaller number please ")
        counter=counter+1
    print(f"Congrats You guess the correct number in {counter} guesses")
except:
    print("Wrong input, Rerun the game")
