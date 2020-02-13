global course
course = input("Course: ")

def MakeBody(countries, curr, price):
    priceUpdt = '"CountryCodes":[{}],"LabMaterialNumber":"{}","Price":{},"Currency":"{}","LearningPartnerType":"null"'
    priceUpdt = priceUpdt.format(countries, course, price, curr)
    return priceUpdt

usdCo = '"AG", "AI", "AN", "AR", "AU", "AW", "BB", "BD", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT", "BZ", "CA", "CL", "CN", "CO", "CR", "CW", "DM", "DO", "EC", "FJ", "GD", "GP", "GS", "GT", "GU", "GY", "HK", "HN", "HT", "ID", "IN", "JM", "JP", "KH", "KN", "KR", "KY", "LA", "LC", "LK", "MM", "MO", "MQ", "MS", "MV", "MX", "MY", "NC", "NI", "NP", "NZ", "PA", "PE", "PG", "PH", "PR", "PY", "SB", "SG", "SR", "SV", "SX", "TC", "TH", "TT", "TW", "US", "UY", "VC", "VE", "VG", "VI", "VN", "VU"'
gdpCo = '"GB", "GG", "JE"'
eurCo = '"AD", "AE", "AF", "AL", "AM", "AO", "AT", "AZ", "BA", "BE", "BF", "BG", "BH", "BI", "BJ", "BW", "BY", "CD", "CG", "CH", "CI", "CM", "CV", "CY", "CZ", "DE", "DJ", "DK", "DZ", "EE", "EG", "ER", "ES", "ET", "FI", "FR", "GA", "GE", "GF", "GH", "GI", "GL", "GM", "GN", "GR", "HR", "HU", "IC", "IE", "IL", "IQ", "IS", "IT", "JO", "KE", "KG", "KW", "KZ", "LB", "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MD", "ME", "MG", "MK", "ML", "MN", "MT", "MU", "MW", "MZ", "NA", "NE", "NG", "NL", "NO", "OM", "PF", "PK", "PL", "PT", "QA", "RE", "RO", "RS", "RU", "RW", "SA", "SC", "SE", "SI", "SK", "SL", "SN", "SY", "SZ", "TG", "TJ", "TM", "TN", "TR", "TZ", "UA", "UG", "UZ", "XK", "YE", "ZA", "ZM", "ZW"'
cos = [usdCo, gdpCo, eurCo]

currs = ["USD", "GDP", "EUR"]
costs = []
costs.append(input("USD: "))
costs.append(input("GBP: "))
costs.append(input("EUR: "))

prices = ""

for i in range(len(costs)):
    prices += '{}:'.format(i)+'{'+MakeBody(cos[i],currs[i],costs[i])+'}\n'

outfile = open('C:\\Users\\bbarker\\Documents\\Countries-Costs.txt', 'w')
outfile.write(prices)
outfile.close()
