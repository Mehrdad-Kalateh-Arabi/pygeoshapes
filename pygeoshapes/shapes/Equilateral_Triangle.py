# use this module to draw an equilateral triangle by entring an odd number

class NumberError(Exception):
    "I used this class to create a new type of error (NumberError)"
    pass

class Equilateral_Triangle:
    "use this class to draw an equilateral triangle"
    def __init__(self, star_num):
        self.star_num = star_num
        self.draw(star_num)

    def draw(self, star_num):
        space = star_num
        star = 1
        if star_num % 2 != 0:
            for i in range(1, star_num + 1):
                print ((' ' * space) + ('* ' * (i))) 
                space -= 1
        else:
            raise NumberError("check your input number (You must pass ODD number NOT EVEN, Type must be INT NOT OTHERS)")

    def get_star_num(self):
        "you can use this function to find number of stars: f(x) = ((x ** 2) + x) / 2 ==> x is star_num"
        "x parameter is same that star_num"
        result = ((self.star_num ** 2) + self.star_num) / 2
        print(f"stars number ==> {int(result)}")





