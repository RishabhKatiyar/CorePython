class Program:
    @staticmethod
    def staticMethod():
        print("In Static Method")
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ == "__main__":
    Program.staticMethod()

    ob = Program(1,5)
    print(ob.a)
    print(ob.b)