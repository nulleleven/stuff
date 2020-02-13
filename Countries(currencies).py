import re

doc = open("C:\\Users\\bbarker\\Desktop\\prices.txt", "r").read()
docArray = doc.split('},')
currCountries = {"USD":'"',"GBP":'"',"EUR":'"'}

for i in range(len(docArray)):
    country = re.search(r'(?<="CountryCode": ")\w+', docArray[i])
    currency = re.search(r'(?<="Currency": ")\w+', docArray[i])
    current = currCountries[str(currency[0])]
    if str(country[0]) not in current:
        currCountries[currency[0]] += country[0] + ' '

for kind in currCountries:
    currCountries[kind] = currCountries[kind].strip().replace(" ", '", "') + '"'
    print(kind + ': ' + currCountries[kind])
