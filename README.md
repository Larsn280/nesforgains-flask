<!-- Create Project Directory -->

mkdir nesforgains-web
cd nesforgains-web

<!-- Set up venv -->

py -3 -m venv .venv

<!-- Activate venv -->

.venv\Scripts\activate

<!-- Install Flast or Django Framework -->

pip install Flask
pip install django

<!-- Deactivate venv -->

deactivate

<!-- Set temporary path instead of System env path -->

<!-- Cmd temporary -->

set FLASK_APP=application.py

<!-- PowerShell temporary -->

$env:FLASK_APP = "application.py"

% Run app

flask run
flask run --debug

% Run pytest

pytest

TESTING
