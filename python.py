class Library:
    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()      
    

    # kitapları listeleme
    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for line in lines:
            record = line.split(',')
            book_name, author, category, release_date, number_of_pages = record
            print(f"Kitap Adı: {book_name}, Yazar: {author}")

    # kitap ekleme
    def add_book(self):
        book_name = input("Kitab adını girin:  ")
        author = input("Yazar adını girin:  ")
        category = input("Kitap kategorisini girin: ")
        release_date = input("Yayınlanma tarihini girin:  ")
        number_of_pages = input("Kitap sayfa sayısını girin:  ")

        record = f"{book_name},{author},{category},{release_date},{number_of_pages}\n"
        self.file.write(record)
        print(f"'{book_name}' kitabı eklendiii")

    # kitap silme

    def remove_book(self):
        remove_book_name = input("Silinecek olan kitabın adını girin: ")
        lines = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        for line in lines:
            if remove_book_name not in line:
                self.file.write(line)

        print(f"'{remove_book_name}' kitabı listeden silindiii")


lib = Library()

while True:
    print("-----------------------")
    print("------- M E N U -------")
    print("-----------------------")
    print("1) Kitapları listeleme")
    print("2) Kitap ekleme")
    print("3) Kitap silme")
    print("q) Çıkış yapma")
    option = input("Lütfen seçiminizi girin: ")


    if option == '1':
        lib.list_books()
    elif option == '2':
        lib.add_book()
    elif option == '3':
        lib.remove_book()
    elif option.lower() == 'q':
        break
    else:
        print("Lütfen belirtilen şeçenekleri kullanınız.")