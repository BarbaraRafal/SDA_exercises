import modul_a as m_a

items = ["Myszka", "Monitor", "Kubek"]

if __name__ == "__main__":
    print(m_a.test)
    element = "Kubek"
    index = m_a.find_index(items, element)
    if index is not None:
        print(f"Index przedmiotu {element} to {index}")
    else:
        print(f"Przedmiotu {element} nie ma w kolekcji")
