# Unity

## Run Backend

```bash
cd unity_be
pip install -r /path/to/requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
Import the Postman collection to use API to add mail and add partner

## Run Frontend
Frontend only show information about partner whose id is 1 because I do not have enough time to create a UI that can modify partner's id.

```bash
cd unity_fe
npm install
npm run serve
```
## Todo

- [x] Exposes an API to store the emails. Feel free to use Django REST Framework
- [ ] A view to list down the emails in the reverse chronological order and show the number of new emails added this calendar month
- [x] Integrate the api with the email collection widget present in this project.
- [ ] Bonus - setup a celery task that runs every Monday and Wednesday and prints the number of new emails added in the current calendar month to the console
