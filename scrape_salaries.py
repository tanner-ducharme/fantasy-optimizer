from bs4 import BeautifulSoup
import requests
import csv

# Function to clean player data
def clean_player_data(player_data):
    player, info = player_data.split(' (')
    team, position = info.rstrip(')').split(' - ')
    return player, team, position

# URL to scrape from
url = 'https://www.fantasypros.com/daily-fantasy/nfl/fanduel-salary-changes.php'

# Fetch the webpage content using requests
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate the table containing the data
    table = soup.find('table', {'id': 'data-table'})
    
    # Initialize a CSV file to store the scraped data
    with open('fanduel_salaries_cleaned.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write headers
        headers = ['ECR', 'Player', 'Team', 'Position', 'Kickoff', 'Opp', 'This Week', 'Last Week', 'Difference']
        csvwriter.writerow(headers)
        
        # Iterate through each row in the table
        for row in table.find_all('tr')[1:]:  # Skip the header row
            data = []
            for cell in row.find_all('td'):
                data.append(cell.text.strip())
            
            # Clean the player data
            player, team, position = clean_player_data(data[1])
            
            # Replace the original player data with cleaned data
            data[1:2] = [player, team, position]
            
            # Write to CSV
            csvwriter.writerow(data)
            
    print("Data scraping and cleaning successful!")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
