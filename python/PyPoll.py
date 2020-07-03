# Add our dependencies.
import csv
import os
#  Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
   
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# 1. Initialize  a total vote counter.
total_votes = 0

# County options
county_options = []

# Declare the empty dictionaty for the county votes.
county_votes ={}

turnout={}

# Candidates Options
candidate_options = []

# 1. Declare the empty dictionary for candidate votes.
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
        
             
    #     county_name = row[1]               
         
    #     if county_name not in county_options:
    #         # Add name to the county dictionary
    #         county_options.append(county_name)
             
    #         county_votes[county_name] = 0
            
    #     # Increment the county votes by 1.     
    #     county_votes[county_name]  += 1
        
        
    # for county_name in county_votes:
    #     # Calculate the turnout of each county.
    #     turnout[county_name]= int(county_votes[county_name])/ int(total_votes) * 100
    
       
    # for candidate_name in candidate_votes:
    #     # Calculate the vote percentage of each candidate.
    #     candidate_percentage[candidate_name] = candidate_votes[candidate_name]/total_votes * 100
    
    # # Find out the county with largest turnout.
    # largest_turnout=max(turnout, key=turnout.get)
    
    # print(turnout) 
    # print(candidate_percentage)  
    # print(f"{largest_turnout} has largest turnout of {turnout[largest_turnout]: .1f}%")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     for row in file_reader:
#         county_name = row[1]
        
#         if county_name not in county_options:
#             county_options.append(county_name)

# with open(file_to_load) as election_data:  
#     file_reader = csv.reader(election_data) 
          
#     for county_name in county_options:
#         election_data.seek(0)
#         county_votes[county_name]=0
#         for row in file_reader:
#             if county_name in row[1]:
#                 county_votes[county_name] += 1
                
#                 total_votes=total_votes+ 1
    
    
#     for key in county_votes:            
#         turnout[key]=county_votes[key]/total_votes * 100
        
#     print(f"{county_votes}")  
#     print(f"{total_votes}") 
#     #print(f"{turnout} ")  
#     largest_turnout=max(turnout,key=turnout.get)
#     print(f"Largest turnout: {largest_turnout}, {turnout[largest_turnout]: .1f} %")
#     for key in turnout:
#         print(f"{key} :  {turnout[key]:.1f}%  (Num of Votes {county_votes[key]})")

    

        
            
        
    
    
 
#Save results to our text file.
with open(file_to_save,"w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
          f"\nElection Results"
          f"\n---------------------------"
         f"\nTotal votes : {total_votes:,}"
         f"\n----------------------------\n")
    
    print(election_results, end="")
    
    # Save the funal vote count to the txt file.
    txt_file.write(election_results)
          
        
    # Determine the percentage of votes for each candidate by loopig through the counts.
    # 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrive vote count  of  a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate  the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        
        #To do: print out each candidate's name , vote count and percentage of votes to the terminal.
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # print each candidate name, their percentage and vote counts to the terminal.
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
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote count: {winning_count:,}\n"
        f"Winning percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")       
        
    # Print winning candidate's results to the terminal.
    print(winning_candidate_summary)
    
    # Save the Winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)
   
    


    
    


