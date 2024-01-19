# Izveidot Python programmu, kas nolasītu un izdrukātu trešās teksta faila rindas saturu.

def r4(tkst1):

    with open(tkst1, 'r', encoding='utf-8') as f34:
            rinds = f34.readlines()

            if len(rinds) >= 3:
                rinda3 = rinds[2].strip()
                print(f"Trešās rindas saturs: {rinda3}")
            else:
                print("Failā nav pietiekami daudz rindu.")


tkst1 = '1uzd.txt'
r4(tkst1)