PAGE_SIZE = 4096

class Page:
    
    def __init__(self, page_num: int, data):
        if page_num >= 0:
            self.page_num = page_num
        else:
            raise ValueError("Page num is less than 0")
        
        if len(data) != PAGE_SIZE:
            raise ValueError("Length of data is not equal to the page size")
        else:
            if isinstance(data, bytearray):
                self.data = data
            elif isinstance(data, bytes):
                self.data = bytearray(data)
                
                