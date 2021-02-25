#use this module to draw a butterfly

class NumberError(Exception):
    "I used this class to create a new type of exception"
    pass

class Butterfly:
    "use this class to draw a Butterfly"
    def __init__(self, row):
        self.row = row
        self.draw(row)

    def draw(self, row):
        if row % 2 == 0:
            star = row // 2
            # Upper part
            for i in range(1, star + 1):
                for j in range(1, 2 * star + 1):
                    if j > i and j < 2 * star + 1 - i:
                        print("  ", end="")
                    else:
                        print("* ", end="")
                print()

            # Lower part
            for i in range(star, 0, -1):
                for j in range(2 * star, 0, -1):
                    if j > i and j < 2 * star + 1 - i:
                        print("  ", end="")
                    else:
                        print("* ", end="")
                print()   
        else:
            raise NumberError("check your input number (You must pass EVEN number NOT ODD, Type must be INT NOT OTHERS)")
            

    def get_star_num(self):
        "use this method to get number of stars"
        "you can use this function ==> f(x) = ((x ** 2) / 2) + x ==> x is row"
        result = int(((self.row ** 2) / 2) + self.row)
        print(f"stars number ==> {result}")

