from abc import ABC, abstractmethod


class Country(ABC):
    @abstractmethod
    def display_capital(self):
        pass
    
    @abstractmethod
    def display_language(self):
        pass
    
    @abstractmethod
    def display_type(self):
        pass

class India(Country):
    def display_capital(self):
        print("Capital: New Delhi")
    
    def display_language(self):
        print("Language: Hindi, English")
    
    def display_type(self):
        print("Type of Country: Republic")

class Japan(Country):
    def display_capital(self):
        print("Capital: Tokyo")
    
    def display_language(self):
        print("Language: Japanese")
    
    def display_type(self):
        print("Type of Country: Constitutional Monarchy")


india = India()
japan = Japan()


def display_country_info(country: Country):
    country.display_capital()
    country.display_language()
    country.display_type()


print("India Information:")
display_country_info(india)

print("\nJapan Information:")
display_country_info(japan)
