#creating a class.

class PartyAnimal: #defining the class in name in camelcase

    def __init__(self) : #calling the builting function "constructer" to initialize the variable x
        self.x = 0 #self refers to the newly created object
        print('I am constructed', self.x)
    def party(self) : # defining a function name party with self parameter which is again refering to object
        self.x = self.x + 1 #adding 1 to variable x for that specific object
        print("So far", self.x)

    def __del__(self): #calling the destructor to destroy the variable x
        print('I am destructed', self.x)
an = PartyAnimal() #creating the object and saving it in a variable name "an"

an.party() #with an named objected created above calling function inside the class. which will print the value of x.
an.party()
an.party()
