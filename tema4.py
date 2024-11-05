import random
cuvinte = ["python", "programare", "calculator", "date", "algoritm"]
cuvant_de_ghicit = random.choice(cuvinte)
progres = ["_" for _ in cuvant_de_ghicit]

incercari_ramase = 6
litere_incercate =[]

def afiseaza_progres():
    print("Cuvantul de ghicit: " + " ".join(progres))
    print(f"Incercari ramase: {incercari_ramase}")
    print(f"Litere incercate: {', '.join(litere_incercate)}")
    print()

while incercari_ramase > 0 and "_" in progres:
    afiseaza_progres()

    litera = input("Introdu o literă: ").lower()
    if len(litera) != 1 or not litera.isalpha():
        print("Eroare! Introdu o litera valida.\n")
        continue
    if litera in litere_incercate:
        print("Ai incercat aceasta litera. Alege o alta litera.\n")
        continue

        litere_incercate.append(litera)

    if litera in cuvant_de_ghicit:
        print(f"Litera '{litera}' este in cuvant.\n")

        for i in range(len(cuvant_de_ghicit)):
            if cuvant_de_ghicit[i] == litera:
                progres[i] = litera

    else:
        incercari_ramase -=1
        print(f"Litera '{litera}' nu este in cuvant. Incercari ramase: {incercari_ramase}\n")


if "_" not in progres:
    print(f"Felicitari! Ai ghicit cuvantul : {cuvant_de_ghicit}")
else:
    print(f"Ai pierdut. Cuvantul era: {cuvant_de_ghicit}")