listam = []
idk = ""
lapcsere = 0

while True:
    try:
        idk = input()
        if idk != "":
            listam = idk.split(",")
    except EOFError:
        break

for x in range(len(listam)):
    listam[x] = int(listam[x])
    if listam[x] < 0:
        listam[x] *= -1

tarol = [['B', 0, 0], ['C', 0, 0], ['A', listam[0], 3]]
print('A', end='')

counter = 1
for i in range(1, len(listam)):
    vanilyen = False
    for j in range(3):
        if listam[i] == tarol[j][1]:
            print("-", end="")
            tarol.append([tarol[j][0], listam[i], tarol[j][2]])
            tarol.pop(j)
            vanilyen = True
            break
    if not vanilyen:
        if tarol[0][2] > 0:
            if tarol[1][2] > 0:
                if tarol[2][2] > 0:
                    print("*", end="")
                    counter += 1
                else:
                    print(tarol[2][0], end="")
                    counter += 1
                    tarol.append([tarol[2][0], listam[i], 4])
                    tarol.pop(2)
            else:
                print(tarol[1][0], end="")
                counter += 1
                tarol.append([tarol[1][0], listam[i], 4])
                tarol.pop(1)
        else:
            print(tarol[0][0], end="")
            counter += 1
            tarol.append([tarol[0][0], listam[i], 4])
            tarol.pop(0)
    tarol[0][2] -= 1
    tarol[1][2] -= 1
    tarol[2][2] -= 1

print('\n', end="")
print(counter)
