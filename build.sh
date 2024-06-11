python -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
rmdir /s /q public
reflex init
reflex export --frontend-only
tar -xf frontend.zip -C public
del frontend.zip
deactivate
