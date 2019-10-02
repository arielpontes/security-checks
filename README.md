# EEA Security Checks

This is a simple script that access the GitHub API and tries to find all Python
repositories with security warnings. It is not 100% reliable because the GitHub
API doesn't provide this information, so the script downloads the requirements
file from the repositories (if they are found) and runs the safety checks
locally using the `safety` package.

## How to use

* Create a virtualenv
* Install the dependencies

        pip install -r requirements.txt

* Create a `settings.py` file based on the example and update it with your token:

        cp settings.py.example settings.py

* Run the script

        python run.py

This will generate a `report.json` with the results.

## Limitations

### API limit

The GitHub API has a limit. This means the execution of the script will stop
after analyzing a certain number of repositories.

### Static list of Python repositories

In order to minimize the number of API hits, the script uses a static list of
Python repos. This list was generated using the `update_python_repos.py` script.
If new Python repos are added to the EEA organization, you need to run this
script again to update the list and commit the new list.
