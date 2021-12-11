from tkinter import *
import os

from Dijkstra.dikstra_algorithmus import berechne_route_nach_dijkstra
from Dijkstra.netzwerk_knoten_und_kanten import Netzwerk_Knoten_und_Kanten


class DijkstraAlgorithmusGui:

    def starte_grafische_benutzeroberflaeche(self):
        # Erstellt ein fenster, mit gegebener Hintergrundfarbe, Größe und Titel
        fenster = Tk()
        fenster['background'] = '#283634'
        fenster.geometry("900x950")
        fenster.title("Dijkstra - Shortest Way")
        directory_path = os.path.dirname(__file__)
        filepath = os.path.join(directory_path, 'dijkstra_mittenwald.png')
        canvas = Canvas(fenster, width=625, height=400)
        canvas.grid(row=0)
        img = PhotoImage(file=filepath)
        canvas.create_image(0, 0, anchor=NW, image=img)

        self.fuege_grafische_elemente_hinzu(fenster)

        # In der Ereignisschleife auf Eingabe des Benutzers warten.
        fenster.mainloop()

    def fuege_grafische_elemente_hinzu(self, fenster):
        def kuerzester_weg_berechnung():
            netzwerk = Netzwerk_Knoten_und_Kanten
            start = startpunkt.get()
            ziel = zielpunkt.get()

            text = berechne_route_nach_dijkstra(netzwerk, start, ziel, [], {}, {})
            ergebnis.config(text=text)

        label1 = Label(fenster, text="Coordinates:", bg='#283634', fg='#F0F3EB')

        punkt1 = Label(fenster, text="Point1: [670801.50, 5256604.50]", bg='#283634', fg='#F0F3EB')
        punkt2 = Label(fenster, text="Point2: [670765.75, 5256474.50]", bg='#283634', fg='#F0F3EB')
        punkt3 = Label(fenster, text="Point3: [670534.25, 5256568.00]", bg='#283634', fg='#F0F3EB')
        punkt4 = Label(fenster, text="Point4: [670506.50, 5256470.25]", bg='#283634', fg='#F0F3EB')
        punkt5 = Label(fenster, text="Point5: [670476.75, 5256482.00]", bg='#283634', fg='#F0F3EB')
        punkt6 = Label(fenster, text="Point6: [670436.75, 5256422.00]", bg='#283634', fg='#F0F3EB')
        punkt7 = Label(fenster, text="Point7: [670387.25, 5256441.25]", bg='#283634', fg='#F0F3EB')
        punkt8 = Label(fenster, text="Point8: [670423.25, 5256520.75]", bg='#283634', fg='#F0F3EB')
        punkt9 = Label(fenster, text="Point9: [670329.00, 5256471.50]", bg='#283634', fg='#F0F3EB')
        punkt10 = Label(fenster, text="Point10: [670371.75, 5256674.75]", bg='#283634', fg='#F0F3EB')
        punkt11 = Label(fenster, text="Point11: [670420.50, 5256673.50]", bg='#283634', fg='#F0F3EB')
        punkt12 = Label(fenster, text="Point12: [670420.25, 5256761.25]", bg='#283634', fg='#F0F3EB')
        punkt13 = Label(fenster, text="Point13: [670503.75, 5256750.00]", bg='#283634', fg='#F0F3EB')
        punkt14 = Label(fenster, text="Point14: [670551.50, 5256691.50]", bg='#283634', fg='#F0F3EB')

        startpunkt = Entry(fenster, bd=5, width=20)
        startpunkt_label = Label(fenster, text="Enter start point:", bg='#283634', fg='#F0F3EB')
        zielpunkt = Entry(fenster, bd=5, width=20)
        zielpunkt_label = Label(fenster, text="Enter end point:", bg='#283634', fg='#F0F3EB')
        berechne_button = Button(fenster, text='Berechne', bg='#9BABA0', fg='#F0F3EB', command=kuerzester_weg_berechnung)
        ergebnis = Label(fenster, text='Kürzester Weg:', bg='#283634', fg='#F0F3EB')

        empty_space1 = Label(fenster, bg="#283634")
        empty_space2 = Label(fenster, bg="#283634")
        empty_space3 = Label(fenster, bg="#283634")

        label1.grid(row=1)
        punkt1.grid(row=2)
        punkt2.grid(row=3)
        punkt3.grid(row=4)
        punkt4.grid(row=5)
        punkt5.grid(row=6)
        punkt6.grid(row=7)
        punkt7.grid(row=8)
        punkt8.grid(row=9)
        punkt9.grid(row=10)
        punkt10.grid(row=11)
        punkt11.grid(row=12)
        punkt12.grid(row=13)
        punkt13.grid(row=14)
        punkt14.grid(row=15)
        empty_space1.grid(row=16)
        startpunkt_label.grid(row=17)
        startpunkt.grid(row=18)
        zielpunkt_label.grid(row=19)
        zielpunkt.grid(row=20)
        empty_space2.grid(row=21)
        berechne_button.grid(row=22)
        empty_space3.grid(row=23)
        ergebnis.grid(row=24)

        fenster.grid_columnconfigure(0, weight=1)
