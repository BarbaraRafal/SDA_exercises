# # # Wariant 1 Dodaj swoje imie do listy i zwróc posortowana liste
# # quest_list = ['Adam', 'Tomasz', 'Marta']
# #
# # my_name = input ('My name is: ')
# # quest_list.append(my_name)
# # print(sorted(quest_list))
#
# #2 napisz funkcje formatujaca nr telefonu  format_phone_number wraz z prefixem krajowyn (np. +48). Wykorzystaj argumenty domyslne dla kodu kraju.
#
# # def format_phone_number(phone_number, prefix="+48"):
# #     return prefix + str(phone_number)
# # print(format_phone_number(665221001, "+47 "))
#
# #3 napisz funkcję ktora zwróci indeks elementu, gdy ten bedzie taki sam jakiego szukamy.
# # list= ['a','b','c']
# # def find_index(list, target):
# #         if target in list:
# #             return list.index(target)
# #
# # print(find_index(list, 'c'))
#
# # zadanie 4 napisz od ktory przyjmie dowolny tekst od użytkownika oraz zwróci go bez duplikatu
# #trenera rozwiązanie
# #wariant 1
# # def remove_duplicates(text): # jako argument tylko tekst bez szukanego duplikatu
# #     unique_words = []
# #     for word in text.split():
# #         if word not in unique_words:
# #             unique_words.append(word) # bo jesli sie pojawi to go nie doda
# #     return ' '.join(unique_words)
# # print(remove_duplicates('some random some some some some'))
#
# # wariant 2 wyswietli text bez duplikatow i wyswietli ilosc powtorzen
# #
# # def remove_duplicates(text):
# #     number_of_repetitions = 0
# #     unique_words = []
# #
# #     for word in text.split():
# #         if word not in unique_words:
# #             unique_words.append(word) # bo jesli sie pojawi to go nie doda
# #         else :
# #             number_of_repetitions += 1
# #
# #     return ' '.join(unique_words), number_of_repetitions
# # print(remove_duplicates('mój mój piękny dom na warmii'))
#
# # napisz kod ktory przyjmie sekwencję liczb oraz wypełni jej brakujące wartości
def fill_gaps(elements):
    filled = []
    for index in range(elements[0] ,elements[-1] +1): # start i stop zdefiniowane
        filled.append(index)
    return filled

print(fill_gaps([1, 2, 6, 8]))
#
# #napisz kod ktory pzyjmie od uzytkownika  tekst i zliczy oraz zwroci ilosc wystapien znaków
# # def occurrences(text):
# #     character_occurrences = {}
# #
# #     for character in text:
# #         if character_occurrences.get(character):
# #             character_occurrences[character] += 1
# #         else:
# #             character_occurrences[character] = 1
# #     return character_occurrences
# #
# # print(occurrences('abbbccc'))
# # # rozwiązanie Patryka
# # from collections import Counter
# # def your_text(text):
# #     text = text.lower()
# #     res = Counter(text)
# #     return str(res)
# # print(your_text(input("Your text: ")))
#
#
# # zadanie z otwieraniem pliku i importem wybranych danych
# # with open('text.txt', 'r') as file:
# #     lines = file.readlines()
# #
# # result=[]
# # for x in lines:
# #     result.append(x.split("|")[1])
# #     # file.close()# chyba nie potrzebne zamykanie
# # print(result)
#
# ### Napisz funkcję, która odczyta filmy z pliku oraz zwróci tylko filmy nakręcone po roku 2000
# # def filtered_movies(file_path):
# #     with open('movie.txt') as file:
# #         for lines in file:
# #             year = int(lines.split('|')[2])
# #             if year >= 2000:
# #                 print(lines)
# #
# # print(filtered_movies("movie.txt"))
#
# ### Napisz funkcję ktora dodoa nowy film do pliku JA ZROBIłam sama!!!
#
# # DATABASE_PATH = 'movies.txt'
# # def add_movie(title, year):
# #     with open(DATABASE_PATH, 'a') as file:
# #         file.write(f'{title}|{year}\n')
# # add_movie('Catch me if you can', 2002)
#
#
# # ####  dodac wartosc punktów. Tu raz odczytujemy linie i drugi raz odczytujemy linie z pliku do zapisu. Rozwiazanie trenera
# #
# # DATABASE_PATH = 'add_points.txt'
# # def add_points(value=20):
# #     with open(DATABASE_PATH, 'r') as read_handler:
# #         lines = read_handler.readlines()
# #     with open(DATABASE_PATH, 'w') as write_handler:
# #         for line in lines:
# #             name, points = line.split('|')
# #             write_handler.write(f'{name}|{int(points) + value}\n')
# # add_points(5)
# #
# # ### usuń film po podanym id filmu
# # #
# # DATABASE_PATH = 'movie.txt'
# # def remove(movie_id):
# #     with open(DATABASE_PATH, 'r') as file_read:
# #         lines = file_read.readlines()
# #         print(lines)
# #
# #     with open(DATABASE_PATH,'w') as file_write:
# #         for line in lines:
# #              if int(line.split('|')[0]) != movie_id:
# #                  file_write.write(line)
# # remove(3)
#
# # HOME WORK
#
# # Napisz funkcję, która wyświetli `schody` w formaciedef render_stairs(size) -> str:
#
# def render_stairs(size):
#     spa = " "
#     ste = "#"
#     n = int(size)
#     for i in range(n+1):
#         print(((n-i)*spa)+(i*ste))
#         pass
#
# render_stairs(5)
#
# # Napisz funkcje przeliczajace stopnie Celsjusza na Fahrenheita i na odwrót
#
# # def celsius_to_fahrenheit(temperature_C):
# #     temperature_F = (temperature_C* 1.8)+32
# #     print(f'Temperature {temperature_C}C is equal to {temperature_F}F ')
# #     return
# # celsius_to_fahrenheit(32)
#
# # def fahrenheit_to_celsius(temperature_F):
# #     temperature_C = (temperature_F-32)*0.56
# #     print(f'Temperature {temperature_F}F is equal to {temperature_C}C ')
# #     return
# # fahrenheit_to_celsius(56)


if __name__ == "__main__":
    print(fill_gaps([1, 2, 6,mis 8]))