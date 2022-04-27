# Multiple File Reading

UserString = input('> Write in the countries to be analyzed:\n')
UserList = UserString.replace(' ', '').split(',')

for country in UserList:
    data = open("{}.csv".format(country))
    CountryRead = data.readlines()

    year = []
    population = []

    for l in CountryRead[1:]:
        l = l.replace('"', '')
        a = l.split(',')
        year.append(int(a[0]))
        population.append(float(a[1]))
    
    print(year)
    print(population)



