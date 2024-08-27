from bs4 import BeautifulSoup
import requests
import csv
from argparse import ArgumentParser

# Function for scraping Quarterback data
def scrape_qb_data(table):
    headers = ['Player', 'Team', 'ATT', 'CMP', 'YDS', 'TDS', 'INTS', 'Rushing_ATT', 'Rushing_YDS', 'Rushing_TDS', 'FL', 'FPTS']
    rows = []
    for row in table.find_all('tr')[2:]:  # Skip the header rows
        data = []
        for cell in row.find_all('td'):
            data.append(cell.text.strip())

        # Extract the player's name and team
        player = row.find('td', class_='player-label').find('a', class_='player-name').text.strip()
        team = row.find('td', class_='player-label').contents[-2].strip()

        # Replace the original player data with the cleaned data
        data[0:1] = [player, team]

        # Add the cleaned row to the list of rows
        rows.append(data)

    return {'headers': headers, 'rows': rows}


# Function for scraping Running Back data
def scrape_rb_data(table):
    headers = ['Player', 'Team', 'Rushing_ATT', 'Rushing_YDS', 'Rushing_TDS', 'Receiving_REC', 'Receiving_YDS', 'Receiving_TDS', 'FL', 'FPTS']
    rows = []
    for row in table.find_all('tr')[2:]:  # Skip the header rows
        data = []
        for cell in row.find_all('td'):
            data.append(cell.text.strip())

        # Extract the player's name and team
        player = row.find('td', class_='player-label').find('a', class_='player-name').text.strip()
        team = row.find('td', class_='player-label').contents[-2].strip()

        # Replace the original player data with the cleaned data
        data[0:1] = [player, team]

        # Add the cleaned row to the list of rows
        rows.append(data)

    return {'headers': headers, 'rows': rows}


# Function for scraping Wide Receiver data
def scrape_wr_data(table):
    headers = ['Player', 'Team', 'Receiving_REC', 'Receiving_YDS', 'Receiving_TDS', 'Rushing_ATT', 'Rushing_YDS', 'Rushing_TDS', 'FL', 'FPTS']
    rows = []
    for row in table.find_all('tr')[2:]:  # Skip the header rows
        data = []
        for cell in row.find_all('td'):
            data.append(cell.text.strip())

        # Extract the player's name and team
        player = row.find('td', class_='player-label').find('a', class_='player-name').text.strip()
        team = row.find('td', class_='player-label').contents[-2].strip()

        # Replace the original player data with the cleaned data
        data[0:1] = [player, team]

        # Add the cleaned row to the list of rows
        rows.append(data)

    return {'headers': headers, 'rows': rows}


# Function for scraping Tight End data
def scrape_te_data(table):
    headers = ['Player', 'Team', 'Receiving_REC', 'Receiving_YDS', 'Receiving_TDS', 'FL', 'FPTS']
    rows = []
    for row in table.find_all('tr')[2:]:  # Skip the header rows
        data = []
        for cell in row.find_all('td'):
            data.append(cell.text.strip())

        # Extract the player's name and team
        player = row.find('td', class_='player-label').find('a', class_='player-name').text.strip()
        team = row.find('td', class_='player-label').contents[-2].strip()

        # Replace the original player data with the cleaned data
        data[0:1] = [player, team]

        # Add the cleaned row to the list of rows
        rows.append(data)

    return {'headers': headers, 'rows': rows}


# Function for scraping Flex data
def scrape_flex_data(table):
    headers = ['Player', 'Team', 'POS', 'Rushing_ATT', 'Rushing_YDS', 'Rushing_TDS', 'Receiving_REC', 'Receiving_YDS', 'Receiving_TDS', 'FL', 'FPTS']
    rows = []
    for row in table.find_all('tr')[2:]:  # Skip the header rows
        data = []
        for cell in row.find_all('td'):
            data.append(cell.text.strip())
        
        # Extract the player's name and team
        player = row.find('td', class_='player-label').find('a', class_='player-name').text.strip()
        team = row.find('td', class_='player-label').contents[-2].strip()
        
        # Replace the original player data with the cleaned data
        data[0:1] = [player, team]
        
        # Add the cleaned row to the list of rows
        rows.append(data)
        
    return {'headers': headers, 'rows': rows}


# Function for scraping Kicker data
def scrape_k_data(table):
    headers = ['Player', 'Team', 'FG', 'FGA', 'XPT', 'FPTS']
    rows = []
    for row in table.find_all('tr')[1:]:  # Skip the header rows
        data = []
        for cell in row.find_all('td'):
            data.append(cell.text.strip())
        
        # Extract the player's name and team
        player = row.find('td', class_='player-label').find('a', class_='player-name').text.strip()
        team = row.find('td', class_='player-label').contents[-2].strip()
        
        # Replace the original player data with the cleaned data
        data[0:1] = [player, team]
        
        # Add the cleaned row to the list of rows
        rows.append(data)
        
    return {'headers': headers, 'rows': rows}


# Function for scraping Defense/Special Teams data
def scrape_dst_data(table):
    headers = ['Player', 'Team', 'SACK', 'INT', 'FR', 'FF', 'TD', 'SAFETY', 'PA', 'YDS AGN', 'FPTS']
    rows = []
    for row in table.find_all('tr')[2:]:  # Skip the header rows
        data = []
        for cell in row.find_all('td'):
            data.append(cell.text.strip())
        
        # Extract the player's name and team
        player = row.find('td', class_='player-label').find('a', class_='player-name').text.strip()
        team = row.find('td', class_='player-label').contents[-2].strip()
        
        # Replace the original player data with the cleaned data
        data[0:1] = [player, team]
        
        # Add the cleaned row to the list of rows
        rows.append(data)
        
    return {'headers': headers, 'rows': rows}



def scrape_data(position, url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table', {'id': 'data'})
        
        if position == 'qb':
            scraped_data = scrape_qb_data(table)
        elif position == 'rb':
            scraped_data = scrape_rb_data(table)
        elif position == 'wr':
            scraped_data = scrape_wr_data(table)
        elif position == 'te':
            scraped_data = scrape_te_data(table)
        elif position == 'flex':
            scraped_data = scrape_flex_data(table)
        elif position == 'k':
            scraped_data = scrape_k_data(table)
        elif position == 'dst':
            scraped_data = scrape_dst_data(table)
        
        
        
        with open(f'{position}_projections.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(scraped_data['headers'])
            csvwriter.writerows(scraped_data['rows'])
                
        print(f"Data scraping and cleaning successful for {position}!")
    else:
        print(f"Failed to fetch the webpage for {position}. Status code: {response.status_code}")



# Example of how to take a week number as an argument and format the URLs accordingly
def format_urls(week_number):
    base_urls = [
        'https://www.fantasypros.com/nfl/projections/qb.php?week={}',
        'https://www.fantasypros.com/nfl/projections/rb.php?week={}',
        'https://www.fantasypros.com/nfl/projections/wr.php?week={}',
        'https://www.fantasypros.com/nfl/projections/te.php?week={}',
        'https://www.fantasypros.com/nfl/projections/flex.php?week={}',
        'https://www.fantasypros.com/nfl/projections/k.php?week={}',
        'https://www.fantasypros.com/nfl/projections/dst.php?week={}',
    ]
    
    formatted_urls = [url.format(week_number) for url in base_urls]
    return formatted_urls


if __name__ == '__main__':

    # Initialize ArgumentParser
    parser = ArgumentParser(description="Scrape NFL projections for a given week.")
    parser.add_argument("week", type=int, help="The NFL week for which to scrape projections.")

    # Parse the arguments
    args = parser.parse_args()
    week_number = args.week

    urls = format_urls(week_number)


    # Main loop for scraping
    for url in urls:
        position = url.split('/')[-1].split('.')[0]
        scrape_data(position, url)
