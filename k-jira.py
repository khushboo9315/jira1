from jira import JIRA
  
# Specify a server key. It should be your
# domain name link. yourdomainname.atlassian.net
jiraOptions = {'server': "https://khushboo9315.atlassian.net/"}
  
# Get a JIRA client instance, pass,
# Authentication parameters
# and the Server name.
# emailID = your emailID
# token = token you receive after registration
jira = JIRA(options=jiraOptions, basic_auth=(
    "khushboo22@navgurukul.org", "YVtytAyOp0bAsX1wlEVG9F4D"))
# Search all issues mentioned against a project name.
for singleIssue in jira.search_issues(jql_str='project = KHUS'):
    print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary,
                             singleIssue.fields.reporter.displayName))