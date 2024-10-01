myfavfruits = int(input("pila kabook akung ganahan:"))
namesofmyfruits = []

for i in range(myfavfruits):
    myfavfruits = input("Enter name of fruits")
    namesofmyfruits.append(myfavfruits)

print(namesofmyfruits)

for data in myfavfruits:
    if data == "banana":
        break
    elif data == "apple":
        print ("happy eating")

        



