class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()      
    
    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            record = line.split(',')
            book_name, author, category, release_date, num_pages = record
            print(f"Kitap Adı: {book_name}, Yazar: {author}")

    def add_book(self):
        book_name = input("Kitab adını girin:  ")
        author = input("Yazar adını girin:  ")
        category = input("Kitap kategorisini girin: ")
        release_date = input("Yayınlanma tarihini girin:  ")
        num_pages = input("Kitap sayfa sayısını girin:  ")

        record = f"{book_name},{author},{category},{release_date},{num_pages}\n"
        self.file.write(record)
        print(f"'{book_name}' kitabı eklendiii")

    def remove_book(self):
        title_to_remove = input("Silinecek olan kitabın adını girin: ")
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for line in lines:
            if title_to_remove not in line:
                self.file.write(line)

        print(f"'{title_to_remove}' kitabı listeden silindiii")


lib = Library()