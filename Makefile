mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser --username admin

run:
	python3 manage.py runserver localhost:8013




git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ALLEGORY1133/graphql.git
git push -u origin main