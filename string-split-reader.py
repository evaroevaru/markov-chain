a = {"1":0, "2":0, "3":0}
b = {"1":0, "2":0, "3":0}
c = {"1":0, "2":0, "3":0}
d = []
e = 0
f = 0
g = 0
with open('string_split.txt', 'r') as file:
    for line in file:
        d = line.split("*")
        if d[0]=='1':
            e = e+1
            if '1' in d[1]:
                a["1"]=a["1"]+1
            if '2' in d[1]:
                a["2"]=a["2"]+1
            if '3' in d[1]:
                a["3"]=a["3"]+1
        if d[0]=='2':
            f = f+1
            if '1' in d[1]:
                b["1"]=b["1"]+1
            if '2' in d[1]:
                b["2"]=b["2"]+1
            if '3' in d[1]:
                b["3"]=b["3"]+1
        if d[0]=='3':
            g = g+1
            if '1' in d[1]:
                c["1"]=c["1"]+1
            if '2' in d[1]:
                c["2"]=c["2"]+1
            if '3' in d[1]:
                c["3"]=c["3"]+1
a["1"] = round(a["1"]/e,3)
a["2"] = round(a["2"]/e,3)
a["3"] = round(a["3"]/e,3)
b["1"] = round(b["1"]/f,3)
b["2"] = round(b["2"]/f,3)
b["3"] = round(b["3"]/f,3)
c["1"] = round(c["1"]/g,3)
c["2"] = round(c["2"]/g,3)
c["3"] = round(c["3"]/g,3)
print(f'1: {a}')
print(f'2: {b}')
print(f'3: {c}')


