from pprint import pprint

import requests

def searching_most_intelligent_hero(mylist):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    # response = requests.get(url)
    data = requests.get(url).json()
    heroes = {}
    searsh_heroes = []
    for line in data:
        heroes[line['name']] = int(line['powerstats']['intelligence'])
    intelligence_heroes = sorted(heroes.items(), key=lambda x: x[1])
    for name in intelligence_heroes:
        for y in mylist:
            if name[0] == y:
                searsh_heroes.append({name[0]: name[1]})
    pprint(f'Самый умный герой - {"".join(list(searsh_heroes[-1].keys()))}. '
           f'Его интеллект равен {str(list((searsh_heroes[-1].values()))).strip("[]")}.')

herous_list = ['Hulk', 'Captain America', 'Thanos']

if __name__ == '__main__':
    searching_most_intelligent_hero(herous_list)

