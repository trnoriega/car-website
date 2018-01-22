import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'cars.settings')

import django
django.setup()

import csv

from classifier.models import Car, BODY_STYLE_CHOICES

body_list = [tup[0] for tup in BODY_STYLE_CHOICES]
print('body_list:', body_list)

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
        # print(label)
        add_car(label)

def add_car(label):
    c = Car.objects.get_or_create(label=label)[0]
    label_split = label.split('-')
    c.make = label_split[0].replace('_', ' ')
    model = label_split[1]
    model_split = model.split('_')
    # print('model', model.replace('_', ' '))
    # print('body-style?:', model_split[-1].upper())
    if model_split[-1].upper() in body_list:
        c.body_style = model_split[-1].upper()
        # print('added:', model_split[-1].upper())
        model = ' '.join(model_split[:-1])
    elif model_split[-1].upper() == 'CAB':
        c.body_style = 'PICKUP'
    c.model = model.replace('_', ' ')
    c.year = label_split[2]
    c.save()

if __name__ == '__main__':
    print('Starting classifier population script')
    populate()
    print('Classifier population script ended')
