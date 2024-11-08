# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:28:37 2024

@author: Simen
"""

"""
Nedenfor er informasjon som programmet skal baseres på (som selvsagt kan diskuteres, men ikke ifm. denne oppgaven :-)

Du kan selv velge antall kjørte km/år ut fra din typiske bilbruk. Ev. (hvis du ikke har bil) kan du anta 10.000 km.
Forsikring: Elbil: 5000 kr/år. Bensinbil: 7500 kr/år.
Trafikkforsikringsavgift: 8,38 kr/dag for både elbil og bensinbil.
Drivstoffbruk: Elbil: 0,2 kWh/km. 
Strømpris (antar kun hjemmelading): 2.00 kr/kWh. Bensinbil: 1,0 kr/km.
Bomavgift: Elbil: 0,1 kr/km. Bensinbil: 0,3 kr/km.






Setter KM per år basert på eget forbruk: 20 000

"Regn ut bilkostnader"
sammenlign elbil vs fossilbil

kalkulator
variabler:
AntallKM (kan has som fast variabel, evt fylle inn selv)
ForsikringEl 
ForsikringBensin
Trafikkforsikringsavgift
DrivstoffEl 
DrivstoffBensin
LadekostEl
BomavgiftEl
BomavgiftBensin

KalkulertEl
KalkulertBensin
 
"""
"""Variabler nedenfor: """
AntallKM = 20000
ForsikringEl = 5000
ForsikringBensin = 7500
Trafikkforsikringsavgift = 8.38*365
DrivstoffEl = 0.2*AntallKM
DrivstoffBensin = 1.0*AntallKM
LadekostEl = 2.0/DrivstoffEl 


BomavgiftEl = 0.1*AntallKM
BomavgiftBensin = 0.3*AntallKM

"Utregninger: "
KalkulertEl = ForsikringEl+Trafikkforsikringsavgift+DrivstoffEl+LadekostEl+BomavgiftEl
KalkulertBensin = ForsikringBensin+Trafikkforsikringsavgift+DrivstoffBensin+BomavgiftBensin

"Prints med formattering for å få to desimaler:"
print("Pris for elbil er: ", "%.2f" % KalkulertEl, "kroner per år")
print("Pris for bensinbil er: ", "%.2f" % KalkulertBensin, "kroner per år")
print("Elbil er", "%.2f" % (KalkulertBensin-KalkulertEl), "kroner billigere per år om man kjører 20 000 km")
