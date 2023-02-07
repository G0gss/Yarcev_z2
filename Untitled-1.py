class Car:

    def __init__ (self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
        
    def ZapuskAvto(self):
        print ("Автомобиль заведен")
        
    def OffAvto(self):
        print ("Автомобиль отключен")
        
    def age_of_car (self, age):
        self. year = age
        
    def tip_of_car(self, tip):
    # тип автомобиля
        self.type = tip
    def cvet_of_car(self, cvet):
    
        self, color = cvet
Сaг1 = Car ("Белый", "Марседее", 501)
print (Сaг1)