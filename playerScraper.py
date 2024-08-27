from bs4 import BeautifulSoup
import requests
import pandas as pd
from typing import List, Dict, Union

from utils import clean_player_data_projection,clean_player_data_salary, combine_projection_and_salary

class PlayerScraper:
    """Class for scraping fantasy football player data."""
    
    def __init__(self, week_number: int):
        """
        Initialize PlayerScraper with the week number.
        
        Parameters:
            week_number (int): NFL week number
        """
        self.week_number = week_number
        self.projection_urls = {
            'QB': f'https://www.fantasypros.com/nfl/projections/qb.php?week={self.week_number}',
            'RB': f'https://www.fantasypros.com/nfl/projections/rb.php?week={self.week_number}',
            'WR': f'https://www.fantasypros.com/nfl/projections/wr.php?week={self.week_number}',
            'TE': f'https://www.fantasypros.com/nfl/projections/te.php?week={self.week_number}',
            'FLEX': f'https://www.fantasypros.com/nfl/projections/flex.php?week={self.week_number}',
            'K': f'https://www.fantasypros.com/nfl/projections/k.php?week={self.week_number}',
            'DST': f'https://www.fantasypros.com/nfl/projections/dst.php?week={self.week_number}',
        }

        self.salary_url = 'https://www.fantasypros.com/daily-fantasy/nfl/fanduel-salary-changes.php'

    def _scrape_generic_projection(self, table: BeautifulSoup, headers: List[str], position: str) -> List[Dict]:
        """
        A generic function to scrape player projection data from a table.
        
        Parameters:
            table (BeautifulSoup): The HTML table to scrape data from.
            headers (List[str]): A list of headers corresponding to the table columns.
            position (str): The player's position (e.g., 'QB', 'RB', etc. or 'FLEX').
        
        Returns:
            List[Dict]: A list of dictionaries, where each dictionary contains the scraped data for one player.
        """
        results = []  # To hold the scraped data for each player as a list of dictionaries

        for row in table.find_all('tr')[2:]:  # Skip the header rows
            data = {}  # To hold the scraped data for one player
            row_data = [cell.text.strip() for cell in row.find_all('td')]
            
            # Extract player's name and team
            raw_player_data = row.find('td', class_='player-label').text.strip()
            player_parts = raw_player_data.split(' ')
            player = ' '.join(player_parts[:-1])
            team = player_parts[-1]

            # Map the headers to the row_data
            data['Player'] = player
            data['Position'] = position
            data['Team'] = team
            for header, value in zip(headers[2:], row_data[1:]):  # Skip "Player" and "Team" headers as we've manually added them
                data[header] = value
            
            # Add position information
            
            
            results.append(data)

        return results





    # ... (other functions like scrape_qb_projection, scrape_rb_projection, etc.)
    # For each of them, pass the position argument to _scrape_generic_projection like so:
    def scrape_qb_projection(self, table: BeautifulSoup) -> Dict:
        """Scrape Quarterback data from the provided HTML table."""
        headers = ['Player', 'Team', 'ATT', 'CMP', 'YDS', 'TDS', 'INTS', 'Rushing_ATT', 'Rushing_YDS', 'Rushing_TDS', 'FL', 'FPTS']
        return self._scrape_generic_projection(table, headers, 'QB')

    def scrape_rb_projection(self, table: BeautifulSoup) -> Dict:
        """Scrape Running Back data from the provided HTML table."""
        headers = ['Player', 'Team', 'Rushing_ATT', 'Rushing_YDS', 'Rushing_TDS', 'Receiving_REC', 'Receiving_YDS', 'Receiving_TDS', 'FL', 'FPTS']
        return self._scrape_generic_projection(table, headers, 'RB')

    def scrape_wr_projection(self, table: BeautifulSoup) -> Dict:
        """Scrape Wide Receiver data from the provided HTML table."""
        headers = ['Player', 'Team', 'Receiving_REC', 'Receiving_YDS', 'Receiving_TDS', 'Rushing_ATT', 'Rushing_YDS', 'Rushing_TDS', 'FL', 'FPTS']
        return self._scrape_generic_projection(table, headers, 'WR')

    def scrape_te_projection(self, table: BeautifulSoup) -> Dict:
        """Scrape Tight End data from the provided HTML table."""
        headers = ['Player', 'Team', 'Receiving_REC', 'Receiving_YDS', 'Receiving_TDS', 'FL', 'FPTS']
        return self._scrape_generic_projection(table, headers, 'TE')

    def scrape_flex_projection(self, table: BeautifulSoup) -> Dict:
        """Scrape Flex data from the provided HTML table."""
        headers = ['Player', 'Team', 'POS', 'Rushing_ATT', 'Rushing_YDS', 'Rushing_TDS', 'Receiving_REC', 'Receiving_YDS', 'Receiving_TDS', 'FL', 'FPTS']
        return self._scrape_generic_projection(table, headers, 'FLEX')

    def scrape_k_projection(self, table: BeautifulSoup) -> Dict:
        """Scrape Kicker data from the provided HTML table."""
        headers = ['Player', 'Team', 'FG', 'FGA', 'XPT', 'FPTS']
        return self._scrape_generic_projection(table, headers, 'K')

    def scrape_dst_projection(self, table: BeautifulSoup) -> Dict:
        """Scrape Defense/Special Teams data from the provided HTML table."""
        headers = ['Player', 'Team', 'SACK', 'INT', 'FR', 'FF', 'TD', 'SAFETY', 'PA', 'YDS AGN', 'FPTS']
        return self._scrape_generic_projection(table, headers, 'DST')

    def scrape_projection(self, positions: List[str]) -> Dict:
        """
        Scrape player data for the given positions.
        
        Parameters:
            positions (List[str]): List of positions to scrape (e.g., ['qb', 'rb']).
        
        Returns:
            Dict[str, Dict[str, List[List[str]]]]: Scraped data for each position.
        """
        results = {}  # To hold the scraped data for each position
        
        for position in positions:
            url = self.projection_urls[position]  # Get the URL for the specific position
            
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                table = soup.find('table', {'id': 'data'})
                
                scrape_method_name = f"scrape_{position.lower()}_projection"
                scrape_method = getattr(self, scrape_method_name, None)
                if scrape_method is None:
                    print(f"No scraping method for position: {position}. Skipping.")
                    continue
                
                scraped_projection = scrape_method(table)
                results[position] = scraped_projection
                
                print(f"Data scraping and cleaning successful for {position}!")
            else:
                print(f"Failed to fetch the webpage for {position}. Status code: {response.status_code}")
        
        return results
    
    def scrape_salaries(self) -> Dict[str, str]:
        """
        Scrape the salaries of players from FantasyPros and return as a dictionary.
        
        Returns:
            Dict[str, str]: Dictionary mapping player names to their salaries.
        """
        # URL to scrape from
        
        url = self.salary_url

        # Fetch the webpage content using requests
        response = requests.get(url)
        
        # Dictionary to store player salaries
        player_salaries = {}
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Locate the table containing the data
            table = soup.find('table', {'id': 'data-table'})
            
            # Iterate through each row in the table
            for row in table.find_all('tr')[1:]:  # Skip the header row
                data = []
                for cell in row.find_all('td'):
                    data.append(cell.text.strip())
                
                # Clean the player data
                player, team, position = clean_player_data_salary(data[1])
                
                # Replace the original player data with cleaned data
                data[1:2] = [player, team, position]
                
                # Store the player salary
                player_salaries[player] = data[-3]  # "This Week" column contains the salary
                
            print("Salary data scraping and cleaning successful!")
        else:
            print(f"Failed to fetch the webpage for salaries. Status code: {response.status_code}")
        
        return player_salaries
    
    

    
    def save_to_csv(self, position_data: Dict, filename: str) -> None:
        """
        Save the scraped player data to a CSV file for a given position.

        Parameters:
            position_data (Dict): The player data scraped for a single position.
            filename (str): The name of the CSV file to save the data to.
        """
        
        # Convert the list of dictionaries to a DataFrame
        df = pd.DataFrame(position_data)
        
        # Save the DataFrame to a CSV file
        df.to_csv(filename, index=False)
