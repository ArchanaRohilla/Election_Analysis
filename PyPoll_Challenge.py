# Add our dependencies.
import csv
import os

#  Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
   
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Initialize  a total vote counter.
total_votes = 0

# Create a county options list.
county_options = []

# Declare the empty dictionaty for the county votes.
county_votes ={}

# Declare the empty dictionary for the county votes turnout.
turnout={}

# County with largest turnout tracker.
largest_turnout = ""
largest_count = 0
largest_percentage = 0

# Create a candidates Options list.
candidate_options = []

# Declare the empty dictionary for candidate votes.
candidate_votes = {}

# Declare the candidate percenatge empty dictionary.
candidate_percentage = {}

# Winning candidate and the winning count tracker.
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# open the election results and read the file.
with open(file_to_load) as election_data:
    
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   
    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes +=1
        
        # Get the county name from each row.     
        county_name = row[1]               
        
        # If the county name does not match any existing county, add it in the list. 
        if county_name not in county_options:
            
            # Add name to the county list.
            county_options.append(county_name)
            
            # And begin tracking that county's voter count. 
            county_votes[county_name] = 0
            
        # Add a vote to that county's count.      
        county_votes[county_name]  += 1
        
        # Get the candidate name from each row.
        candidate_name = row[2]
         
        # If the candidate name does not match any existing candidate, add it in the list.            
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
           
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name]=0
        
        # Add a vote to that candidate's count.    
        candidate_votes[candidate_name] += 1
     
 
#Save results to our text file.
with open(file_to_save,"w") as txt_file:
    
    # Print the final vote count to the terminal.
    election_results = (
          f"\nElection Results"
          f"\n----------------------------------"
         f"\nTotal Votes : {total_votes:,}"
         f"\n----------------------------------\n")
    
    print(election_results, end="")
    
    # Save the final vote count to the txt file.
    txt_file.write(election_results)
    
    # Print the text 'County Votes:' in the terminal.
    print('\nCounty Votes:')
    
    # Write the text 'County Votes:' in the text file.
    txt_file.write('\nCounty Votes:')
    
    # Determine the turnout for each county by loopig through the counts.
    # Iterate through the county list.      
    for county_name in county_votes:
        
        # Retrive the vote count of a county.
        votes1 = county_votes[county_name]        
        
        # Calculate the turnout of each county.
        turnout[county_name]= int(county_votes[county_name])/ int(total_votes) * 100
        
        # Print each county name, their turnout and vote counts to the terminal.
        county_results = (f"\n{county_name}: {turnout[county_name]:.1f}% ({votes1:,})")
        
        # Print each candidate name, their percentage and vote counts to the terminal.              
        print(county_results)
        
        # Save the county name, their turnout and vote counts in the txt file.
        txt_file.write(county_results)
        
        if (votes1 > largest_count) and (turnout[county_name] > largest_percentage):
            # if true then set largest_count = votes1 and largest_percentage = turnout.
            largest_count = votes1
            largest_percentage = turnout[county_name]
            
            # Set the largest turnout equal to the county's name.
            largest_turnout = county_name
            
    # Print the county name with largest turnout to the terminal.
    largest_turnout_summary = (
        f"\n----------------------------------\n"
        f"Largest County Turnout: {largest_turnout}\n"
        f"----------------------------------\n")
    
    # Print  the county name with largest turnout to the terminal.
    print(largest_turnout_summary)
    
    # Save the county name with largest turnout to the text file.
    txt_file.write(largest_turnout_summary)    
                      
       
    # Determine the percentage of votes for each candidate by loopig through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        
        # Retrive vote count  of  a candidate.
        votes = candidate_votes[candidate]
        
        # Calculate  the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        
        # Print out each candidate's name , vote count and percentage of votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate name, their percentage and vote counts to the terminal.
        print(candidate_results)
        
        # Save the candidate name, their percentage and vote counts in the txt file.
        txt_file.write(candidate_results)
        
        # Determine the winning count and candidate.
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
            # if true then set winning_count = votes and winning_percentage = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            
            # And set the winning_candidate  equal to the candidate's name.
            winning_candidate = candidate
        
    #To do: print out each winning candidate , vote count and percentage of votes to the terminal.
    winning_candidate_summary = (
        f"----------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------\n")       
        
    # Print winning candidate's results to the terminal.
    print(winning_candidate_summary)
    
    # Save the Winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
   
    


    
    




