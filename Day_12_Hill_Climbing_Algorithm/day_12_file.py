import numpy as np
from typing import List, Dict, Tuple, Set

PuzzleOutput = Tuple[Tuple[int], Tuple[int], np.array]
ElevationGraph = Dict[Tuple[int], Dict[Tuple[int], int]]
PathDict = Dict[Tuple[int], int]
NodesDict = Dict[Tuple[int], Tuple[int]]

def load_puzzle_input(case: str) -> PuzzleOutput:
    if case == 'test':
        file_name = "Day_12_Hill_Climbing_Algorithm/test_input.txt"
    elif case == 'puzzle':
        file_name = "Day_12_Hill_Climbing_Algorithm/puzzle_input.txt"
    with open(file_name) as f:
        lines = [x.strip() for x in f.readlines() if x.strip() != ""]

    rows, columns = len(lines), len(lines[0])
    elevation_grid = np.zeros(shape=(rows, columns), dtype=int)

    for row_index in range(rows):
        for column_index in range(columns):
            if lines[row_index][column_index] == "S":
                start_position = (row_index, column_index)
                elevation_grid[row_index, column_index] = ord('a')
            elif lines[row_index][column_index] == "E":
                target_position = (row_index, column_index)
                elevation_grid[row_index, column_index] = ord('z')
            else:
                elevation_grid[row_index, column_index] = ord(lines[row_index][column_index])

    return start_position, target_position, elevation_grid

def make_elevation_graph(elevation_grid: np.array) -> ElevationGraph:
    rows, columns = elevation_grid.shape

    all_points: Set[int] = set((i, j) for i in range(rows) for j in range(columns))

    # Initialize graph
    graph: ElevationGraph = dict.fromkeys(all_points)
    for node in graph.keys():
        graph[node] = {}

    for current_node in graph.keys():
        for target_node in all_points:
            elevation_difference: int = elevation_grid[current_node] - elevation_grid[target_node]
            elevation_check: bool = elevation_difference <= 1
            proximity_check: bool = max(abs(current_node[0] - target_node[0]), abs(current_node[1] - target_node[1])) <= 1
            not_diagonal_check: bool = (current_node[0] == target_node[0]) | (current_node[1] == target_node[1])
            if target_node == current_node:
                graph[current_node][target_node] = 0
            elif elevation_check and proximity_check and not_diagonal_check:
                graph[current_node][target_node] = 1
            else:
                graph[current_node][target_node] = 1000

    return graph

def hill_climb_algorithm(point_E: Tuple[int], graph: ElevationGraph) -> PathDict:
    """
    The hill climb algorithm calculates the shortest path from point E (the starting
    point of highest elevation, to every other point in the grid
    """    
    unvisited_nodes: List[Tuple(int)] = list(graph.keys())
    shortest_path: PathDict = {}
    previous_nodes: NodesDict = {}

    max_distance: int = 10_000_000_000
    for node in unvisited_nodes:
        shortest_path[node] = max_distance
    shortest_path[point_E] = 0    

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                    
        for target_node in graph[current_min_node].keys():
            if graph[current_min_node][target_node] == 1:
                tentative_distance = shortest_path[current_min_node] + 1
                if tentative_distance < shortest_path[target_node]:
                    shortest_path[target_node] = tentative_distance
                    previous_nodes[target_node] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return shortest_path
            

def steps_from_any_a_level(shortest_paths_from_E: PathDict, elevation_graph: ElevationGraph) -> int:
    a_points = [point for point in elevation_graph.keys() if elevation_grid[point] == ord('a')]
    
    shortest_path_from_a = min([shortest_paths_from_E[point] for point in a_points])

    return shortest_path_from_a

if __name__ == "__main__":
    point_S, point_E, elevation_grid = load_puzzle_input("puzzle")

    elevation_graph = make_elevation_graph(elevation_grid)

    shortest_paths_from_E = hill_climb_algorithm(point_E, elevation_graph)

    print(f"The number of steps in the shortest path from {point_S=} to {point_E=} is {shortest_paths_from_E[point_S]} steps")

    shortest_path_a = steps_from_any_a_level(shortest_paths_from_E, elevation_graph)

    print(f"The number of steps in the shortest path from any elevation a to {point_E=} is {shortest_path_a} steps")