class vehicle:
    def __init__(self,speed,model):
        self.speed=speed
        self.model=model


ob=vehicle(250,"BMW X2")
ob2=vehicle(100,"Audi m1")
ob3=vehicle(150,"Benz m2")
ob4=vehicle(300,"Audi m10")
print("Speed:",ob4.speed)
print("Model:",ob4.model)