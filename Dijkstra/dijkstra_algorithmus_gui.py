from tkinter import *
import os

from Dijkstra.dikstra_algorithmus import berechne_route_nach_dijkstra
from Dijkstra.netzwerk_knoten_und_kanten import Netzwerk_Knoten_und_Kanten

WINDOW_WIDTH_HALBE = 450


class DijkstraAlgorithmusGui:

    def starte_grafische_benutzeroberflaeche(self):
        # Erstellt ein fenster, mit gegebener Hintergrundfarbe, Größe und Titel
        fenster = Tk()
        fenster['background'] = '#283634'
        fenster.geometry("900x950")
        fenster.title("Dijkstra - Shortest Way")

        # Erstellt einen Main Frame
        main_frame = Frame(fenster)
        main_frame.pack(fill=BOTH, expand=1)

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

        directory_path = os.path.dirname(__file__)
        filepath = os.path.join(directory_path, 'dijkstra_mittenwald.png')
        canvas = Canvas(frame, width=625, height=400)
        canvas.pack()
        img = PhotoImage(file=filepath)
        canvas.create_image(0, 0, anchor=NW, image=img)

        self.fuege_grafische_elemente_hinzu(frame)

        # In der Ereignisschleife auf Eingabe des Benutzers warten.
        fenster.mainloop()

    def fuege_grafische_elemente_hinzu(self, frame):
        def kuerzester_weg_berechnung():
            netzwerk = Netzwerk_Knoten_und_Kanten
            start = startpunkt.get()
            ziel = zielpunkt.get()

            text = berechne_route_nach_dijkstra(netzwerk, start, ziel, [], {}, {})
            ergebnis.config(text=text)

        label1 = Label(frame, text="Coordinates:", bg='#283634', fg='#F0F3EB')

        punkt1 = Label(frame, text="Point1: [670801.50, 5256604.50]", bg='#283634', fg='#F0F3EB')
        punkt2 = Label(frame, text="Point2: [670765.75, 5256474.50]", bg='#283634', fg='#F0F3EB')
        punkt3 = Label(frame, text="Point3: [670534.25, 5256568.00]", bg='#283634', fg='#F0F3EB')
        punkt4 = Label(frame, text="Point4: [670506.50, 5256470.25]", bg='#283634', fg='#F0F3EB')
        punkt5 = Label(frame, text="Point5: [670476.75, 5256482.00]", bg='#283634', fg='#F0F3EB')
        punkt6 = Label(frame, text="Point6: [670436.75, 5256422.00]", bg='#283634', fg='#F0F3EB')
        punkt7 = Label(frame, text="Point7: [670387.25, 5256441.25]", bg='#283634', fg='#F0F3EB')
        punkt8 = Label(frame, text="Point8: [670423.25, 5256520.75]", bg='#283634', fg='#F0F3EB')
        punkt9 = Label(frame, text="Point9: [670329.00, 5256471.50]", bg='#283634', fg='#F0F3EB')
        punkt10 = Label(frame, text="Point10: [670371.75, 5256674.75]", bg='#283634', fg='#F0F3EB')
        punkt11 = Label(frame, text="Point11: [670420.50, 5256673.50]", bg='#283634', fg='#F0F3EB')
        punkt12 = Label(frame, text="Point12: [670420.25, 5256761.25]", bg='#283634', fg='#F0F3EB')
        punkt13 = Label(frame, text="Point13: [670503.75, 5256750.00]", bg='#283634', fg='#F0F3EB')
        punkt14 = Label(frame, text="Point14: [670551.50, 5256691.50]", bg='#283634', fg='#F0F3EB')

        startpunkt = Entry(frame, bd=5, width=20)
        startpunkt_label = Label(frame, text="Enter start point:", bg='#283634', fg='#F0F3EB')
        zielpunkt = Entry(frame, bd=5, width=20)
        zielpunkt_label = Label(frame, text="Enter end point:", bg='#283634', fg='#F0F3EB')
        berechne_button = Button(frame, text='Berechne', bg='#9BABA0', fg='#F0F3EB', command=kuerzester_weg_berechnung)
        ergebnis = Label(frame, text='Kürzester Weg:', bg='#283634', fg='#F0F3EB')

        empty_space1 = Label(frame, bg="#283634")
        empty_space2 = Label(frame, bg="#283634")
        empty_space3 = Label(frame, bg="#283634")

        label1.pack()
        punkt1.pack()
        punkt2.pack()
        punkt3.pack()
        punkt4.pack()
        punkt5.pack()
        punkt6.pack()
        punkt7.pack()
        punkt8.pack()
        punkt9.pack()
        punkt10.pack()
        punkt11.pack()
        punkt12.pack()
        punkt13.pack()
        punkt14.pack()
        empty_space1.pack()
        startpunkt_label.pack()
        startpunkt.pack()
        zielpunkt_label.pack()
        zielpunkt.pack()
        empty_space2.pack()
        berechne_button.pack()
        empty_space3.pack()
        ergebnis.pack()
