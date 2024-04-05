with open("cesty.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

cesty = []
cesty_2 = []


for line in lines:

    cesty.append(line.split())

    for number in line.split():

        x = int(number)

        if x != 0:
            cesty_2.append(int(number))


for i in range(len(cesty_2)):

    for p in range(len(cesty_2)-1):

        if cesty_2[i] > cesty_2[p]:

            cesty_2[i], cesty_2[p] = cesty_2[p], cesty_2[i]

vypis = ""

for riadok in cesty:

    vypis += "\n"

    for cislo in riadok:

        vypis += (cislo)
        vypis += " "

print(f"{vypis}\n")
print(f"Najdlhsia cesta je {cesty_2[0]}\nNajkratsia cesta je {cesty_2[-1]}")



