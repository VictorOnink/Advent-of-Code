import numpy as np


def load_puzzle_input(case: str) -> np.array:
    if case == "test":
        file_name = "Day_8_Treetop_Tree_House/test_input.txt"
    elif case == "puzzle":
        file_name = "Day_8_Treetop_Tree_House/puzzle_input.txt"
    tree_grid: np.array = np.genfromtxt(file_name, delimiter=1)
    tree_grid = tree_grid.astype(int)
    return tree_grid


def count_visible_tree(tree_grid: np.array) -> None:
    visibility_grid = np.zeros(tree_grid.shape, dtype=int)

    # All edges are visible
    visibility_grid[0, :] = 1
    visibility_grid[-1, :] = 1
    visibility_grid[:, 0] = 1
    visibility_grid[:, -1] = 1

    for row in range(1, tree_grid.shape[0] - 1):
        for column in range(1, tree_grid.shape[1] - 1):
            tree: int = tree_grid[row, column]
            visibility_grid[row, column] = max(
                tree > max(tree_grid[:row, column]),
                tree > max(tree_grid[row + 1 :, column]),
                tree > max(tree_grid[row, :column]),
                tree > max(tree_grid[row, column + 1 :]),
            )

    print(f"There are {np.sum(visibility_grid)} trees visible in this grid.")


def get_scenic_score(tree_grid: np.array) -> None:
    scenic_grid = np.zeros(tree_grid.shape, dtype=int)

    for row in range(tree_grid.shape[0]):
        for column in range(tree_grid.shape[1]):
            tree: int = tree_grid[row, column]

            if row == 0:
                visibility_top = 0
            else:
                visibility_top = scenic_score_direction(
                    tree, tree_grid[:row, column][::-1]
                )
            if row == (tree_grid.shape[1] - 1):
                visibility_down = 0
            else:
                visibility_down = scenic_score_direction(
                    tree, tree_grid[row + 1 :, column]
                )
            if column == 0:
                visibility_left = 0
            else:
                visibility_left = scenic_score_direction(
                    tree, tree_grid[row, :column][::-1]
                )
            if column == (tree_grid.shape[0] - 1):
                visibility_right = 0
            else:
                visibility_right = scenic_score_direction(
                    tree, tree_grid[row, column + 1 :]
                )
            scenic_grid[row, column] = (
                visibility_top * visibility_down * visibility_left * visibility_right
            )

    print(f"The maximum scenic score is {np.max(scenic_grid)}")


def scenic_score_direction(tree_value: int, trees_line_of_view: np.array) -> int:
    scenic_score: int = 0
    for tree_height in trees_line_of_view:
        scenic_score += 1
        if tree_height >= tree_value:
            break
    return scenic_score


if __name__ == "__main__":
    tree_grid = load_puzzle_input("puzzle")

    count_visible_tree(tree_grid)

    get_scenic_score(tree_grid)
