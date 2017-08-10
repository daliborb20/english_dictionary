import json
import difflib
dict='data.json'


def recnik():
    podaci=json.load(open(dict,'r'))
    rec=input("Unesite trazenu rec: ")
    rec=rec.lower()
    priblizno=difflib.get_close_matches(rec, podaci)
    duzina=len(priblizno)
    if rec in podaci:
        print(podaci[rec])
    else:
        print("Trazena rec nije pronadjena.", "Pronasli smo", duzina, " reci. ","Da li ste mislili na ", priblizno)
        k=int(input("Broj za trazenu rec:  "))
        p=priblizno[k-1]        
        if p in podaci:
            a=priblizno[k-1]
            print(podaci[a])


        else:
            print("Trazena rec nije pronadjena")


recnik()
