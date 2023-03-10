class Animal:
    def __init__(self, name, colorr, age) :
        self.name=name
        self.colorr=colorr
        self.age=age

    def getname(self):
        return self.name

    def display(self):
        item=' '                                                    
        item=item+f'\n name: {self.name}'        
        item=item+f'\n colour: {self.colorr}'
        item=item+f'\n name: {self.age}'
        return item

    def makesound(self):
        print('they have sound')   


class Dog(Animal):
    def eatingbone(self):
        print('!!!!!!!!bone!!!!!!!!!')  
    
    def makesound(self):
        print('hop hop')   



class Cat(Animal):
    def chasingMouse(self):
        print('chasing...........') 
    #Over write
    def makesound(self):
        print('mewooooooo')   

                  