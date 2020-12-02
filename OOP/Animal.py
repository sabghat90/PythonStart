class Calc:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        print(self.a + self.b)


s = Calc(1, 3)
s.sum()

# class Animal:
#     def dog(self):
#         print("Gho Gho")
#
#     def cat(self):
#         print("Mew Mew")
#
#
# dog = Animal()
# cat = Animal()
#
# Animal.cat(cat)
# Animal.dog(dog)