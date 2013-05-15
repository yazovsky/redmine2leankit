from python_leankit import *
from python_redmine import *

# LeanKit configuration
LEANKIT_HOST = "test.leankitkanban.com"
LEANKIT_LOGIN = "use@host.com"
LEANKIT_PASSWORD = "qwerty"
LEANKIT_BOARDNAME = "Test"

# RedMine configuration
READMINE_URL = "https://redmine.host.com"
READMINE_API_KEY = "kj46436faa25e36ade5bdsdg474325798c72234"
READMINE_PROJECT_IDENTIFIER = "test-project"
READMINE_MAPPING_FEATURE_ID = 2

# you should specify mapping between statuses in RedMine and columns in Leankit
STATUSES_MAPPING = {
    "New": "ToDo",

    "Evaluated": "Analysis::In progress",
    "Assigned": "Analysis::Done",

    "In Progress": "Development",

    "Resolved": "Testing::In progress",
    "Reopened / Rejected": "Testing::In progress",
    "Tested": "Testing::Done",

    "Closed": "Delivered",
    "Blocked / Feedback": "Blocked"
    # ,"Invalid": "Analysis::ToDo" # commented statuses will no be sycnhronized
}

if __name__ == '__main__':

    kanban = LeankitKanban(LEANKIT_HOST, LEANKIT_LOGIN, LEANKIT_PASSWORD)
    redmine = Redmine(READMINE_URL, READMINE_API_KEY)

    print "Getting RedMine project '%s' ... " % READMINE_PROJECT_IDENTIFIER,
    project = redmine.get_project(identifier = READMINE_PROJECT_IDENTIFIER)
    print "[yes]"
    # for b in kanban.getBoards():
    #     print b.title

    print "Getting LeanKit board '%s'..." % LEANKIT_BOARDNAME,
    board = kanban.getBoard(title = LEANKIT_BOARDNAME)

    print "Cleanup LeanKit board ... ",
    for card in board.cards:
        card.remove()
    print "[yes]"

    print "Start copy tickets from RedMine to LeanKit ..."
    for issue in project.filter_issues(tracker_id = READMINE_MAPPING_FEATURE_ID, status_id = "*"):
        if issue.status['name'] in STATUSES_MAPPING:
            lane = board.getLane(STATUSES_MAPPING[issue.status['name']])
            print "sync '%s' ... " % issue.subject,
            card = LeankitCard.create(lane, externalId = issue.id, title = issue.subject).save()
            print "[yes]"
    print "Finished"
