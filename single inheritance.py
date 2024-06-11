#single inheritance

class parent:
    def display(self):
        print("parent")
class child(parent):
    def show(self):
        print("child")
obj=child()
obj.show()
obj.display()


#multi level inheritance

class grandparent:
    def display(self):
        print("grandparent")
class parent(grandparent):
    def pdisplay(self):
        print("parent")
class child(parent):
    def cdisplay(self):
        print("child")
c1=child()
c1=display()
c1=pdisplay()
c1=cdisplay()
    
#multiple inheritance

class father:
    def display(self):
        print("father")
class mother:
    def mdisplay(self):
        print("mother")
class child(father,mother):
    def cdisplay(self):
        print("child")
c1=child()
c1.display()
c1.mdisplay()
c1.cdisplay()


# hybird/hierarchical inheritance

class parent:
    def pdisplay(self):
        print("parent")
class child1  (parent):
    def cdisplay(self):
        print("child 1")
class child2(parent):
    def mdisplay(self):
        print("child 2")
c1=child1()
c1.pdisplay()
c1.cdisplay()

c2=child2()
c2.pdisplay()
c2.mdisplay()

