def berechne_route_nach_dijkstra(Netzwerk_Knoten_und_Kanten, startpunkt, zielpunkt, punkt_geprueft, entfernungen, vorgaenger):
    if startpunkt not in Netzwerk_Knoten_und_Kanten:
        return 'Startpunkt nicht vorhanden - Bitte geben Sie P gefolgt von einer Zahl zwischen 1 und 14 ein.'
    if zielpunkt not in Netzwerk_Knoten_und_Kanten:
        return 'Zielpunkt nicht vorhanden - Bitte geben Sie P gefolgt von einer Zahl zwischen 1 und 14 ein.'
    if startpunkt == zielpunkt:
        weg_pfad = []
        variable_fuer_vorgaenger = zielpunkt
        while variable_fuer_vorgaenger != None:
            weg_pfad.append(variable_fuer_vorgaenger)
            variable_fuer_vorgaenger = vorgaenger.get(variable_fuer_vorgaenger, None)
        text = str(" Länge (in Meter): " + str(entfernungen[zielpunkt]) + " -> Kürzester Weg: " + str(weg_pfad[::-1]))
        return text
    else:
        if not punkt_geprueft:
            entfernungen[startpunkt] = 0
        for nachbarpunkt in Netzwerk_Knoten_und_Kanten[startpunkt]:
            if nachbarpunkt not in punkt_geprueft:
                neue_entfernung = entfernungen[startpunkt] + Netzwerk_Knoten_und_Kanten[startpunkt][nachbarpunkt]
                if neue_entfernung < entfernungen.get(nachbarpunkt, float('inf')):
                    entfernungen[nachbarpunkt] = neue_entfernung
                    vorgaenger[nachbarpunkt] = startpunkt
        punkt_geprueft.append(startpunkt)
        ungeprueft = {}
        for k in Netzwerk_Knoten_und_Kanten:
            if k not in punkt_geprueft:
                ungeprueft[k] = entfernungen.get(k, float('inf'))
        nd = min(ungeprueft, key=ungeprueft.get)
        return berechne_route_nach_dijkstra(Netzwerk_Knoten_und_Kanten, nd, zielpunkt, punkt_geprueft, entfernungen, vorgaenger)



