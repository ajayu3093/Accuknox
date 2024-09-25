class Rectangle:
    def __init__(self):
        self.length = int(input("Enter the length of the rectangle: "))
        self.width = int(input("Enter the width of the rectangle: "))
    
    def __iter__(self):
        
       return iter([{'length': self.length}, {'width': self.width}])
        
result = Rectangle()
for attribute in result:
    print(attribute)
