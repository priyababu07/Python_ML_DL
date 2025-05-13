_3d = []

for i in range(3):  
    layer = []
    for j in range(4): 
        row = []
        for k in range(6): 
            row.append("*")
        layer.append(row)
    _3d.append(layer)


for layer in _3d:
    for row in layer:
        print(row)
    print()
