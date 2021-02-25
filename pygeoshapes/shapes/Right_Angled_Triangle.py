# this is file that can return you a right angle triangle

class Right_Angled_Triangle:
    "use this class to draw a Right Angel Triangle"

    def __init__(self, row_num):
        self.row_number = row_num
        self.draw(row_num)

    def draw(self, row_num):
        if row_num != float(row_num) or row_num != str(row_num) or row_num != list(row_num):   
            for i in range(1, row_num + 1):
                print("*" * i)
                self.stars_number = i
                while(self.stars_number == row_num):
                    self.stars_number += i
        else:
            raise TypeError("row_num must be int NOT other types")

    def get_star_num(self):
        "this method can count the number of stars in your shape"
        "you can use this functin to calculate number of stars : f(x) = ((x**2) / 2) + (x / 2) "
        row_num = self.row_number
        result = ((row_num ** 2) / 2) + (row_num / 2)
        print(f"stars number ==> {int(result)}")


