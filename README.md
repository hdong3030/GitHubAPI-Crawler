# GitHubAPI-Crawler
This is a fork of @user2589/ghd

## To execute the script
Create token.txt file, and list your GitHub Token per line

## How to create GitHub Tokens
Once you log into your GitHub account, click on your avatar - Settings - Developer settings - Personal access tokens - Generate new token - Generate token (green button at the bottom of the screen). Important: DO NOT CHECK ANY OF THE BOXES THAT DEFINE SCOPES

You could have multiple email accounts (--> multiple GitHub accounts) --> make a token for each. 

## How to contribute
Create a fork, make changes in your fork, and once finish the implementation, submit a PR.

## to download notebooks
python3 download_notebooks.py

## to find notebooks with a specific keyword

type this into main.py, where "ready" is the keyword and then run the main file:

get_commits("ready")
python3 main.py

## to get notebooks from a specific date range

type this into main.py, where the parameters are as follows:
(start date, end date, increment in hours, any condition)

get_all_repos(datetime.datetime(2019, 2, 3), datetime.datetime(2019, 6, 1), 6, True)
python3 main.py

## to get all commits of a certain repository

type this into main.py, where repo is a repository (owner/repo).
Example: "hdong3030/GitHubAPI-Crawler"

api.repo_commits(repo)
python3 main.py

## to get notebooks that have a certain type of file

type this into main.py. Then go to get_production_nb.py and change the conditions
that are wanted.

get_production_nb_byEXT()
python3 main.py

## to get notebooks that used kedros, modelDB, databricks






