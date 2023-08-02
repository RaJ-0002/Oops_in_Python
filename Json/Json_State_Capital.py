import json

indian_states_and_capitals = {
    "Telangana": "Hyderabad",
    "Arunachal Pradesh": "Itanagar",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Haryana": "Chandigarh",
    "Karnataka": "Bengaluru"
}

with open("states_and_capitals.json", "w") as file:
    json.dump(indian_states_and_capitals, file,indent=4)

print("Data has been written to states_and_capitals.json")
