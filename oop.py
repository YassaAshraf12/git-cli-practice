class Car:
    price=200000

    def __init__(self,model,year,color ,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
        Car.price+=1000
    def drive(self):
        print("u drive the car")
    def dtop(self):
        print(f"u stop the car{self.model}")
    def describe(self):
        print(f"{self.model}{self.year}{self.color}")  



class motor(Car):# inherite from car
    pass
