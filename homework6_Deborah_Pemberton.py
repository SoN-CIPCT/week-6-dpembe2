web_users = ["racerlectern", "pumpkinsmusic", "illustratesnow", "brashlethal", "princessdone"]
new_users = ["pumpkinsmusic", "whisperedinject", "bookshelfdiorite", "princessdone", "regardingmerely"]
for new_users in new_users:
    if new_users in web_users:
        print(f"This user name '{new_users}' is already in use. Please choose a different username.")
    else:
        print(f"The username '{new_users}' is available.")
cities = {}
cities['Seattle'] = {'country': 'United States','population': 816600,'fact': 'Seattle is home to Amazon and Starbucks.'} 
cities['London'] = {'country': 'United Kingdom','population': 9100000,'fact': 'London was founded by the Romans in AD 47.'}
cities['Rome'] = {'country': 'Italy','population': 2750000,'fact': 'Rome was the first city in the world to reach a population of 1 million people.'}
for city, city_info in cities.items():
    print(f"\nCity: {city}")
    print(f"\tCountry: {city_info['country']}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}")
