while True:
    try:
        x = int(input("please enter a number :"))
        break
    except ValueError:
        print ("oppzzz that was no valid number. try again")