class Sparrow:
    sp="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age


Cherry=Sparrow("Cherry",5)
tom=Sparrow("Tom",4)
print("Cherry and tom both are",tom.sp)
print("{} is {} year old".format(Cherry.name,Cherry.age))
print("{} is {} year old".format(tom.name,tom.age))