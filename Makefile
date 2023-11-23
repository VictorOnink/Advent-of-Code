include .env

black:
	isort --profile black advent_of_code
	black advent_of_code

year=2022
day=1
case=test

solution:
	python run_solution.py --year $(year) --day $(day) --case $(case)
