class Movie:
    def accept_movie(self):
        self.title = input("Enter Movie Title: ")
        self.genre = input("Enter Genre: ")

    def display_movie(self):
        print(f"Movie Title: {self.title}")
        print(f"Genre: {self.genre}")


class Rental:
    def accept_rental(self, mv):
        self.custname = input("Enter Customer Name: ")
        self.mo = mv
        self.days = int(input("Enter Rental Days: "))

    def display_rental(self):
        print("\n--- Rental Details ---")
        print(f"Customer: {self.custname}")
        self.mo.display_movie()
        print(f"Days Rented: {self.days}")

if __name__=="__main__":
    m = Movie()
    m.accept_movie()
    r = Rental()
    r.accept_rental(m)
    r.display_rental()