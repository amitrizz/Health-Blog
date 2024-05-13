#!/bin/bash

echo "Collecting static files..."
python manage.py collectstatic --noinput || { echo "Failed to collect static files"; exit 1; }

echo "Making migrations..."
python manage.py makemigrations
python manage.py makemigrations posts || { echo "Failed to make migrations"; exit 1; }
python manage.py makemigrations users --empty || { echo "Failed to make migrations"; exit 1; }

echo "Applying migrations..."
python manage.py migrate
echo "Applying migrations for posts app..."
python manage.py migrate posts || { echo "Failed to apply migrations for posts app"; exit 1; }
echo "Applying migrations for users app..."
python manage.py migrate users || { echo "Failed to apply migrations for users app"; exit 1; }

echo "All migrations applied successfully."

echo "Creating superuser..."
# python manage.py createsuperuser --noinput --username=admin --email=admin@gmail.com --password=admin || { echo "Failed to create superuser"; exit 1; }
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@gmail.com', 'admin')" | python manage.py shell || { echo "Failed to create superuser"; exit 1; }

exec "$@"
