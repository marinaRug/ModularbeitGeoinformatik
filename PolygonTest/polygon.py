from typing import List

from PolygonTest.punkt import Punkt


class Polygon:

    def __init__(self, punkte: List[Punkt]):
        self.punkte = punkte
