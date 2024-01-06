#before
from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass
    
class DotMatrixPrinter(Printer):
    def print(self, document):
        print('Print from DotMatrixPrinter')
    
    def scan(self, document):
       pass
   
class InkjetPrinter(Printer):
    def print(self, document):
        print('Print from InkjetPrinter')
    
    def scan(self, document):
       print('Scan')  
    
           
#after

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass
    
class DotMatrixPrinter(Printer):
    def print(self, document):
        print('Print from DotMatrixPrinter')
  
class InkjetPrinter(Printer, Scanner):
    def print(self, document):
        print('Print from InkjetPrinter')
    
    def scan(self, document):
       print('Scan')  


dotMatrixPrinter = DotMatrixPrinter()
dotMatrixPrinter.print('document')

inkjetPrinter = InkjetPrinter()
inkjetPrinter.print('document')
inkjetPrinter.scan('document')