import json
import matplotlib.pyplot as plt
from country_code import get_country_code


filename = 'learn_matplotlib/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

china_pop = {}
year = []
population = []
for pop_dict in pop_data:
    if pop_dict["Country Name"] == 'China':
        year.append(int(pop_dict["Year"]))
        population.append(int(pop_dict["Value"]))
        china_pop[year[-1]] = population[-1]

#print(china_pop)
plt.plot(year, population)
plt.savefig('learn_matplotlib/china.png')
plt.show()