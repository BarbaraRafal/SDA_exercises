# # exercise 1 Powinna przyjmować imie, wiek oraz płeć
# # Wszystkie wlaściwośći powinny być prywatne _
# # Klasa powinna posiadać metody zwracające te dane
# #
# # class Human:
# #     def __init__(self, name, age, sex):
# #         self._name = name
# #         self._age = age
# #         self._sex = sex
# #
# #     def get_name(self):
# #         return self._name
# #
# #     def get_age(self):
# #         return self._age
# #
# #     def get_sex(self):
# #         return self._sex

# # stranger = Human("John", 25, "Male")
# # stranger2 = Human('Ala', 25,'Female')
# #
# # print(f'Name: {stranger2.get_name()}\nSex: {stranger2.get_sex()}\nAge: {stranger2.get_age()}')
# # print(f'Name: {stranger.get_name()}\nSex: {stranger.get_sex()}\nAge: {stranger.get_age()}')
#
# # exercise 2 Koszyk powinien przetrzymywać produkty, lista ->słownik[name: string, price: float]
# # Na starcie koszyk jest pusty
# # metoda add_product, powinna dodać produkt do koszyka
# # metoda get_all, powinna zwrócić wszystkie produkty z koszyka
# # można wykorzystać @property
# # Metoda get_sum powinna zwrócić wartość produktów w koszyku/
#
# # exercise 3 Podczas tworzenia powinna być pusta -> Lista -> {name, expired: 0-10} -> 1-3 to expired
# # Metoda 'add_product' powinna dodać produkt do lodówki
# # Metoda get_all powinna zwrócić wszystie produkty
# ####################
# # Metoda get_all(fresh=false) dla true powinna zwrócic produty tylko świeże
#
class Refrigerator:
    def __init__(self):
        self._products = []

    def add_product(self, name, expired):
        self._products.append({'name': name, 'expired': expired})

    def get_all(self, fresh=False):
            fresh_product = []
            if fresh:
                for product in self._products:
                    if product['expired'] > 3:
                        fresh_product.append(product)
                return fresh_product
            else:
                return self._products


my_refrigerator = Refrigerator()
my_refrigerator.add_product("apple", 5)
my_refrigerator.add_product("banana", 2)
my_refrigerator.add_product("milk", 10)
my_refrigerator.add_product("butter", 8)
print(my_refrigerator.get_all(True))
# # #
# # ### exercise 4
# #
# #
# # from typing import List
# # class Browser:
# #     def __init__(self):
# #         self._history = []
# #
# #     def visit(self, address: str) -> List[str]:
# #         self._history.append(address)
# #
# #     def go_back(self) -> None:
# #         if len(self._history):
# #             self._history.pop()
# #         else:
# #             return []
# #
# #     def history(self) -> List[str]:
# #         return self._history
# #
# #     def current(self) -> str:
# #         if len(self._history):
# #             return self._history[-1]
# #
# #
# # my_browser = Browser()
# # my_browser.visit('http://www.wp.pl')
# # my_browser.visit('http://www.wp.pl/1')
# # my_browser.visit('http://www.wp.pl/2')
# # my_browser.visit('http://www.wp.pl/3')
# # my_browser.visit('http://www.wp.pl/5')
# # my_browser.visit('http://www.wp.pl/6')
# # my_browser.visit('http://www.wp.pl/7')
# # print(my_browser.history())
# # print(my_browser.go_back())
# # print(my_browser.current())
#
#
# # # Pobieramy userów z pliku users.txt
# # # Metoda powinna zwrócić List -> Dictionary(id, username, role)
# #
# # class UserProvider:
# #     def get_users(self):
# #         all_users = []
# #
# #         with open("users.txt") as file:
# #             lines = file.readlines()
# #
# #         for line in lines:
# #             splited_lines = line.split('|')
# #             all_users.append({'id': splited_lines[0], 'username': splited_lines[1], 'role': splited_lines[2]})
# #         return all_users
# #
# # my_users = UserProvider()
# # # print(my_users.get_users())
# # #
# # #
# # # ### edited
# # #
# # from typing import List
# #
# # class User:
# #     def __init__(self, user_id, username, role):
# #         self.user_id = user_id
# #         self.username = username
# #         self.role = role
# #
# #
# # class UserProvider:
# #     def get_users(self) ->List[User]:
# #         all_users = []
# #
# #         with open("users.txt") as file:
# #             lines = file.readlines()
# #
# #         for line in lines:
# #             user_id, username, role  = line.strip().split('|')
# #             all_users.append(User(user_id, username, role))
# #         return all_users
# #
# # my_users = UserProvider()
# # print(my_users.get_users())
# #
# #
# # ####Zaimplementuj metodę get_users_by_role aby  zwracała listę użytkowników po danej roli role orazssciezka z zewnatrz do pliku z danymi
# # from typing import List
# #
# # class User:
# #     def __init__(self, user_id, name, role):
# #         self._name = name
# #         self._role = role
# #         self._user_id = user_id
# #
# #     @property
# #     def name(self):
# #         return self._name
# #
# #     @property
# #     def user_id(self):
# #         return self._user_id
# #
# #     @property
# #     def role(self):
# #         return self._role
# #
# # class UserProvider:
# #     def __init__(self, db_path):
# #         self.db_path = db_path
# #
# #     def get_users(self) -> List[User]:
# #         return self._fetch_from_file()
# #
# #     def get_users_by_role(self, role) -> List[User]:
# #         users_by_role = []
# #         for user in self._fetch_from_file():
# #             if user.role == role:
# #                 users_by_role.append(user)
# #         return users_by_role
#
# #     def _fetch_from_file(self) -> List[User]:
# #         users = []
# #         with open(self.db_path) as read_handler:
# #             for line in read_handler:
# #                 user_id, name, role = line.strip().split('|')
# #                 users.append(User(user_id, name, role))
# #         return users
# #
# # provider = UserProvider('other_db.txt')
# # print(provider.get_users())
# # print(provider.get_users_by_role('Admin')[0].name)
# #
# #
# # ### z dziedziczeniem
#
# from typing import List
# #
# # class Product:
# #     def __init__(self, name: str, price: float):
# #         self._name = name
# #         self._price = price
# #
# #     @property
# #     def name(self) -> str:
# #         return self._name
# #
# #     @property
# #     def price(self) -> float:
# #         return self._price
# #
# # class DiscountProduct(Product):
# #      def __init__(self, name, price, discount: float):
# #         super().__init__(name, price)
# #         self._discount = discount
# #
# #      @property
# #      def price(self) -> float:
# #          return self._price - (self._price*self._discount)
# #
# # class Register:
# #     def __init__(self):
# #         self._products = []
# #
# #     def add_product(self, product: Product):
# #         self._products.append(product)
# #
# #     def sum(self) -> float:
# #         result = 0.0
# #         for product in self._products:
# #             result += product.price
# #         return result
# #
# # my_register = Register()
# # my_register.add_product(DiscountProduct('usb', 500.00, 0.2))
# # my_register.add_product(DiscountProduct('tv', 2000.00, 0.8))
# # my_register.add_product(DiscountProduct('dvd', 1000.00, 0.15))
# print(my_register.sum())
#
#
# # homework
#
# def censor(text, black_list=()):
#     censored_text = []
#     censored_word = '*****'
#
#     for words in text.split():
#         if words in black_list:
#             censored_text.append(censored_word)
#         else:
#             censored_text.append(words)
#     return ' '.join(censored_text)
#
# print(censor('You are a damn fool',('damn','fool')))
#
# ### odorny na duze znaki w przekleństwach
# # def censor(text, black_list=()):
# #     censored_text = []
# #     censored_word = '*****'
# #
# #     for words in text.split():
# #         if words.lower() in black_list:
# #             censored_text.append(censored_word)
# #         else:
# #             censored_text.append(words)
# #     return ' '.join(censored_text)
# #
# # print(censor('You are a daMn FOOL',('damn','fool')))
#
#
# ##### odporny na znaki specjalne w przerkleństwach
# def censor(text, black_list=()):
#     censored_text = []
#     censored_word = '*****'
#     banned_signs = ['@','*']
#     filtered_text = ''
#
#     for sign in text:
#         if sign not in banned_signs:
#             filtered_text += sign
#
#     for words in filtered_text.split():
#         if words.lower() in black_list:
#             censored_text.append(censored_word)
#         else:
#             censored_text.append(words)
#
#     return ' '.join(censored_text)
#
# print(censor('You are a d@aMn FOO*L',('damn','fool')))
#
# ### wariant 4i 3 ceznora
#
# import requests
#
# def censor(text,swear_db):
#     response = requests.get(swear_db)
#     print(response.status_code) #opcjonalne, żeby zobaczyć czy udało się pobrac zawartosc ze strony
#     profanities = response.text
#     censored_text = []
#     censored_word = '*****'
#     banned_signs = ['@','*']
#     filtered_text = ''
#
#     for sign in text:
#         if sign not in banned_signs:
#             filtered_text += sign
#
#     for words in filtered_text.split():
#         if words.lower() in profanities:
#             censored_text.append(censored_word)
#         else:
#             censored_text.append(words)
#
#     return ' '.join(censored_text)
#
# print(censor('You a*re a d@amn f**ool','http://www.bannedwordlist.com/lists/swearWords.txt'))
#
# ## waiant 3
# # def censor(text, profanities=('damn', 'fool')):
# #     censored_text = []
# #     censored_word = '*****'
# #     banned_signs = ['@','*']
# #     filtered_text = ''
# #
# #     for sign in text:
# #         if sign not in banned_signs:
# #             filtered_text += sign
# #
# #     for words in filtered_text.split():
# #         if words.lower() in profanities:
# #             censored_text.append(censored_word)
# #         else:
# #             censored_text.append(words)
# #
# #     return ' '.join(censored_text)
# #
# # print(censor('You a*re a d@amn f**ool'))
# # print(censor(('You a*re a d@amn f**ool'),('stupid', 'ass')))
#
# #
# # class User:
# #     def __init__(self, first_name, last_name, email, active):
# #         self._first_name = first_name
# #         self._last_name = last_name
# #         self._email = email
# #         self._active = active
# #
# #     @property
# #     def email(self):
# #         return self._email
# #
# #
# # class NewsletterSystem:
# #     def __init__(self):
# #         self._all_users = []
# #
# #     def add_user(self, user:User):
# #         self._all_users.append(user)
# #
# #
# #     def print_users(self):
# #         return self._all_users
# #
# #     # def remove_user(self, user:user):
# #     #     pass
# #
# #     def send(self):
# #         for user in self._all_users:
# #             return user.email
# #
# #
# #
# #
# # newsletter = NewsletterSystem()
# # newsletter.add_user('abc@op.pl','Tom','Sparkle',True)
# # newsletter.add_user('def@op.pl','Matt','Fischer',True)
# # newsletter.add_user('ghi@op.pl','John','Water',False)
# # newsletter.add_user('jkl@op.pl','James','Bond',True)
# #
# # print(newsletter.print_users())
# #
# # print(newsletter.send())
#
# #
# # from typing import Dict
# # class Item:
# #     def __init__(self, id, name,price:float):
# #         self._id = id
# #         self._name = name
# #         self._price = price
# #
# #     def __repr__(self):
# #         return self._name
# #
# #     @property
# #     def id(self):
# #         return self._id
# #
# #     @property
# #     def name(self):
# #         return self._name
# #
# #     @property
# #     def price(self):
# #         return self._price
# #
# # class RentalSystem:
# #     def __init__(self):
# #         self._rented_items = {}
# #
# #     def rent(self, item: Item):
# #         self._rented_items[item.id] = item
# #
# #     def give_back(self, item_id):
# #         del self._rented_items[item_id]
# #
# #     def show(self) -> Dict[str, Item]:
# #         return self._rented_items
# #
# #     def sum(self) -> float:
# #         result = 0
# #         for key in self._rented_items:
# #             result += self._rented_items.get(key).price
# #             return result
# #
# # my_system = RentalSystem()
# # my_system.rent(Item(1, 'Matrix 1', 2.5))
# # my_system.rent(Item(2, 'Matrix 2', 3.5))
# # my_system.rent(Item(3, 'Matrix 3', 5.5))
# #
# # print(my_system.show())
# # print(my_system.sum())
