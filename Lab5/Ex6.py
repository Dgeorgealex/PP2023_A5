class LibraryItem:
    def __init__(self, item_id, title, available = 1):
        self.item_id = item_id
        self.title = title
        self.available = available

    def get_info(self):
        info = f"{self.__class__.__name__} - id: {self.item_id} - title: {self.title} - available: {self.available}"
        return info

    def check_out(self):
        if self.available == 0:
            print("Item is not available")
        else:
            print("Item successfully checked out")
            self.available = 0

    def bring_back(self):
        if self.available == 1:
            print("Item was not checked out")
        else:
            print("Item successfully returned")
            self.available = 1

    def __str__(self):
        pass


class Book(LibraryItem):
    def __init__(self, item_id, title, num_pages=0, available=1):
        super().__init__(item_id, title, available)
        self.num_pages = num_pages

    def __str__(self):
        info = self.get_info() + f" - num_pages: {self.num_pages}"
        return info


class Magazine(LibraryItem):
    def __init__(self, item_id, title, edition=1, available=1):
        super().__init__(item_id, title, available)
        self.edition = edition

    def __str__(self):
        info = self.get_info() + f" - edition: {self.edition}"
        return info


class DVD(LibraryItem):
    def __init__(self, item_id, title, duration = 0, available=1):
        super().__init__(item_id, title, available)
        self.duration = duration

    def __str__(self):
        info = self.get_info() + f" - duration: {self.duration}"
        return info


if __name__ == "__main__":
    dvd = DVD(1, 'a', 60)
    print(dvd)

    dvd.check_out()
    dvd.check_out()
    dvd.bring_back()
    dvd.bring_back()