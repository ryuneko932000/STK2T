# Import and read CSV file: 

# Open one country
fid = input('> What country should be analyzed?\n')
data = open("{}.csv".format(fid))

# Read lines of document
Country = data.readlines()

# Create empty lists
year = []
population = []

# For every country in the lines of our document, replace the character " for a ''
# then split the line into different variables by every comma 
# Save data in first column of line into list year 
# Save data from second column of line into list population
for l in Country[1:]:
    l = l.replace('"', '')
    a = l.split(',')
    year.append(int(a[0]))
    population.append(float(a[1]))

print(year)
print(population)


