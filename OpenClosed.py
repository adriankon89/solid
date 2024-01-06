#before

class Printer:
    def __init__(self, type = '', content = ''):
        self.type = type
        self.content = content
    
    def print(self):
        if self.type == 'document':
            print('print as document')
        if self.type == 'certificate':
            print('print as certificate')    
        
  
documentPrinter = Printer('document', 'content')
documentPrinter.print()

certificatePrinter = Printer('certificate', 'content')
certificatePrinter.print()

#after

from abc import ABC, abstractmethod
class Printer(ABC):
    def __init__(self):
      pass
   
    @abstractmethod
    def print(self):
        pass

class Document(Printer):
    def __init__(self, content= ''):
        self.content = content
        
    def print(self):
        print('print from Document class')

class Certificate(Printer):  
    def __init__(self, content= ''):
        self.content = content
        
    def print(self):
        print('print from Certificate class')
        


documentPrinter = Document('content')
documentPrinter.print()

certificatePrinter = Certificate('content')
certificatePrinter.print()        
    
             