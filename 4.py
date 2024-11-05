class Mamal:
    className = "Mamal"
class Dog(Mamal):
    species = 'canine'
    sounds = 'meow'
class Cat(Mamal):
    species = 'feline'
    sounds = 'meow'
dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat. className}, but they say {cat. sounds}")