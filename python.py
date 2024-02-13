class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")
        
    def __del__(self):
        self.file.close()      
