# def main():
    # number = float(input("\033[1;3m Type a number to see its square;\033[0m"))
    # square = number * number
    # print (f"{number} squared is {square}")

    # if __name__ == '__main__':
    #  main()







def main():
    num: float = float(input("\033[1;3m Type a number to see its square: \033[0m")) # Make sure to cast the input to a float so we can do math with it!
    print(str(num) + " squared is " + str(num ** 2)) # num * num is equivalent to num ** 2. The ** operator raises something to a power!


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
