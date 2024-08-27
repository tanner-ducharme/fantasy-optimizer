import json
from playerScraper import PlayerScraper
from utils import combine_projection_and_salary
from rosterOptimizer import RosterOptimizer
    



if __name__ == '__main__':
    # Initialize scraper with the current NFL week number
    # week_number = 1  # Replace with the current week number
    # scraper = PlayerScraper(week_number)

    # # Define positions to scrape
    # positions_to_scrape = ['RB', 'DST', 'FLEX']

    # # Scrape player projections
    # projection_data = scraper.scrape_projection(positions_to_scrape)
    
    # # Scrape player salaries
    # salary_data = scraper.scrape_salaries()

    # # Combine projection and salary data
    # combined_data = combine_projection_and_salary(projection_data, salary_data)

    # # print(json.dumps(combined_data, sort_keys=False, indent=4))

    # scraper.save_to_csv(combined_data, 'data/FLEX.csv')
    # scraper.save_to_csv(projection_data['RB'], 'data/RB.csv')
    
    PLAYER_DATA = [
        {'Name': 'QB_Player1', 'Position': 'QB', 'Cost': 6100, 'ProjectedPoints': 22},
        {'Name': 'QB_Player2', 'Position': 'QB', 'Cost': 6400, 'ProjectedPoints': 20},
        {'Name': 'QB_Player3', 'Position': 'QB', 'Cost': 6700, 'ProjectedPoints': 25},
        {'Name': 'QB_Player4', 'Position': 'QB', 'Cost': 6900, 'ProjectedPoints': 23},
        {'Name': 'QB_Player5', 'Position': 'QB', 'Cost': 7200, 'ProjectedPoints': 28},

        {'Name': 'RB_Player1', 'Position': 'RB', 'Cost': 5300, 'ProjectedPoints': 15},
        {'Name': 'RB_Player2', 'Position': 'RB', 'Cost': 5700, 'ProjectedPoints': 17},
        {'Name': 'RB_Player3', 'Position': 'RB', 'Cost': 6000, 'ProjectedPoints': 19},
        {'Name': 'RB_Player4', 'Position': 'RB', 'Cost': 6200, 'ProjectedPoints': 21},
        {'Name': 'RB_Player5', 'Position': 'RB', 'Cost': 6500, 'ProjectedPoints': 23},

        {'Name': 'WR_Player1', 'Position': 'WR', 'Cost': 4800, 'ProjectedPoints': 14},
        {'Name': 'WR_Player2', 'Position': 'WR', 'Cost': 5200, 'ProjectedPoints': 16},
        {'Name': 'WR_Player3', 'Position': 'WR', 'Cost': 5500, 'ProjectedPoints': 18},
        {'Name': 'WR_Player4', 'Position': 'WR', 'Cost': 5800, 'ProjectedPoints': 20},
        {'Name': 'WR_Player5', 'Position': 'WR', 'Cost': 6100, 'ProjectedPoints': 22},

        {'Name': 'TE_Player1', 'Position': 'TE', 'Cost': 3300, 'ProjectedPoints': 10},
        {'Name': 'TE_Player2', 'Position': 'TE', 'Cost': 3600, 'ProjectedPoints': 11},
        {'Name': 'TE_Player3', 'Position': 'TE', 'Cost': 3800, 'ProjectedPoints': 12},
        {'Name': 'TE_Player4', 'Position': 'TE', 'Cost': 4000, 'ProjectedPoints': 13},
        {'Name': 'TE_Player5', 'Position': 'TE', 'Cost': 4200, 'ProjectedPoints': 15},

        {'Name': 'FLEX_Player1', 'Position': 'FLEX', 'Cost': 4700, 'ProjectedPoints': 13},
        {'Name': 'FLEX_Player2', 'Position': 'FLEX', 'Cost': 5000, 'ProjectedPoints': 15},
        {'Name': 'FLEX_Player3', 'Position': 'FLEX', 'Cost': 5300, 'ProjectedPoints': 16},
        {'Name': 'FLEX_Player4', 'Position': 'FLEX', 'Cost': 5500, 'ProjectedPoints': 18},
        {'Name': 'FLEX_Player5', 'Position': 'FLEX', 'Cost': 5800, 'ProjectedPoints': 20},

        {'Name': 'K_Player1', 'Position': 'K', 'Cost': 2500, 'ProjectedPoints': 8},
        {'Name': 'K_Player2', 'Position': 'K', 'Cost': 2700, 'ProjectedPoints': 9},
        {'Name': 'K_Player3', 'Position': 'K', 'Cost': 2900, 'ProjectedPoints': 10},
        {'Name': 'K_Player4', 'Position': 'K', 'Cost': 3100, 'ProjectedPoints': 11},
        {'Name': 'K_Player5', 'Position': 'K', 'Cost': 3300, 'ProjectedPoints': 12},

        {'Name': 'DST_Player1', 'Position': 'DST', 'Cost': 2700, 'ProjectedPoints': 8},
        {'Name': 'DST_Player2', 'Position': 'DST', 'Cost': 2900, 'ProjectedPoints': 9},
        {'Name': 'DST_Player3', 'Position': 'DST', 'Cost': 3100, 'ProjectedPoints': 10},
        {'Name': 'DST_Player4', 'Position': 'DST', 'Cost': 3200, 'ProjectedPoints': 11},
        {'Name': 'DST_Player5', 'Position': 'DST', 'Cost': 3400, 'ProjectedPoints': 12},
    ]


    # Initialize the optimizer with sample player data
    optimizer = RosterOptimizer(PLAYER_DATA)

    # Build the optimization problem
    optimizer.build_problem()

    # Solve the problem
    result_status = optimizer.solve()

    # Get the optimal lineup
    optimal_lineup = optimizer.get_optimal_lineup()

    # Display the results
    print(f"Optimization Status: {result_status}")
    print("Optimal Lineup:")
    for player in optimal_lineup:
        print(f"{player['Name']} ({player['Position']}) - ${player['Cost']}, {player['ProjectedPoints']} points")






