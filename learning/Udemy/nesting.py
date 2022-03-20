# capitols = {
#     'France': 'Paris',
#     'Germanry': 'Berlin'
# }

# travel_log ={ 
#     'France': ['Paris', 'Dijon']
# }

# print(travel_log['France'][1])

# travel_log2 = {
#     'France': {
#         'cities':['Paris', 'Dijon', 'Lille'],
#         'attractions': ['Eifle Tower']
#     }
# }

# print(travel_log2['France']['cities'])

travel_log = [
    {
        'country': 'France',
        'visits': 12,
        'cities': ['Paris', 'Lille', 'Dijon']
    },
    {
        'country': 'Germany',
        'visits': 5,
        'cities': ['Berlin', 'Hamburg', 'Stuttgart']
    }
]

def add_new_country(country, visits, cities):
   travel_log.append({'country': country, 'visits': visits, 'cities': cities})

add_new_country('Russia', 2, ['Moscow', 'St. Petersburg'])

print(f'''
You\'ve visited {travel_log[2]['country']} {travel_log[2]['visits']} times.
You\'ve beenn to {travel_log[2]['cities'][0]}
''')