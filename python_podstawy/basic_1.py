# # #1 PIERWSZY PROGRAM Napisz kod, który po uruchomieniu wyświetli twoje imię oraz nazwisko w dowolnym terminalu.
# # print("Barbara Rafał")
# #
# # #2 TYPY DANYCH Napisz kod, który po uruchomieniu wyświetli typ zmiennej my_variable = "some", "random", 1, 2
# # my_variable = "some","random",1,2
# # print(type(my_variable))
# #
# # #3 ZMIENNE I OPERATORY
# # # WARIANT 1 Napisz kod, który po uruchomieniu zwróci twoje imię, nazwisko oraz wiek, gdzie każda z wartości będzie
# # #przypisana do osobnej zmiennej.
# # name = "Barbara"
# # surname = "Rafał"
# # age = 34
# # print(f'{name} {surname} {age}')
# #
# # # WARIANT 2 Napisz kod, który po uruchomieniu zwróci twoje imię, nazwisko oraz wiek, gdzie każda z wartości będzie
# # # przypisana do osobnej zmiennej, zwrócona wartość powinna być tuplem.
# # name = "Barbara"
# # surname = "Rafał"
# # age = 34
# # me = (name,surname,age)
# # print(me)
#
# # #Napisz kod, który przyjmie imię od użytkownika oraz zwróci True gdy podaną wartością będzie John, w
# # #innym przypadku kod powinien zwrócić False. Wykorzystaj funkcję input.
# # name = input("Your name:")
# # if name == "Barbara":
# #     print(True)
# # else:
# #     print(False)
# #
# # #Napisz kod, który przyjmie imię od użytkownika oraz zwróci True gdy podaną wartością będzie John,
# # #Tom lub Mark. Wykorzystaj operator przynależności (in, not in).
# # NAMES= ['John','Mark','Tom']
# # your_name = input("Your name:")
# # if your_name in NAMES:
# #     print(True)
# # else: # lub if your_name is not in names
# #     print(False)
# #
# # # rozwinięcie poprzedniego zadania
# # NAMES= ['John','Mark','Tom']
# # your_name = input("Your name:")
# # if your_name in NAMES:
# #     print(your_name,  "is in our Database")
# # if your_name not in NAMES:
# # print(your_name," is not supported, contact with", NAMES) # nie wiem jak zmienic wyswietlanie elementow listy a nie calej listy :)
# #
# # # 4 FORMATOWANIE TEKSTU
# # # WARIANT 1 Napisz kod, który przyjmie numer telefonu od użytkownika oraz zwróci go wraz z numerem
# # # kierunkowym kraju.(Poniżej rozwiązanie trenera)
# # telephone_number = input('Enter phone number: ')
# # country_prefix = input('Enter country prefix value: ')
# # print(f'+{country_prefix} {telephone_number}')
# #
# # #moje rozwiązanie
# # phone_number = input("Your phone number:")
# # print("+48", phone_number)
# #
# #
# # # WARIANT2 Napisz kod, który przyjmie numer telefonu oraz kod kierunkowy kraju od użytkownika oraz poprawnie zwróci
# # # sformatowaną wartość.
# # phone_number = input("Your phone number:")
# # prefix = input( "prefix:")
# # print("+",prefix, phone_number) #
# #
# # #WARIANT 3 Napisz kod, który przyjmie numer telefonu oraz kod kierunkowy kraju od użytkownika oraz poprawnie zwróci
# # # sformatowaną wartość oraz sprawdzi czy kod kierunkowy jest poprawny.
# # PREFIXES = {48, 12, 81, 55}
# # phone_number = input('Write your phone number: ')
# # prefix = input('write prefix: ')
# #
# # if int(prefix) in PREFIXES:
# #     print(f' + {prefix} {phone_number}')
# # else:
# #     print(f' Prefix {prefix} is not supported')
# #
# # # Napisz kod, który przyjmie numer telefonu oraz kod kierunkowy kraju od użytkownika oraz:
# # # sprawdzi czy prefix jest poprawny, jesli nie wyswieli ze prefix niepoprawny
# # # sprawdzi czy nr tel zawiera 9 cyfr, jesli tak wyswietli numer z prefixem, jesli nie wyswietli ze format niepoprawny
#
# # PREFIXES = {48, 12, 81, 55}
# # phone_number = input('Write your phone number: ')
# # prefix = input('write prefix: ')
# #
# # if int(prefix) in PREFIXES and prefix.isnumeric():
# #     if phone_number.isnumeric() and len(phone_number) == 9:
# #         print(f' + {prefix} {phone_number}')
# #     else:
# #         print(f'Invalid phone number format')
# # else:
# #     print(f' Prefix {prefix} is not supported')
#
# # WARIANT 3 Napisz kod, który przyjmie numer telefonu oraz kod kierunkowy kraju od użytkownika oraz poprawnie zwróci
# # sformatowaną wartość oraz sprawdzi czy dana pula numerów znajduje się na czarnej liście.
# #SUPPORTED_PREFIXES = {12, 48, 55, 81}
# # BLACK_PREFIXES = {999, 888}
# # phone_number = input('Write your phone number: ')
# # prefix = input('write prefix: ')
#
# # if int(prefix) in SUPPORTED_PREFIXES and prefix.isnumeric():
# #
# #     if phone_number.isnumeric() and len(phone_number) == 9:
# #         print(f' + {prefix} {phone_number}')
# #         if int(phone_number[0:3]) not in BLACK_PREFIXES:
# #             print(f' + {prefix} {phone_number}')
# #         else:
# #             print(f'Given number pool {phone_number[0:3]} is not supported')
# #
# #     else:
# #         print(f'Invalid phone number format')
# #
# # else:
# #     print(f' Prefix {prefix} is not supported')
#
#
# # #WARIANT 1 Napisz kod, który przyjmie dowolny tekst oraz zwróci jego długość.Zwroci ilosc znakow.
# #
# # your_text = input('Please, write your text:')
# # print('Size of your text is', len(your_text)) #mozna dodac STR() str(len(your_text)))
#
# #  WARIANT 2 Napisz kod, który przyjmie dowolny tekst oraz zwróci ilość znajdujących się w nim wyrazów.
# your_text = input('Please, write your text:')
# divided_text = len(your_text.split())
# print (f'size of your text is:  {str(divided_text)}')
#
#
# # # # WARIANT 1 Napisz kod, który przyjmie dowolny tekst oraz zwróci najdłuższy wyraz.
# some_text= input("Twoj tekst:")
#
# def the_longest_text(some_text):
#     splitted_text = some_text.split()
#     return max(splitted_text, key=len)
#
# print(the_longest_text(some_text))
#
# # # WARIANT 2 Napisz kod, który przyjmie dowolny tekst oraz zwróci najdłuższy wyraz oraz jego długość.
#
# some_text= input("Twoj tekst:")
#
# def the_longest_text(some_text):
#     splitted_text = some_text.split()
#     return max(splitted_text, key=len)
#
# print(the_longest_text(some_text))
# print(f' dlugosc tego wyrazu wynosi : {str(len(the_longest_text(some_text)))}')
#
# # # kolegi rozwiazanie oba poprzednie warianty
# # sentence = input("Enter sentence: ")
# # longest = max(sentence.split(), key=len)
# # print("Longest word is: ", longest)
# # print("And its length is: ", len(longest))
# # # drugie rozwiazanie niemal identyczne
# # text = input("your text: ")
# # print('longest word in your text: ', max(text.split(), key=len))
# # print('size of the longest word: ', len(max(text.split(), key=len)))
#
# # # WARIANT 3 Napisz kod, który przyjmie dowolny tekst oraz zwróci najdłuższy wyraz lub wyrazy jeśli jest więcej niż
# # #trenera rowiazanie
# # user_text = input("Enter text you want to examine: ")
# # words = {}
# # for word in user_text.split():
# #     if len(word) in words:
# #         words[len(word)].append(word)
# #     else:
# #         words[len(word)] = [word]
# # print(words[max(words)])


# # from collections import defaultdict
# # user_text = input("Enter text you want to examine: ")
# # words = defaultdict(list)
# # for word in user_text.split():
# #     words[len(word)].append(word)
# # if element not in banned:
# #         results.append(element)
# # print(len(results))
#
#
# # # WARIANT1 Napisz kod, który przyjmie dowolny tekst oraz zwróci ilość znajdujących się w nim wyrazów bez banned
# # # words [and, of, in, on, at, the you, but, we, he, she, I, it, my, this, that]
# #
# # user_text = input("Write your text: ")
# # banned = ['and', 'is', 'of', 'in', 'on', 'at', 'the', 'you', 'but', 'we', 'he', 'she', 'I', 'it', 'my', 'this', 'that']
# # results = []
# # for element in user_text.split():
# #     if element not in banned:
# #         results.append(element)
# # print('Number of words in your text is:' ,  str(len(results)))
# #
# #
# # # WARIANT 2 Napisz kod, który przyjmie dowolny tekst oraz zwróci ilość znajdujących się w nim wyrazów bez banned
# # # words z poprzedniego zadania oraz znaki interpunkcyjne
#
# # banned_words = ['and', 'is', 'of', 'in', 'on', 'at', 'the', 'you', 'but', 'we', 'he', 'she', 'I', 'it', 'my', 'this',
# #                 'that']
# # other_signs = [",", ".", ";", ":", "'", "\"", ">", "<", "(", ")", "{", "}", "!", "?"]
# # user_text = input("Write your text: ")
# # filtered_text = ""
# #
# # for sign in user_text:
# #     if sign not in other_signs:
# #         filtered_text += sign
# #
# # number_of_words = 0
# # for element in filtered_text.split():
# #     if element.lower() not in banned_words and element.upper() not in banned_words:
# #         number_of_words += 1
# #
# # print(f'Liczba wyrazów wynosi: {str(number_of_words)}')
#
#
# # #WARIANT 1 Napisz kod, który przyjmie od użytkownika dowolny tekst oraz, wartość którą ma wyszukać i zwróci
# # # True/False czy dany wyraz znajduje się w podanym tekście.
#
# # text = input('Write your text: ')
# #
# # searching_word = input("Write a word, you are searching for: ")
# # if searching_word.upper() in text.upper() and searching_word.lower() in text.lower():
# #     print(True)
# # else:
# #     print(False)

# # # WARIANT 2 Zaktualizuj kod z wariantu #1, od teraz kod ma zwracać ilość wystąpień szukanej frazy.

your_text = input('Write your text: ').lower()
searching_word = input("Write a word, you are searching for: ").lower()

if searching_word in your_text:
    print(f'Szukane słowo występuje {str(your_text.count(searching_word))} razy')
else:
    print("Nie znalazłem szukanego słowa")
