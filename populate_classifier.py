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
    label_split = label.split('-')
    c.make = label_split[0]
    c.model = label_split[1]
    c.body_type = label_split[1]
    c.year = label_split[2]
    c.save()

if __name__ == '__main__':
    print('Starting classifier population script')
    populate()
