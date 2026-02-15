web_users = ["racerlectern", "pumpkinsmusic", "illustratesnow", "brashlethal", "princessdone"]
new_users = ["pumpkinsmusic", "whisperedinject", "bookshelfdiorite", "princessdone", "regardingmerely"]
for new_users in new_users:
    if new_users in web_users:
        print(f"This user name '{new_users}' is already in use. Please choose a different username.")
    else:
        print(f"The username '{new_users}' is available.")


