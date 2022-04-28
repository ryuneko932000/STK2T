# Multiple File Reading
import matplotlib.pyplot as plt


UserString = input('> Write in the countries to be analyzed:\n')
UserList = UserString.replace(' ', '').split(',')

for country in UserList:
    CountryRead = open("{}.csv".format(country)).readlines()

    year = []
    population = []

    for l in CountryRead[1:]:
        l = l.replace('"', '')
        a = l.split(',')
        year.append(int(a[0]))
        population.append(float(a[1]))

    print(country, year, population)
    plt.plot(year, population)
    plt.show()



