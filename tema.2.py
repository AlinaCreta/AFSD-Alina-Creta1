articol = "Comisia Electorală Centrală din Republica Moldova a anunțat că a încheiat de numărat voturile pentru alegerile prezidențiale din 2024"

lungime = len(articol)
punct_mijloc = lungime // 2
prima_parte = articol[:punct_mijloc]
a_doua_parte = articol[punct_mijloc:]

prima_parte = prima_parte.upper()
prima_parte = prima_parte.strip()

a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize()
import string
a_doua_parte = a_doua_parte.translate(str.maketrans('', '', string.punctuation))

rezultat = prima_parte + ' ' + a_doua_parte

print(rezultat)