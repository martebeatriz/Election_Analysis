#print("Hello World")

#counties = ["Arapahoe","Denver","Jefferson"]

#for county in counties:
    #print(county)

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for county, voters in counties_dict.items():
    #print(str(county) + " county has " + str(voters) + " registered voters.")

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                #{"county":"Denver", "registered_voters": 463353},
                #{"county":"Jefferson", "registered_voters": 432438}]

#for county_dict in voting_data:

     #print(county_dict['registered_voters'])

#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for countyVoters in voting_data:
    print(f"{countyVoters['county']} county has {countyVoters['registered_voters']} registered voters.")
     
        