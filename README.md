# Example Tetra Project

Clone repository, setup python environment, and install esbuild from npm:

```
git clone https://github.com/samwillis/tetra-example.git
cd ./tetra-example
python -m env venv
source ./env/bin/activate
pip install -r requirements.txt
npm init
npm install esbuild
```

Create sqlite db:
```
python manage.py migrate
```

Run server:
```
python manage.py runserver
```
