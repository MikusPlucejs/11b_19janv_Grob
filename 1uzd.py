# Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā).

def p1(tkst):
    with open(tkst, 'r', encoding='utf-8') as p2:
            satr = p2.read()

            print(f"Faila saturs: {satr}")


tkst = '1uzd.txt'
p1(tkst)