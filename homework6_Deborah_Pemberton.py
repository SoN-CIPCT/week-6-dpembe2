web_users = ["racerlectern", "pumpkinsmusic", "illustratesnow", "brashlethal", "princessdone"]
new_users = ["pumpkinsmusic", "whisperedinject", "bookshelfdiorite", "princessdone", "regardingmerely"]
for new_user in new_users:
    if new_user in web_users:
        print(f"Sorry, the username '{new_user}' is already taken.")
    else:
        print(f"The username '{new_user}' is available.")


