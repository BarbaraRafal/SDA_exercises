def get_description(age: int):
    if age < 0:
        return None
    if age < 18:
        return f"Nastolatek"
    if age < 30:
        return f"Młody"
    if age < 50:
        return f"Dojrzały"
    if age < 65:
        return f"Wiekowy"
    return "Emeryt"

