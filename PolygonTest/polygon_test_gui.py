from tkinter import *

from PolygonTest.polygon import Polygon
from PolygonTest.punkt import Punkt
from PolygonTest.punkt_in_polygon_check import punkt_in_polygon_check
from PolygonTest.validation import validate_berechnung, validate_point, validate_line_in_file


class PolygonTestGui:
    polygon = Polygon()
    polygon_punkte = ""

    def starte_grafische_benutzeroberflaeche(self):
        # Erstellt ein fenster, mit gegebener Hintergrundfarbe, Größe und Titel
        fenster = Tk()
        fenster['background'] = '#283634'
        fenster.geometry("700x700")
        fenster.title("Point in Polygon Test")

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
            polygon_points.config(text=self.polygon_punkte, wraplength=650)

        def file_hochladen():
            with open("punkte.txt", "r") as file:
                lines = file.read().split(';')

            for line in lines:
                is_valid, text = validate_line_in_file(line, lines.index(line))
                if not is_valid:
                    message.config(text=text, bg="red")
                    break
                else:
                    daten = line.split(',')
                    neuer_polygonpunkt = Punkt()
                    neuer_polygonpunkt.x_koordinate = float(daten[1])
                    neuer_polygonpunkt.y_koordinate = float(daten[2])
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
        punkt_x_label = Label(fenster, text="Punkt: X-Koordinate", bg='#283634', fg='#F0F3EB')

        # Point to check, y-coordinate
        y_koordinate = Entry(fenster, bd=5, width=20)
        punkt_y_label = Label(fenster, text="Punkt: Y-Koordinate", bg='#283634', fg='#F0F3EB')

        fill_polygon_label = Label(fenster, text="Fügen Sie Punkte zum Polygon hinzu!", bg='#283634', fg='#F0F3EB')

        # Points to add to polygon
        x_koordinate_polygon_punkt = Entry(fenster, bd=5, width=20)
        punkt_x_label_polygon_punkt = Label(fenster, text="Polygon-Punkt: X-Koordinate", bg='#283634', fg='#F0F3EB')

        # Point to check, y-coordinate
        y_koordinate_polygon_punkt = Entry(fenster, bd=5, width=20)
        punkt_y_label_polygon_punkt = Label(fenster, text="Polygon-Punkt: Y-Koordinate", bg='#283634', fg='#F0F3EB')

        punkt_hinzufuegen_button = Button(fenster, text='Punkt zu Polygon hinzufügen', bg='#9BABA0', fg='#F0F3EB', command=punkt_zu_polygon_hinzufuegen)
        punkte_liste_hinzufuegen_button = Button(fenster, text='Punkteliste hinzufügen', bg='#9BABA0', fg='#F0F3EB', command=file_hochladen)
        oder_label = Label(fenster, text="oder", bg='#283634', fg='#F0F3EB')

        berechne_button = Button(fenster, text='Berechne', bg='#9BABA0', fg='#F0F3EB', command=punkt_in_polygon)
        reset_button = Button(fenster, text='Reset', bg='#9BABA0', fg='#F0F3EB', command=reset)

        polygon_points = Label(fenster, bg="#283634")

        info_label = Label(fenster, text="Info zum Fileupload: File mit den Punkten in das Verzeichnis legen.", bg="#283634")
        info2_label = Label(fenster, text="File muss den Namen \"punkte.txt\" haben.", bg="#283634")
        info3_label = Label(fenster, text="In der letzten Zeile des Files kein Strichpunkt.", bg="#283634")
        schema_label = Label(fenster, text="Fileupload-Schema: P1, 66.8, 988.5;", bg="#283634")

        message = Label(fenster, bg="#283634")
        empty_space1 = Label(fenster, bg="#283634")
        empty_space2 = Label(fenster, bg="#283634")
        empty_space3 = Label(fenster, bg="#283634")
        empty_space4 = Label(fenster, bg="#283634")
        empty_space5 = Label(fenster, bg="#283634")
        empty_space6 = Label(fenster, bg="#283634")

        # Erstellt ein grid in dem die Elemente angeordnet werden
        anweisungs_label = Label(fenster, text="Überprüfen Sie, ob ein Punkt im Polygon liegt!", bg='#283634', fg='#F0F3EB')

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
        oder_label.grid(row=11)
        punkte_liste_hinzufuegen_button.grid(row=12)
        empty_space3.grid(row=13)

        polygon_points.grid(row=14)

        empty_space4.grid(row=15)
        punkt_x_label.grid(row=16)
        x_koordinate.grid(row=17)
        punkt_y_label.grid(row=18)
        y_koordinate.grid(row=19)

        empty_space5.grid(row=20)
        berechne_button.grid(row=21)
        empty_space6.grid(row=22)
        reset_button.grid(row=23)

        info_label.grid(row=24)
        info2_label.grid(row=25)
        info3_label.grid(row=26)
        schema_label.grid(row=27)

        fenster.grid_columnconfigure(0, weight=1)
