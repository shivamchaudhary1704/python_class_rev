class cars:
    new_student="yay" #its a class attribute it wont have any affect untill the new_satudent dont have any value passed
    def __init__ (self,name):
        print("this is the constructor to work")
        self.new_student=name # generaly the new_student and name should be of same var name its a good practice
#object attiribute >> class attribute (precedence)
s1=cars("bmw")
print(s1.new_student)