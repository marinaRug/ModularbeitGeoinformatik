from PolygonTest.polygon import Polygon
from PolygonTest.punkt import Punkt


def punkt_in_polygon_check(punkt: Punkt, polygon: Polygon):
    # Diese Funktion berechnet, ob der Punkt in dem Polygon liegt
    # Quelle: Algorithms & Technologies.Punkt-in-Polygon in Python. https://www.algorithms-and-technologies.com/de/punkt_in_polygon/Python (03.01.2022)

    punkt_in_polygon = False
    i = 0
    j = len(polygon.punkte) - 1
    while i < len(polygon.punkte) - 1:
        i = i + 1
        if (((polygon.punkte[i].y_koordinate > punkt.y_koordinate) != (polygon.punkte[j].y_koordinate > punkt.y_koordinate)) and (punkt.x_koordinate < (
                (polygon.punkte[j].x_koordinate - polygon.punkte[i].x_koordinate) *
                (punkt.y_koordinate - polygon.punkte[i].y_koordinate) / (polygon.punkte[j].y_koordinate - polygon.punkte[i].y_koordinate)) + polygon.punkte[
                                                                                                                                      i].x_koordinate)):
            punkt_in_polygon = not punkt_in_polygon
        j = i

    if punkt_in_polygon:
        return "Der Punkt liegt in dem Polygon", "green"
    return "Der Punkt liegt nicht in dem Polygon", "red"
