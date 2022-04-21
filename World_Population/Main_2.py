# Multiple File Reading

Country_List = []
UserInput = input('> Write in the countries to be analyzed:\n')
UserInput.replace(' ', '')
UserInput.split(',')
Country_List.append(UserInput)

print(Country_List)

for i in Country_List:
    data = open(f'{i}.csv')


