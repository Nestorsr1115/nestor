source .venv\Scripts\Activate
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rm -rf public
Expand-Archive -Path .\frontend.zip -DestinationPath ""D:\reflex\mouredev\public\"
rm -f frontend.zip
deactivate