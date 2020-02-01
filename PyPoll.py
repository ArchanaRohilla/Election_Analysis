# Add our dependencies.
import csv
import os
#  Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
   
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize  a total vote counter.
total_votes = 0

# Candidates Options
candidate_options = []

# 1. Declare the empty dictionary
candidate_votes = {}

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
    
    # Print each row in  the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in  candidate_options:
            candidate_options.append(candidate_name)
            
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            
        # Add one vote to that candidates vote count.
        candidate_votes[candidate_name] += 1
        
# Determine the percentage of votes for each candidate by loopig through the counts.
# 1. Iterate through the candidate list.
for candidate in candidate_votes:
    # 2. Retrive vote count  of  a candidate.
    votes = candidate_votes[candidate]
    # 3. Calculate  the percentage of votes.
    vote_percentage= int(votes) / int(total_votes) * 100
    
    #To do: print out each candidate's name , vote count and percentage of votes to the terminal.
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    
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
    f"------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count:,}\n"
    f"Winning percentage: {winning_percentage:.1f}%\n"
    f"------------------------------\n")       
print(winning_candidate_summary)
        
   
    


    
    


