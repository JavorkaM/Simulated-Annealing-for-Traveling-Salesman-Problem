# Simulated Annealing for Traveling Salesman Problem

This is a Python implementation of the Simulated Annealing algorithm to solve the Traveling Salesman Problem (TSP). The goal is to find the shortest possible route for a business traveler who needs to visit multiple cities exactly once, minimizing travel costs based on the Euclidean distance between cities.

## Algorithm Overview

Simulated Annealing is an optimization algorithm that explores the search space of possible solutions and avoids getting stuck in local optima. It starts with an initial solution and iteratively improves it by randomly generating neighboring solutions and accepting worse solutions with a decreasing probability.

The algorithm follows these steps:

1. Generate an initial solution (random permutation of cities).
2. Calculate the fitness of the current solution (total distance traveled).
3. Set the initial temperature and define the temperature decrease rate.
4. While the temperature is above a minimum threshold:
   - Generate a neighboring solution by applying one of the three types of neighbor generation: Swap, Insertion, or Reversion.
   - Calculate the fitness of the new solution.
   - If the new solution is better (has a lower fitness), accept it as the current solution.
   - If the new solution is worse, accept it with a probability determined by the temperature and the difference in fitness.
   - Decrease the temperature.
5. Output the final solution and its fitness.

## Neighbor Generation

This implementation includes three types of neighbor generation techniques:

1. **Swap**: Selects two random cities in the current solution and swaps their positions.
2. **Insertion**: Selects a random city in the current solution and inserts it at a different random position.
3. **Reversion**: Selects two random positions in the current solution and reverses the order of the cities between those positions.

By applying these neighbor generation techniques, the algorithm explores different local search regions and increases the chances of finding an optimal or near-optimal solution.

## Parameters

The algorithm includes several adjustable parameters that can be modified to customize the behavior of the algorithm:

- `TEMPERATURE_AT_START`: Initial temperature for the annealing process.
- `TEMPERATURE_DECREASE`: Percentage decrease rate for the temperature at each iteration.
- `MIN_TEMPERATURE`: Minimum temperature threshold to stop the annealing process.
- `NUM_OF_ITERATIONS_FOR_TEMPERATURE`: Number of iterations to perform at each temperature level.
- `TYPE_OF_NEIGHBOURHOOD_GENERATION`: Type of neighbor generation technique to use (0 for random per cycle, 1 for swap, 2 for insertion, 3 for reversion).
- `NUM_OF_CITIES`: Number of cities to visit.
- `GRID_SIZE_X` and `GRID_SIZE_Y`: Size of the map/grid where the cities are located.
- `VISUALIZE_SOLUTION`: Flag to enable/disable visualization of the final solution.

## Usage

1. Install Python (version 3.6 or higher) if not already installed.
2. Clone the repository or download the `simulated_annealing_tsp.py` file.
3. Open a terminal/command prompt and navigate to the directory containing the script.
4. Run the script using the command: `python simulated_annealing_tsp.py`.
5. The algorithm will generate a random set of cities and output the final solution and its fitness.

Feel free to modify the parameters and experiment with different settings to observe their effects on the algorithm's performance.

## Visualization

If the `VISUALIZE_SOLUTION` flag is set to `True`, a graphical window will open to visualize the final solution. The cities are represented as circles, and the path connecting

 them is displayed. The window can be resized, and the scale can be adjusted using the `VISUAL_WINDOW_SCALE` parameter.

## License

This project is licensed under the [MIT License](LICENSE).

Please refer to the license file for more information.
