print("Hello World")
counties=["Arapahoe","Denver","Jefferson"]
if counties[1] =='Denver':
    print(counties[1])
    if counties[0] != 'Jefferson':
        print(counties[2])
    
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

if "Arapahoe" and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not the list of counties.")
    
if "Arapahoe" or "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not the list of counties.")  
    
for county in counties:
    print(county)
    
for i in range(len(counties)):
    print(counties[i])
    
counties_tuple = ["Arapahoe","Denver","Jefferson"]

for i in range(len(counties_tuple)):
    print(counties_tuple[i])
    

    
for county in counties_tuple:
    print(county)
    

    
for county in counties_tuple:
    print(county)
    
counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for county in counties_dict:
    print(county)
    
for county in counties_dict.keys():
    print(county)
    
for county in counties_dict.keys():
    print(county)
    
for voters in counties_dict.values():
    print(voters)
    

for county in counties_dict:
    print(counties_dict[county])
    
for county in counties_dict:
    print(counties_dict.get(county))
    
for county, voters in counties_dict.items():
    print(county,voters)
    
for county, voters in counties_dict.items():
    print((county) + " county has " + str(voters) + " registered voters.")
 
voting_data= [{"county":"Arapahoe","registered_voters":422829},
              {"county":"Denver","registered_voters":463353},
              {"county":"Jefferson","registered_voters": 432438}]   

for county_dict in voting_data:
    print(county_dict)
    
for i in range(len(voting_data)):
    print(voting_data[i])
    
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
        
for county_dict in voting_data:
    print(county_dict['registered_voters'])
    
for county_dict in voting_data:
    print(county_dict['county'])
    
counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}."
    f"You received {candidate_votes / total_votes *100 : .2f}% of the total votes.")

print(message_to_candidate)





    

    
