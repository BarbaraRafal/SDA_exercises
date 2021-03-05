from person.descriptor import get_description


def start_app():
    while True:
        print("Aby wyjść wpisz 'x'")
        given_age = input("Proszę podać swój wiek: ")
        if given_age == "x":
            print("Do widzenia!")
            break
        age_description = get_description(age=int(given_age))
        if age_description is None:
            print(f"Podany wiek: {given_age} jest błędny!")
            print("Spróbuj jeszcze raz")
        else:
            print(f"Twoja grupa wiekowa to: {age_description}")


start = start_app()

