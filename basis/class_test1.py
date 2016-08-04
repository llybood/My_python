#-*- coding: utf-8 -*-
__author__ = 'coolfire'

class Animal(object):
    def __init__(self):
        pass
    def Eat(self):
        pass

class Chicken(Animal):
    def __init__(self):
        super(Chicken,self).__init__() #使用super函数初始化超类的构造方法
    def Eat(self):
        print "the chicken has been eat"

class Dog(Animal):
    def __init__(self):
        super(Dog,self).__init__()
    def Eat(self):
        print "the dog has been eat"

class Person(object):
    def __init__(self,name):
        self.name = name
    def Feed(self,ped):
        ped.Eat()

class mytest():
    def __init__(self,name):
        print "hello" + " " + name




if __name__ == "__main__":
    #Kobe = Person("hello")
    #pedChicken = Chicken()
    #pedDog = Dog()
    #Kobe.Feed(pedChicken)
    #Kobe.Feed(pedDog)
    test = mytest()

