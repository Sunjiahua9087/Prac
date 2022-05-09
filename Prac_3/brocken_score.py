import random

score = random.randint(0,100)
def main():
    if score < 0:
        print("your score is",score,"Invalid score")
    else:
        if score > 100:
         print("your score is",score,"Invalid score")
        elif 100> score > 90:
            print("your score is",score,"Excellent")
        elif 90> score > 50:
            print("your score is",score,"Passable")
        else:
            print("your score is",score,"Bad")
main()