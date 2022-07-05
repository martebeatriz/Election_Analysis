# Analysis of Election Audit 
## Overview of Election Audit: 
The election commission has requested the following additional data to complete the audit:
- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

## Election-Audit Results: 
### Total votes cast: 369,711
### Breakdown by county:
Jefferson County: 
- Votes cast: 38,855
- Percentage of total votes cast: 10.5%

Denver County:
- Votes cast: 306,055
- Percentage of total votes cast: 82.8%

Arapahoe County:
- Votes cast: 24,801
- Percentage of total votes cast: 6.7%

### Largest County Turnout: Denver 

### Breakdown of votes received by each candidate 
- Charles Casper Stockham: 23.0% (85,213 votes)
- Diana DeGette: 73.8% (272,892 votes)
- Raymon Anthony Doane: 3.1% (11,606 votes)

### Winner:
Diana DeGette </br>
272,892 Votes </br>
73.8% of Total Votes </br>

<img width="402" alt="election_analysis screenshot" src="https://user-images.githubusercontent.com/107375554/177226688-ac334cf9-56d6-42f7-8815-8f30b93089eb.png">


## Election-Audit Summary: 
This script is highly adaptive. The variables "candidate_name" is assigned to the 3rd column of this specific data which lists all the candidates. The variable "county_name" is assigned to the 2nd column of this data which lists the county names. If a difference data source is to be analyzed, the indexes of those two variables can be changed to align with the new data's columns.   

As long as the correct columns are correctly identified in the data, the script will be able to return the candidate names, county names, and their respective votes and percentages of votes.

Most importantly, the user would also need to change the “file_to_load” and “file_to_save“ variables so that the data used will be properly identified and so that a new text file is created and to hold the new data. 



