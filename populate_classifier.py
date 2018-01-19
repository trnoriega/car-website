import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'cars.settings')

import django
django.setup()

import csv

from classifier.models import Car

FILE_PATH = os.path.join(
    os.getcwd(),
    'data',
    'labels.csv'
)

def populate():
    with open(FILE_PATH, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        label_list = list(reader)[0]

    for label in label_list:
        print(label)
        add_car(label)

def add_car(label):
    c = Car.objects.get_or_create(label=label)[0]
    c.save()

if __name__ == '__main__':
    print('Starting classifier population script')
    populate()
