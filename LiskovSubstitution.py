#before

class DotMatrixPrinter:
    def __init__(self, content = ''):
        self.content = content
        
    def print(self):
        print('Print from DotMatrixPrinter')
        
        
class InkjetPrinter(DotMatrixPrinter):
    def __init__(self, content = ''):
        self.content = content
    
    def print(self, printInColor = True):
        print('Print from InkjetPrinter')   
       
content = 'Content to print'
dotMatrixPrinter = DotMatrixPrinter(content);   
dotMatrixPrinter.print()  

inkjetPrinter = InkjetPrinter(content);   
inkjetPrinter.print()   

#after


from abc import ABC, abstractmethod
class Printer(ABC):
    @abstractmethod
    def print(self):
        pass  
    
    
class DotMatrixPrinter(Printer):
    def __init__(self, content = ''):
        self.content = content
        
    def print(self):
        print('Print from DotMatrixPrinter')     


class InkjetPrinter(Printer):
    def __init__(self, printInColor = True, content = ''):
        self.content = content
        self.printInColor = printInColor
    
    def print(self):
        print('Print from InkjetPrinter')                            
        

content = 'Content to print'
dotMatrixPrinter = DotMatrixPrinter(content);   
dotMatrixPrinter.print()  

inkjetPrinter = InkjetPrinter(True, content);   
inkjetPrinter.print()           