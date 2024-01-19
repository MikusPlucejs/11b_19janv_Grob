# Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila.

import csv

def nolasit_un_drukaj_otro_kolonnu(csv1):
        with open(csv1, 'r', encoding='utf-8') as r2:
            r1 = csv.reader(r2)
            
            print("Otrās kolonnas dati: ")
            for rinda in r1:
                if len(rinda) > 1:
                    print(rinda[1])


csv1 = '2uzd.csv'

nolasit_un_drukaj_otro_kolonnu(csv1)