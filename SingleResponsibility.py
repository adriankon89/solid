#before
class Document:
    def __init__(self, content= ''):
        self.content = content
        
    def print(self):
        print(self.content)    
        
        
document = Document('document content')
document.print()   


#after

class Document:
    def __init__(self, content= ''):
        self.content = content
    
    def getContent(self):
        return self.content    
        
class Print:
    def print(content):
        print(content)    
                            
document = Document('solid first rule')   
print = Print.print(document.getContent())                        