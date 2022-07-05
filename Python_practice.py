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
     


# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_names = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
county_voter_turnout = 0

# Get the candidate name from each row.
candidate_name = row[2]

# 3: Extract the county name from each row.
county_name = row[1]
      