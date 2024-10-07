# 10.2.py
# Reading CSV

from urllib.request import urlopen
from io import StringIO

import csv

data = (
    urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv")
    .read()
    .decode("ASCII", "ignore")
)

data_file = StringIO(data)
csv_reader = csv.reader(data_file)

# ['Name', 'Year']
# ["Monty Python's Flying Circus", '1970']
# ['Another Monty Python Record', '1971']
# ["Monty Python's Previous Record", '1972']
for row in csv_reader:
    print(row)

data_file = StringIO(data)
csv_dict_reader = csv.DictReader(data_file)

# ['Name', 'Year']
print(csv_dict_reader.fieldnames)

# {"Name": "Monty Python's Flying Circus", "Year": "1970"}
# {"Name": "Another Monty Python Record", "Year": "1971"}
# {"Name": "Monty Python's Previous Record", "Year": "1972"}
for row in csv_dict_reader:
    print(row)
