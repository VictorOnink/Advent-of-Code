include .env

black:
	isort --profile black advent_of_code
	black advent_of_code

solution:
	python run_solution.py --year $(YEAR) --day $(DAY) --case $(CASE)
