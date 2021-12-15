from os import remove


soll_list = []
scan_list = []
notWritten = []

file = open("soll_bestand.txt", "r")
    
for x in file:
    soll_list.append(x)

bestand = open("scan_bestand.txt", "r")
    
for x in bestand:
    scan_list.append(x)
    
file.close()
bestand.close()

for x in scan_list:
    if x in  soll_list:
        soll_list.remove(x)
    else:
        notWritten.append(x)    

print("The missing Simcards are \n")
for x in soll_list:
    print(x)
    
print("The Sim card wich are in Stock but actually arent written in stock:")
print(notWritten)
input("\n press something to end Programm")
