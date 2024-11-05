class Ivan:
    __slots__ = ['name']
    def __init__ (self, name) :
        if name == "Иван":
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Иван"
pers1 = Ivan('Алексей')
pers2 = Ivan('Иван')
print (pers1. name)
print(pers2. name)