ep1 = {22: 345, 55: 585, 58: 585, }

ep2 = {94: 484, 49: 484}

ep1.update(ep2)  # updates something new
ep1.pop(22)      # pop the introduced item
ep1.popitem()    # pop the las inserted item 
# del ep1         # delete the dictionary completely
del ep1[55]      # delete the introduced item
print(ep1)
