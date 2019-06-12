

class Man:

    def __init__(self, name , age):
        self.pname = name
        self.pAge = age


object1 = Man('Riyadh', 26)
object2 = Man('Putin', 70)

print(object1.pname+" is "+ str(object1.pAge) + " year(s) old")
print(object2.pname+" is "+ str(object2.pAge) + " year(s) old")