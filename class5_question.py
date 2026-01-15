class data():
    def __init__(self,name,marks_en,marks_hi,marks_sc):
        self.name=name
        self.marks_en=marks_en
        self.marks_hi=marks_hi
        self.marks_sc=marks_sc
        print(name,marks_en,marks_hi,marks_sc)
    def average(self):
        print("the average of marks are")
        avg=(self.marks_en+ self.marks_hi + self.marks_sc)/3
        #print(avg)
        return avg

s1 = data("ayush",98,99,99)
print(s1.average())

