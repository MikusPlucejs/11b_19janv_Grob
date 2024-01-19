# Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī. Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt"). Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas.
# Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu.

def ter3():

        lvv = input("Ievadiet savu vārdu: ")

        fn1 = 'lietotajs.txt'

        with open(fn1, 'w', encoding='utf-8') as fo1:
            fo1.write(lvv)
    
            print(f"Vārds '{lvv}' veiksmīgi ierakstīts failā '{fn1}'.")
ter3()
