#before

class Document:
    def __init__(self, download_service):
        self.download_service = download_service
    
    def download(self):
        self.download_service.download()

class PdfDownload:
    def download(self):
        print('download as pdf')

class DocDownload:
    def download(self):
        print('download as doc')        

document = Document(PdfDownload())
document.download()


#after

from abc import ABC, abstractmethod

class DownloadService(ABC):
    @abstractmethod
    def download(self):
        pass

class PdfDownload(DownloadService):
    def download(self):
        print('download as pdf')

class DocDownload(DownloadService):
    def download(self):
        print('download as doc')  
        
class Document:
    def __init__(self, download_service):
        self.download_service = download_service
    
    def download(self):
        self.download_service.download()              

document = Document(DocDownload())
document.download()