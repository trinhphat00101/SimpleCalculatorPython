class Calculator:

    def start_calculate(self):
        res = 0
        choice = input("Enter choice: ")
        print("Your choice is: {}".format(choice))
        num_1 = int(input("Enter number 1: "))
        print("Enter fist number: {}".format(num_1))
        num_2 = int(input("Enter number 2: "))
        print("Enter second number: {}".format(num_2))
        if choice == "+":
            res = self.add(num_1, num_2)
        elif choice == "-":
            res = self.minus(num_1, num_2)
        elif choice == "*":
            res = self.mutiple(num_1, num_2)
        elif choice == "/":
            res = self.mutiple(num_1, num_2)
        print("The result is: {}".format(res))
        return res

    def add(self, num_1, num_2):
        return num_1 + num_2

    def minus(self, num_1, num_2):
        return num_1 - num_2

    def mutiple(self, num_1, num_2):
        return num_1 * num_2

    def divide(self, num_1, num_2):
        return num_1 / num_2


if __name__ == '__main__':
    cal = Calculator()
    cal.start_calculate()
