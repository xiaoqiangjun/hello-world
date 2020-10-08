import json
from country_code import get_country_code
import pygal.maps.world
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS


filename = 'learn_matplotlib/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for pop_dict in pop_data:
    if pop_dict["Year"] == '2010':
        country_name = pop_dict["Country Name"]
        population = int(float(pop_dict["Value"]))
        code = get_country_code(country_name)
        if code:
            if population < 10000000:
                cc_pop1[code] = population
            elif population < 1000000000:
                cc_pop2[code] = population
            else:
                cc_pop3[code] = population

print(len(cc_pop1), len(cc_pop2), len(cc_pop3))
wm_style = RS('#336699', base=LCS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = '世界人口地图（2010）'
wm.add('0-10m', cc_pop1)
wm.add('10m-1bn', cc_pop2)
wm.add('>1bn', cc_pop3)

wm.render_to_file('learn_matplotlib/worldmap.svg')