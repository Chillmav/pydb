from pydb.storage.page import PAGE_SIZE, Page
DATABASE_PATH = "C:/python/pydb/data/database.db"
import os

class Pager:
    
    def __init__(self, path=DATABASE_PATH):
        
        self.page_count = 0
        self.file_size = 0
        self.path = path
        self.page_size = PAGE_SIZE
        self.check_size()
        
    def check_size(self):
        
        try:
            self.file_size = os.path.getsize(self.path)
        except:
            raise FileNotFoundError("File doesn't exist")
        
        if self.file_size % self.page_size:
            raise ValueError("File ends with an incomplete page")
        self.page_count = self.file_size // self.page_size
    
    def calc_offset(self, page_num):
        
        if page_num >= self.page_count or page_num < 0:
                    raise IndexError("Page doesn't exist")
                
        return page_num * self.page_size
        
    def read_page(self, page_num):
        
        offset = self.calc_offset(page_num)
        
        with open(self.path, "rb") as f:
            f.seek(offset)
            data = f.read(self.page_size)
            page = Page(page_num, data)
            
        return page
    
    def write_page(self, page: Page):
        
        offset = self.calc_offset(page.page_num)
        
        with open(self.path, "r+b") as f:
            
            f.seek(offset)
            f.write(page.data)
        
    def alloc_page(self):
        
        data = bytearray(self.page_size)
        offset = self.page_count * self.page_size
        
        with open(self.path, "r+b") as f:
            f.seek(offset)
            f.write(data)
            
        self.check_size()
        return Page(self.page_count-1, data)
        
        