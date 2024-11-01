meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []

print( studenti[0] + " a comandat " + comenzi[0])
print( studenti[1] + " a comandat " + comenzi[1])
print( studenti[2] + " a comandat " + comenzi[2])
print( studenti[3] + " a comandat " + comenzi[3])
print( studenti[4] + " a comandat " + comenzi[4])

studenti.pop(0)
print(studenti)
tavi.pop()
print(tavi)
comenzi.pop(0)
print(comenzi)

studenti.pop(0)
print(studenti)
tavi.pop()
print(tavi)
comenzi.pop(0)
print(comenzi)

studenti.pop(0)
print(studenti)
tavi.pop()
print(tavi)
comenzi.pop(0)
print(comenzi)

studenti.pop(0)
print(studenti)
tavi.pop()
print(tavi)
comenzi.pop(0)
print(comenzi)

studenti.pop(0)
print(studenti)
tavi.pop()
print(tavi)
comenzi.pop(0)
print(comenzi)




