class data:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("Constructor")

    def greet(self):
        print("welcome",self.name)

#functions inside a class are methods
s1 = data("shivam",99)
print(s1.marks)
s1.greet()
print(s1.name)