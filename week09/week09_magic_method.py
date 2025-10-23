class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level


    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    def __str__(self): # magic method (operator overloading)
        # return "%s(%s)" % (self.name, self.level)
        # return "{}({})".format(self.name, self.level)
        return f"{self.name}({self.level})"

p1 = Pokemon('Pikachu', 5)
p2 = Pokemon('Squirtle', 3)

print(p1) # C++ -> cout << p1;
print(p2)