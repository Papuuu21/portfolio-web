mkdir public
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
rm -rf public
reflex init
reflex run --frontend-only
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
deactivate
