from PolygonTest.polygon import Polygon
from PolygonTest.punkt import Punkt


def punkt_in_polygon_check(punkt: Punkt, polygon: Polygon()):
    # polygon = [(2, 1), (2, 3), (3, 4), (5, 4), (5, 2), (4,1)]
    # point = [3, 2]

    point_in_polygon = False
    i = 0
    j = len(polygon.punkte) - 1
    while i < len(polygon.punkte) - 1:
        i = i + 1
        if (((polygon.punkte[i].y_koordinate > punkt.y_koordinate) != (polygon.punkte[j].y_koordinate > punkt.y_koordinate)) and (punkt.x_koordinate < (
                (polygon.punkte[j].x_koordinate - polygon.punkte[i].x_koordinate) *
                (punkt.y_koordinate - polygon.punkte[i].y_koordinate) / (polygon.punkte[j].y_koordinate - polygon.punkte[i].y_koordinate)) + polygon.punkte[
                                                                                                                                      i].x_koordinate)):
            # Invert point_in_polygon
            point_in_polygon = not point_in_polygon
        j = i
    # If the number of crossings was point_in_polygon, the point is in the polygon
    if point_in_polygon:
        return "Der Punkt liegt in dem Polygon", "green"
    return "Der Punkt liegt nicht in dem Polygon", "red"
