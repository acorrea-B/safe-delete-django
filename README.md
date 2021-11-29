# safe-delete-django
test the safe delete lib of https://pypi.org/project/django-safedelete/ 

# Install 

pipenv insatll

pipenv shell 


# Run django shell 

python manage.py shell

# Use models

from cars.models import Line, Car

line1 = Line("Suv")
line1.save()
line2 = Line("Sedan")
line2.save()

Line.objects.all()

car = Car(name="Subaru")
car.save()
car.line.add(line2)

Car.objects.all()

# Delete elements

line2.delete()

# List elements with deleted

Line.objects.all_with_deleted()

Line.objects.all(force_visibility=True)

