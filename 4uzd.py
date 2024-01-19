# Izveidot Python programmu, kur lietotājs ievada gan faila nosaukumu, gan faila formātu (paplašinājumu), un atkarībā no faila paplašinājuma tiek nolasīts faila saturs.
# Nolasītā informācija ir jāizdrukā terminālī. Ievērot iespejamās kļūdas! 

def rt5():

        fn1 = input("Ievadiet faila nosaukumu: ")

        fp1 = input("Ievadiet faila paplašinājumu (piemēram, txt): ")

        pfn1 = f"{fn1}.{fp1}"

        with open(pfn1, 'r', encoding='utf-8') as faila_objekts:
            saturs = faila_objekts.read()

            print(f"Faila '{pfn1}' saturs:")
            print(saturs)

rt5()