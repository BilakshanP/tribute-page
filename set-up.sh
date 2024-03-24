# mkdir tribute-page
# cd tribute-page
# python3 -m venv .venv
# source .venv/bin/activate
# pip install django
# django-admin startproject tributepage
# mv tributepage/* .
# python3 manage.py startapp tributeapp

if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi

source .venv/bin/activate
echo "To exit the virtual environment, type 'deactivate'"

if [ ! -f "requirements.txt" ]; then
    echo "requirements.txt not found"
    touch requirements.txt
fi

if [ ! -f ".env" ]; then
    echo ".env not found"
    mv template.env .env
fi

pip install -r requirements.txt