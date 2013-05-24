## Description

I'd like to use RedMine as a tickets tracking system and use LeanKit as dashboard, to enjoy the benefits that both systems give. Advanced project management in RedMine and clean visualization of project progress in LeanKit.

Supported synchronization based on ticket status and on assigned person. 

For example, by default Redmine doesn't support "Testing" ticket status. You may configure to sync ticket with "Resolved" status differently when it's assigned to different persons. "In progress" assigned to QA means "Testing::In Progress". "In progress" assigned to developer means "Development::In progress".

## Configuration

1. Install necessary Python packages by running install-requirements.sh script.
2. Edit app.py file to configurate script with RedMine and LeanKit related properties:

	LEANKIT_HOST = you LeanKit account host name, probably something like this: "your_account.leankitkanban.com"

	LEANKIT_LOGIN = you LeanKit account email

	LEANKIT_PASSWORD = your LeanKit account password

	LEANKIT_BOARDNAME = name of the board what you would like to sync

	READMINE_URL = full URL of your RedMine instans. With protocol, host name and path. For example: http://myhost/redmine/

	READMINE_API_KEY = look at your RedMine account profile for this API key

	READMINE_PROJECT_IDENTIFIER = look at project settings for this, "Identifier" field

	READMINE_MAPPING_FEATURE_ID = you may filter tickets for sync by type. e.g. sync only feaures. You have to specify ID of tickets type which will used for sync, e.g. "Feature" = 2

3. You may also need to configure mapping between RedMine tickets statuses and LeanKit board lanes. Edit app.py file for it and change STATUSES_MAPPING constant.
4. This script do not create the LeanKit board and lanes for you. So, you have to create the board and create lanes according to settings you configured in step 3 (mapping)
5. run python app.py

## Requirements

Python 2.7
Pip 1.0

Also make sure necessary python packages are installed. Run install-requirements.sh script for it or install via pip manually (list of packages in required.txt file).

## License

Author used two source scripts "redmine_python.py" and "redmine_leankit.py", which were open source at the moment of initial project publish. More information about copyright could be found in related files.

Author wrote this script for his own purpose and don't mind if somebody will reuse of rewrite any piece of this code. Enjoy and help your self!

I would love to merge to trunk pull request which will implement two synchronization
