# Here is the code for the FantasyOptimizer class with comments, docstrings, and type annotations.
from typing import List, Dict, Union
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, LpStatus

class RosterOptimizer:
    """
    A class to represent the Fantasy Football Lineup Optimizer.
    """
    def __init__(self, player_data: List[Dict[str, Union[str, int, float]]]) -> None:
        """
        Initialize the FantasyOptimizer with the player data.
        
        Parameters:
            player_data (List[Dict]): List of dictionaries, each containing player details.
        """
        self.player_data = player_data
        self.prob = LpProblem("FantasyFootball", LpMaximize)
    
    def build_problem(self, salary_cap=60000) -> None:
        """
        Build the linear programming problem for the fantasy football lineup optimization.
        """
        # Create a variable for each player
        player_vars = LpVariable.dicts("Player", [player['Name'] for player in self.player_data], 0, 1, cat='Binary')
        
        # Objective function: Maximize the total projected points
        self.prob += lpSum([player['ProjectedPoints'] * player_vars[player['Name']] for player in self.player_data]), "TotalProjectedPoints"
        
        # Constraint: Total cost should not exceed $60,000
        self.prob += lpSum([player['Cost'] * player_vars[player['Name']] for player in self.player_data]) <= salary_cap, "TotalCost"
        
        # Position constraints
        for position, min_players in {'QB': 1, 'RB': 2, 'WR': 3, 'TE': 1, 'FLEX': 1, "K": 1,'DST': 1}.items():
            self.prob += lpSum([player_vars[player['Name']] for player in self.player_data if player['Position'] == position]) == min_players, f"{position}Constraint"
        
        # Uniqueness constraint: A player can only appear once in the roster
        for player in self.player_data:
            self.prob += player_vars[player['Name']] <= 1, f"Uniqueness_{player['Name']}"
    
    def solve(self) -> str:
        """
        Solve the fantasy football lineup optimization problem.
        
        Returns:
            str: The status of the optimization.
        """
        self.prob.solve()
        status = LpStatus[self.prob.status]
        
        return status

    def get_optimal_lineup(self) -> List[Dict[str, Union[str, int, float]]]:
        """
        Get the optimal lineup based on the solved problem.
        
        Returns:
            List[Dict]: List of dictionaries, each containing the details of the players in the optimal lineup.
        """
        optimal_lineup = []
        
        for v in self.prob.variables():
            if v.varValue > 0:
                player_name = v.name.split("_")[1]
                player_details = next((player for player in self.player_data if player['Name'] == player_name), None)
                optimal_lineup.append(player_details)
        
        return optimal_lineup

# You can test this class by creating an object of it and then calling the methods.
# Please make sure to install the `pulp` package before running this code in your environment.
