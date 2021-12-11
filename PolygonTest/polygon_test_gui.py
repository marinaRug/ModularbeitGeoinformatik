from tkinter import *

from PolygonTest.polygon import Polygon
from PolygonTest.punkt import Punkt
from PolygonTest.punkt_in_polygon_check import punkt_in_polygon_check
from PolygonTest.validation import validate_berechnung, validate_point


class PolygonTestGui:
    polygon = Polygon()
    polygon_punkte = ""

    def starte_grafische_benutzeroberflaeche(self):
        # Erstellt ein fenster, mit gegebener Hintergrundfarbe, Größe und Titel
        fenster = Tk()
        fenster['background'] = '#283634'
        fenster.geometry("640x520")
        fenster.title("Point in polygon check.")

        self.fuege_grafische_elemente_hinzu(fenster)

        # In der Ereignisschleife auf Eingabe des Benutzers warten.
        fenster.mainloop()

    def fuege_grafische_elemente_hinzu(self, fenster):
        def punkt_in_polygon():
            x = x_koordinate.get()
            y = y_koordinate.get()
            x = x.replace(',', '.')
            y = y.replace(',', '.')

            is_valid, text = validate_berechnung(x, y, self.polygon)
            if not is_valid:
                message.config(text=text, bg="red")
            else:
                punkt = Punkt()
                punkt.x_koordinate = float(x)
                punkt.y_koordinate = float(y)
                antwort, farbe = punkt_in_polygon_check(punkt, self.polygon)
                message.config(text=antwort, bg=farbe)

        def punkt_zu_polygon_hinzufuegen():
            x = x_koordinate_polygon_punkt.get()
            y = y_koordinate_polygon_punkt.get()
            x = x.replace(',', '.')
            y = y.replace(',', '.')

            is_valid, text = validate_point(x, y)
            if not is_valid:
                message.config(text=text, bg="red")
            else:
                message.config(text="", bg="#283634")
                neuer_polygonpunkt = Punkt()
                neuer_polygonpunkt.x_koordinate = float(x)
                neuer_polygonpunkt.y_koordinate = float(y)

                self.polygon.punkte.append(neuer_polygonpunkt)
                self.polygon_punkte = self.polygon_punkte + "[" + str(neuer_polygonpunkt.x_koordinate) + "," + str(neuer_polygonpunkt.y_koordinate) + "]"
            polygon_points.config(text=self.polygon_punkte, wraplength=500)

        def reset():
            message.config(text="", bg="#283634")
            self.polygon = Polygon()
            self.polygon_punkte = ""
            polygon_points.config(text=self.polygon_punkte, wraplength=500)
            y_koordinate_polygon_punkt.delete(0, 'end')
            x_koordinate_polygon_punkt.delete(0, 'end')
            x_koordinate.delete(0, 'end')
            y_koordinate.delete(0, 'end')

        # Erstellt grafische Elemente die auf dem Hauptfenster angezeigt werden

        # Point to check, x-coordinate
        x_koordinate = Entry(fenster, bd=5, width=20)
        punkt_x_label = Label(fenster, text="Point: X-Coordinate", bg='#283634', fg='#F0F3EB')

        # Point to check, y-coordinate
        y_koordinate = Entry(fenster, bd=5, width=20)
        punkt_y_label = Label(fenster, text="Point: Y-Coordinate", bg='#283634', fg='#F0F3EB')

        fill_polygon_label = Label(fenster, text="Add points to your polygon!", bg='#283634', fg='#F0F3EB')

        # Points to add to polygon
        x_koordinate_polygon_punkt = Entry(fenster, bd=5, width=20)
        punkt_x_label_polygon_punkt = Label(fenster, text="Polygon-Point: X-Coordinate", bg='#283634', fg='#F0F3EB')

        # Point to check, y-coordinate
        y_koordinate_polygon_punkt = Entry(fenster, bd=5, width=20)
        punkt_y_label_polygon_punkt = Label(fenster, text="Polygon-Point: Y-Coordinate", bg='#283634', fg='#F0F3EB')

        punkt_hinzufuegen_button = Button(fenster, text='Add to polygon', bg='#9BABA0', fg='#F0F3EB', command=punkt_zu_polygon_hinzufuegen)

        berechne_button = Button(fenster, text='Berechne', bg='#9BABA0', fg='#F0F3EB', command=punkt_in_polygon)
        reset_button = Button(fenster, text='Reset', bg='#9BABA0', fg='#F0F3EB', command=reset)

        polygon_points = Label(fenster, bg="#283634")

        message = Label(fenster, bg="#283634")
        empty_space1 = Label(fenster, bg="#283634")
        empty_space2 = Label(fenster, bg="#283634")
        empty_space3 = Label(fenster, bg="#283634")
        empty_space4 = Label(fenster, bg="#283634")
        empty_space5 = Label(fenster, bg="#283634")
        empty_space6 = Label(fenster, bg="#283634")

        # Erstellt ein grid in dem die Elemente angeordnet werden
        anweisungs_label = Label(fenster, text="Use this tool to check if a point is inside a polygon.", bg='#283634', fg='#F0F3EB')

        anweisungs_label.grid(row=0)
        message.grid(row=1)
        empty_space1.grid(row=2)

        fill_polygon_label.grid(row=3)
        punkt_x_label_polygon_punkt.grid(row=4)
        x_koordinate_polygon_punkt.grid(row=5)
        punkt_y_label_polygon_punkt.grid(row=6)
        y_koordinate_polygon_punkt.grid(row=7)
        empty_space2.grid(row=8)
        punkt_hinzufuegen_button.grid(row=9)
        empty_space3.grid(row=10)

        polygon_points.grid(row=11)

        empty_space4.grid(row=12)
        punkt_x_label.grid(row=13)
        x_koordinate.grid(row=14)
        punkt_y_label.grid(row=15)
        y_koordinate.grid(row=16)

        empty_space5.grid(row=17)
        berechne_button.grid(row=18)
        empty_space6.grid(row=19)
        reset_button.grid(row=20)
        fenster.grid_columnconfigure(0, weight=1)
