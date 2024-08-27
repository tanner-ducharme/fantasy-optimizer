from typing import List, Dict

def clean_player_data_salary(player_data: str) -> (str, str, str):
    """
    Clean the player data to extract player name, team, and position from salary data.
    
    Parameters:
        player_data (str): Raw player data string from the scraped webpage.
        
    Returns:
        tuple: Tuple containing the cleaned player name, team, and position.
    """
    player, info = player_data.split(' (')
    team, position = info.rstrip(')').split(' - ')
    return player, team, position

def clean_player_data_projection(player_data: str) -> (str, str):
    """
    Clean the player data to extract player name and team for projections.
    
    Parameters:
        player_data (str): Raw player data string from the scraped webpage.
        
    Returns:
        tuple: Tuple containing the cleaned player name and team.
    """
    # Splitting by space to isolate the last element as the team
    parts = player_data.split(' ')
    team = parts[-1]
    player = ' '.join(parts[:-1])
    return player, team


def combine_projection_and_salary(projection_data: Dict[str, List[Dict]], salary_data: Dict[str, str]) -> Dict[str, List[Dict]]:
    """
    Combine the projection and salary data for players.
    
    Parameters:
        projection_data (Dict[str, List[Dict]]): The projection data for players in a list of dictionaries.
        salary_data (Dict[str, str]): The salary data for players.
        
    Returns:
        Dict[str, List[Dict]]: Combined data.
    """
    combined_data = {}
    
    for position, players in projection_data.items():
        combined_data[position] = []
        
        for player in players:
            player_name = player.get("Player")
            if player_name in salary_data:
                player["Salary"] = salary_data[player_name]
            else:
                player["Salary"] = "N/A"  # If salary data is not available
                
            combined_data[position].append(player)
    
    return combined_data
