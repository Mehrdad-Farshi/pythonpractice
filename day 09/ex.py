travel_log=[
    {
        'country':'France',
        'visits':12,
        'cities':['Paris','Lille','Dijon']

    },
    {
        'country':'Germany',
        'visits':5,
        'cities':['Berlin','Hamburg','Stuttgart']
    },
]

# a functon that allow adding new countries to travel_log 

def add_new_country(country_name,visits,cities):
    add= {
        'country':country_name,
        'visits':visits,
        'cities':cities,}
    travel_log.append(add)

add_new_country('russia',2,['Moscow','kazan','samara'])

print(travel_log)