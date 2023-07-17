set -o errexit

pip install -r requiremetnts.txt
python manage.py collectstatic --no-input
pithon manage.py migrate