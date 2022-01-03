import re


def validate_berechnung(x, y, polygon):
    # Diese Funktion validiert die Parameter für die Berechnung

    point_is_valid, text = validate_point(x, y)
    if not point_is_valid:
        return point_is_valid, text
    polygon_is_valid, text2 = validate_polygon(polygon)
    if not polygon_is_valid:
        return polygon_is_valid, text2
    return True, ""


def validate_point(x, y):
    # Hier werden die Punkte validiert. Dies geschieht mit Hilfe einer Regex-Pattern

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
    # Hier wird getestet, ob das Polygon aus mindestens 3 Punken besteht

    if (polygon.punkte == []) or (len(polygon.punkte) < 3):
        return False, "Geben Sie mindestens 3 Polygonpunkte an."
    return True, ""


def validate_line_in_file(zeile, index):
    # Hier wird die Punkte-Datei überprüft

    daten = zeile.split(',')
    if len(daten) < 3:
        return False, "Nicht genug Daten in Zeile " + str(index + 1)
    if len(daten) > 3:
        return False, "Zu viele Daten in Zeile " + str(index + 1)
    is_valid, txt = validate_point(daten[1], daten[2])
    if not is_valid:
        return False, txt + "in Zeile " + str(index + 1)
    return True, ""
