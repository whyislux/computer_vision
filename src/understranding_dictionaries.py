info_charly = {"name": 'Charly',
               "age": 33,
               "address": "18 O.R.",
               "Salary":25500.05,
               "married":True}

print(info_charly["name"])
print(info_charly.keys())
print(info_charly.values())

for key,value in info_charly.items():
    print(key,value)