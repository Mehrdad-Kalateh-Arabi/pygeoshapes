# use this module to draw a kite 
class NumberError(Exception):
    "I used this class to create a new type of exception"
    pass

class Kite:
    "use this class to draw a kite"
    def __init__(self, star_num):
        self.star_num = star_num
        self.draw(star_num)

    def draw(self, star_num):
        if star_num % 2 != 0:
            space = star_num 
            star = 1
            for i in range(star_num - 1):
                print((star_num - i) * ' ' + (2 * i + 1) * '*')
            for i in range(star_num - 1, -1, -1):
                print((star_num - i) * ' ' + (2 * i + 1) * '*')   
        else:
            raise NumberError("check your input number (You must pass ODD number NOT EVEN, Type must be INT NOT OTHERS)")

    def get_star_num(self):
        "use this method to get number of stars"
        "you can use this function ==> f(x) = x ** 2  ===> x is star_num"
        result = self.star_num ** 2
        print(f"stars number ==> {result}")



