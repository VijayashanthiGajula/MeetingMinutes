from django.test import TestCase

# Create your tests here.
class Parrot:

    def fly(self):
        print("Parrot can fly")
    
    def swim(self):
        print("Parrot can't swim")
blu = Parrot()
blu.fly()