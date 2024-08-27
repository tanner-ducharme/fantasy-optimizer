from bs4 import BeautifulSoup
import requests
import csv

# URL to scrape QB projections from
url = 'https://www.fantasypros.com/nfl/projections/qb.php'

# Fetch the webpage content using requests
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Locate the table containing the data using its ID
    table = soup.find('table', {'id': 'data'})
    
    # Initialize a CSV file to store the scraped data
    with open('qb_projections.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write headers
        headers = ['Player', 'Team', 'ATT', 'CMP', 'YDS', 'TDS', 'INTS', 'Rushing_ATT', 'Rushing_YDS', 'Rushing_TDS', 'FL', 'FPTS']
        csvwriter.writerow(headers)
        
        # Iterate through each row in the table
        for row in table.find_all('tr')[2:]:  # Skip the header row
            data = []
            for cell in row.find_all('td'):
                data.append(cell.text.strip())
            
            # The player's name is inside a link within the first 'td' element
            player = row.find('td', class_='player-label').find('a', class_='player-name').text.strip()
            
            # The team abbreviation appears after the player's name
            team = row.find('td', class_='player-label').contents[-2].strip()
            
            # Replace the original player data with cleaned data
            data[0:1] = [player, team]
            
            # Write to CSV
            csvwriter.writerow(data)
            
    print("Data scraping and cleaning successful!")
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
