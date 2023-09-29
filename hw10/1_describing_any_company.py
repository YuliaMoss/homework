"""1- Create a class describing any company. For example, Toshiba or Apple"""


class DescribingCompany:
    """a class describing any company"""

    def __init__(self, name: str, industry: str, address: str, founded_year: int, CEO: str):
        """common info"""
        self.name = name
        self.industry = industry
        self.address = address
        self.founded_year = founded_year
        self.CEO = CEO

    def show_name(self):
        """print the company name"""
        print(self.name)

    def show_address(self):
        """print the company address"""
        print(self.address)

    def __str__(self):
        """return string with common info"""
        return (f"Company {self.name} is a {self.industry} company headquartered in {self.address}. "
                f"It was founded in {self.founded_year} and is led by CEO {self.CEO}.")

    def __repr__(self):
        """Return a string representation of the object."""
        return f'DescribingCompany ({self.name} {self.address} {self.founded_year})'

    @staticmethod
    def show_statement():
        """static method with some statement"""
        print(f"That's some facts")


if __name__ == '__main__':
    """Creating an instance of the Company class"""
    apple = DescribingCompany("Apple Inc.", "Technology", "Cupertino, California",
                              1976, "Tim Cook")

    """print the company name"""
    apple.show_name()

    """print the company address"""
    apple.show_address()

    """return string with common info"""
    print(str(apple))

    """ Printing the representation of the 'apple' instance"""
    print(repr(apple))

    """Calling the 'show_statement' static method"""
    DescribingCompany.show_statement()
