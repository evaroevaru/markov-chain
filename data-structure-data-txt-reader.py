a = 0
b = 0
c = 0
d = 0
e = 0
dct = {"A":a,"B":b,"C":c,"D":d,"E":e}

with open('data_structure_data.txt', 'r') as file:
    for line in file:
        if "A" in line:
            a = a+1
        elif "B" in line:
            b = b+1
        elif "C" in line:
            c = c+1
        elif "D" in line:
            d = d+1
        elif "E" in line:
            e = e+1
dct["A"] = str(a)
dct["B"] = str(b)
dct["C"] = str(c)
dct["D"] = str(d)
dct["E"] = str(e)

for key,value in dct.items():
    print(f"{key}: {value}")




