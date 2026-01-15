print("Before class")

class A:
    print("Class body")

    def __init__(self):
        print("Constructor")

print("Before object")
obj = A()
print("After object")
