# django-admin startproject tributepage
# mv tributepage tribute-page
# cd tribute-page
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

pip install -r requirements.txt