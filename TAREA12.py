#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades.
# En una dimensión, puedes tener diferentes ciudades,
# en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.),
# y en la tercera dimensión, semanas.

temperaturas = [
    [   # QUITO
        [   # Semana 1
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 75},
            {"day": "Jueves", "temp": 56},
            {"day": "Viernes", "temp": 40},
            {"day": "Sábado", "temp": 41},
            {"day": "Domingo", "temp": 47}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 76},
            {"day": "Martes", "temp": 79},
            {"day": "Miércoles", "temp": 83},
            {"day": "Jueves", "temp": 81},
            {"day": "Viernes", "temp": 87},
            {"day": "Sábado", "temp": 89},
            {"day": "Domingo", "temp": 93}
        ],

    ],
    [   # Guayaquil
        [   # Semana 1
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 45},
            {"day": "Miércoles", "temp": 57},
            {"day": "Jueves", "temp": 47},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 34},
            {"day": "Domingo", "temp": 40}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 50},
            {"day": "Martes", "temp": 47},
            {"day": "Miércoles", "temp": 41},
            {"day": "Jueves", "temp": 36},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 40}
        ],

        ]
        ]



# Calcular el promedio de temperaturas para cada ciudad y semana
for ciudad in temperaturas:
    for semana in ciudad:
        suma = 0
        for dia in semana:
            suma += dia['temp']
        print(suma)
