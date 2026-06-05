#17-m
class Hospital:
    def __init__(self, name, paitents):
        self.name = name
        self.__paitents = paitents

    def get_paitents(self):
        return self.__paitents

    def set_paitents(self, new_paitents):
        if new_paitents >= self.__paitents:
            self.__paitents = new_paitents
        else:
            print("Bemorlar soni kamaymasligi kerak")

h1 = Hospital("Shifo", 1200)

print(h1.name)
print(h1.get_paitents())

h1.set_paitents(1200)
print(h1.get_paitents())

h1.set_paitents(6700)
print(h1.get_paitents())
