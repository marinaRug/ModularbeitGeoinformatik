# Das ist das Netzwerk, dass ich erstellt habe. Es besteht aus 14 Knoten, die sich in
# meinem Gebiet in Mittenwald befinden.
# Die Strecken sind auf ganze Meter gerundet

Netzwerk_Knoten_und_Kanten = {
    'P1': {'P2': 131, 'P14': 249},
    'P2': {'P1': 131, 'P3': 254},
    'P3': {'P2': 254, 'P4': 102},
    'P4': {'P3': 102, 'P5': 32},
    'P5': {'P4': 32, 'P14': 224, 'P6': 77},
    'P6': {'P5': 77, 'P7': 55, 'P8': 113},
    'P7': {'P6': 55, 'P8': 98, 'P9': 67},
    'P8': {'P6': 113, 'P7': 98, 'P11': 149},
    'P9': {'P7': 67, 'P10': 215},
    'P10': {'P9': 215, 'P11': 46},
    'P11': {'P10': 46, 'P8': 149, 'P12': 86},
    'P12': {'P11': 86, 'P13': 87},
    'P13': {'P12': 87, 'P14': 78},
    'P14': {'P13': 78, 'P1': 279, 'P5': 224}
}
