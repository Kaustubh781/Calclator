while True:
    Operation = input("What do you wan't to do?")
    def add():
        number_one = int(input("Enter first number."))
        number_two = int(input("Enter second number."))
        print(number_one + number_two)
    def sub():
        number_one = int(input("Enter first number."))
        number_two = int(input("Enter second number."))
        print(number_one - number_two)
    def mul():
        number_one = int(input("Enter first number."))
        number_two = int(input("Enter second number."))
        print(number_one * number_two)
    def div():
        number_one = int(input("Enter first number."))
        number_two = int(input("Enter second number."))
        print(number_one / number_two)
    if Operation == "addition" :
        add()
    elif Operation == "subtraction" :
        sub()
    elif Operation == "multiply" :
        mul()
    elif Operation == "division" :
        div()
   
      
