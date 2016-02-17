# -*- coding: utf-8 -*-

"""
Сделайте простую базу данных.
При первом запуске программы, она создает файл pickle с данными.
При последующих открывает этот файл и выводит на экран содержимое.

3.* Реализовать поиск/фильтрацию в базе данных - то есть вывод по условию.
"""

import pickle
import os

data = {
    1: {"Alfreds Futterkiste": ["Maria Anders", "Obere Str. 57", "Berlin", "12209", "Germany"]},
    2: {"Ana Trujillo, Emparedados y helados": ["Ana Trujillo", "Avda. de la Constitución 2222", "México D.F.", "5021",
                                                "Mexico"]},
    3: {"Antonio Moreno Taquería": ["Antonio Moreno", "Mataderos 2312", "México D.F.", "5023", "Mexico"]},
    4: {"Around the Horn": ["Thomas Hardy"    "120 Hanover Sq.", "London", "WA1 1DP", "UK"]},
    5: {"Berglunds snabbköp": ["Christina Berglund", "Berguvsvägen 8", "Luleå", "S-958 22", "Sweden"]},
    6: {"Blauer See Delikatessen": ["Hanna Moos", "Forsterstr. 57", "Mannheim", "68306", "Germany"]},
    7: {"Blondel père et fils": ["Frédérique Citeaux", "24, place Kléber", "Strasbourg", "67000", "France"]},
    8: {"Bólido Comidas preparadas": ["Martín Sommer", "C/ Araquil, 67", "Madrid", "28023", "Spain"]},
    9: {"Bon app\'": ["Laurence Lebihans", "12, rue des Bouchers", "Marseille", "13008", "France"]},
    10: {"Bottom-Dollar Marketse": ["Elizabeth Lincoln", "23 Tsawassen Blvd.", "Tsawassen", "T2F 8M4", "Canada"]},
    11: {"B's Beverages": ["Victoria Ashworth", "Fauntleroy Circus", "London", "EC2 5NT", "UK"]},
    12: {"Cactus Comidas para llevar": ["Patricio Simpson", "Cerrito 333", "Buenos Aires", "1010", "Argentina"]},
    13: {"Centro comercial Moctezuma": ["Francisco Chang", "Sierras de Granada 9993", "México D.F.", "5022", "Mexico"]},
    14: {"Chop-suey Chinese": ["Yang Wang", "Hauptstr. 29", "Bern", "3012", "Switzerland"]},
    15: {"Comércio Mineiro": ["Pedro Afonso", "Av. dos Lusíadas, 23", "São Paulo", "05432-043", "Brazil"]},
    16: {"Consolidated Holdings": ["Elizabeth Brown", "Berkeley Gardens 12 Brewery", "London", "WX1 6LT", "UK"]},
    17: {"Drachenblut Delikatessend": ["Sven Ottlieb", "Walserweg 21", "Aachen", "52066", "Germany"]},
    18: {"Du monde entier": ["Janine Labrune", "67, rue des Cinquante Otages", "Nantes", "44000", "France"]},
    19: {"Eastern Connection": ["Ann Devon", "35 King George", "London", "WX3 6FW", "UK"]},
    20: {"Ernst Handel": ["Roland Mendel", "Kirchgasse 6", "Graz", "8010", "Austria"]},
    }

dataset = 'lesson3/data.pickle'
data_new = None
if not os.path.exists(dataset):
    with open('lesson3/data.pickle', 'wb') as f:
        pickle.dump(data, f)
    print("Status: Data was dumped to file")
else:
    with open(dataset, 'rb') as f:
        data_new = pickle.load(f)

    print("Database file contents:", "\n", data_new)

EnteredID = 16

for CustomerID, CustomerDetails in data_new.items():
    if CustomerID == EnteredID:
        for CustomerName, ContactData in CustomerDetails.items():
            print("CustomerName:", CustomerName)
            print("ContactPerson:", ContactData[0])
            print("Address:", ContactData[1])
            print("City:", ContactData[2])
            print("Country:", ContactData[4])