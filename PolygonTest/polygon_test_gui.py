from tkinter import *

from PolygonTest.polygon import Polygon
from PolygonTest.punkt import Punkt
from PolygonTest.punkt_in_polygon_check import punkt_in_polygon_check
from PolygonTest.validation import validate_berechnung, validate_point, validate_line_in_file

WINDOW_WIDTH_HALBE = 350


class PolygonTestGui:
    polygon = Polygon([])
    polygon_punkte = ""

    def starte_grafische_benutzeroberflaeche(self):
        # Erstellt ein fenster, mit gegebener Hintergrundfarbe, Größe und Titel
        fenster = Tk()
        fenster['background'] = '#283634'
        fenster.geometry("700x700")
        fenster.title("Punkt in Polygon Test")

        # Erstellt einen Main Frame
        main_frame = Frame(fenster)
        main_frame.pack(fill=BOTH, expand=1, side=TOP)

        # Canvas für die scrollbar
        fenster_canvas = Canvas(main_frame)
        fenster_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Scrollbar
        scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=fenster_canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Canvas konfigurieren -> Scrollbar
        fenster_canvas.configure(yscrollcommand=scrollbar.set)
        fenster_canvas['background'] = '#283634'
        fenster_canvas.bind('<Configure>', lambda e: fenster_canvas.configure(scrollregion=fenster_canvas.bbox("all")))

        # Frame in Canvas für die Scrollbar

        frame = Frame(fenster_canvas)
        frame['background'] = '#283634'
        fenster_canvas.create_window((WINDOW_WIDTH_HALBE, 0), window=frame, anchor=N)

        self.fuege_grafische_elemente_hinzu(frame)

        # In der Ereignisschleife auf Eingabe des Benutzers warten.
        fenster.mainloop()

    def fuege_grafische_elemente_hinzu(self, frame):
        def punkt_in_polygon():
            x = x_koordinate.get()
            y = y_koordinate.get()
            x = x.replace(',', '.')
            y = y.replace(',', '.')

            is_valid, text = validate_berechnung(x, y, self.polygon)
            if not is_valid:
                message.config(text=text, bg="red")
            else:
                punkt = Punkt(float(x), float(y))
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
                neuer_polygonpunkt = Punkt(float(x), float(y))

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
                    neuer_polygonpunkt = Punkt(float(daten[1]), float(daten[2]))
                    self.polygon.punkte.append(neuer_polygonpunkt)
                    self.polygon_punkte = self.polygon_punkte + "[" + str(neuer_polygonpunkt.x_koordinate) + "," + str(neuer_polygonpunkt.y_koordinate) + "]"
                    polygon_points.config(text=self.polygon_punkte, wraplength=500)

        def reset():
            message.config(text="", bg="#283634")
            self.polygon.punkte = []
            self.polygon_punkte = ""
            polygon_points.config(text=self.polygon_punkte, wraplength=500)
            y_koordinate_polygon_punkt.delete(0, 'end')
            x_koordinate_polygon_punkt.delete(0, 'end')
            x_koordinate.delete(0, 'end')
            y_koordinate.delete(0, 'end')

        # Erstellt grafische Elemente die auf dem Hauptfenster angezeigt werden

        # Point to check, x-coordinate
        x_koordinate = Entry(frame, bd=5, width=20)
        punkt_x_label = Label(frame, text="Punkt: X-Koordinate", bg='#283634', fg='#F0F3EB')

        # Point to check, y-coordinate
        y_koordinate = Entry(frame, bd=5, width=20)
        punkt_y_label = Label(frame, text="Punkt: Y-Koordinate", bg='#283634', fg='#F0F3EB')

        fill_polygon_label = Label(frame, text="Fügen Sie Punkte zum Polygon hinzu!", bg='#283634', fg='#F0F3EB')

        # Points to add to polygon
        x_koordinate_polygon_punkt = Entry(frame, bd=5, width=20)
        punkt_x_label_polygon_punkt = Label(frame, text="Polygon-Punkt: X-Koordinate", bg='#283634', fg='#F0F3EB')

        # Point to check, y-coordinate
        y_koordinate_polygon_punkt = Entry(frame, bd=5, width=20)
        punkt_y_label_polygon_punkt = Label(frame, text="Polygon-Punkt: Y-Koordinate", bg='#283634', fg='#F0F3EB')

        punkt_hinzufuegen_button = Button(frame, text='Punkt zu Polygon hinzufügen', bg='#9BABA0', fg='#F0F3EB', command=punkt_zu_polygon_hinzufuegen)
        punkte_liste_hinzufuegen_button = Button(frame, text='Punkteliste hinzufügen', bg='#9BABA0', fg='#F0F3EB', command=file_hochladen)
        oder_label = Label(frame, text="oder", bg='#283634', fg='#F0F3EB')

        berechne_button = Button(frame, text='Berechne', bg='#9BABA0', fg='#F0F3EB', command=punkt_in_polygon)
        reset_button = Button(frame, text='Reset', bg='#9BABA0', fg='#F0F3EB', command=reset)

        polygon_points = Label(frame, bg="#283634")

        info_label = Label(frame, text="Info zum Fileupload: File mit den Punkten in das Verzeichnis legen.", bg="#283634", fg='#F0F3EB')
        info2_label = Label(frame, text="File muss den Namen \"punkte.txt\" haben.", bg="#283634", fg='#F0F3EB')
        info3_label = Label(frame, text="In der letzten Zeile des Files kein Strichpunkt.", bg="#283634", fg='#F0F3EB')
        schema_label = Label(frame, text="Fileupload-Schema: P1, 66.8, 988.5;", bg="#283634", fg='#F0F3EB')

        message = Label(frame, bg="#283634")
        empty_space1 = Label(frame, bg="#283634")
        empty_space2 = Label(frame, bg="#283634")
        empty_space3 = Label(frame, bg="#283634")
        empty_space4 = Label(frame, bg="#283634")
        empty_space5 = Label(frame, bg="#283634")
        empty_space6 = Label(frame, bg="#283634")

        # Erstellt ein grid in dem die Elemente angeordnet werden
        anweisungs_label = Label(frame, text="Überprüfen Sie, ob ein Punkt im Polygon liegt!", bg='#283634', fg='#F0F3EB')

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

        frame.grid_columnconfigure(0, weight=1)
