from datetime import date, timedelta
from github_api import GitHubAPI


def get_all_repos(startDate, endDate, timeWindow):
    api = GitHubAPI()
    change = timedelta(days=timeWindow)
    
    while startDate <= endDate:
        newStart = startDate + change
        api.get_repo("Jupyter%20Notebook", str(startDate), str(newStart))
        startDate = newStart
