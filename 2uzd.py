# Izveidot Python programmu, kas nolasītu un izdrukātu tikai otrās kolonnas datus no CSV faila.

import csv

def fr3(csv1):
        with open(csv1, 'r', encoding='utf-8') as r2:
            r1 = csv.reader(r2)
            
            print("Otrās kolonnas dati: ")
            for rinda in r1:
                    print(rinda[2])
csv1 = '2uzd.csv'
fr3(csv1)