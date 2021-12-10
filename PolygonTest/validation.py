import re


def validate_berechnung(x, y, polygon):
    point_is_valid, text = validate_point(x, y)
    if not point_is_valid:
        return point_is_valid, text
    polygon_is_valid, text2 = validate_polygon(polygon)
    if not polygon_is_valid:
        return polygon_is_valid, text2
    return True, ""


def validate_point(x, y):
    pattern = re.compile("([0-9]*\.[0-9]+|[0-9]+)")

    if x == "":
        return False, "Die X-Koordinate des Punktes darf nicht leer sein."
    if y == "":
        return False, "Die Y-Koordinate des Punktes darf nicht leer sein."
    if not pattern.fullmatch(x):
        return False, "Die X-Koordinate muss eine Zahl sein."
    if not pattern.fullmatch(y):
        return False, "Die Y-Koordinate muss eine Zahl sein."
    return True, ""


def validate_polygon(polygon):
    if (polygon.punkte == []) or (len(polygon.punkte) < 3):
        return False, "Geben Sie mindestens 3 Polygonpunkte an."

    return True, ""
