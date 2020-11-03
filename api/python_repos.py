import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

url =  'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code :" , r.status_code)
response_dict = r.json()

print("total repos: " , response_dict['total_count'])

repo_dicts = response_dict['items']
print('repos returned: ' , len(repo_dicts))

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    plot_dict = {
        'value' : repo_dict['stargazers_count'],
        'label' : repo_dict['description'],
        'xlink' : str(repo_dict['html_url']),
    }
    plot_dicts.append(plot_dict)

my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45 
my_config.show_legend = False
my_config.title_font_size = 24 
my_config.label_font_size = 14 
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Github上星星最多的Python项目（20201008）'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('api/python_repos.svg')