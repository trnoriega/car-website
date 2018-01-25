import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'cars.settings')

import django
django.setup()

import csv

from classifier.models import Car, BODY_STYLE_CHOICES

body_list = [tup[0] for tup in BODY_STYLE_CHOICES]

corrections = [
    (['Acura-Integra_Type_R-2001', 
      'Chevrolet-Cobalt_SS-2010',
      'Chevrolet-Corvette_Ron_Fellows_Edition_Z06-2007',
      'Chevrolet-Corvette_ZR1-2012',
      'Dodge-Challenger_SRT8-2011',
      'Infiniti-G_Coupe_IPL-2012',
      'Jaguar-XK_XKR-2012',
      'Lamborghini-Gallardo_LP_570_4_Superleggera-2012',], 'COUPE'),
    (['Acura-TL_Type_S-2008',
      'Buick-Regal_GS-2012',
      'Chrysler-300_SRT_8-2010',
      'Dodge-Charger_SRT_8-2009',], 'SEDAN'),
    (['Chevrolet-HHR_SS-2010',
      'Chevrolet-TrailBlazer_SS-2009',], 'SUV'),
    (['FIAT-500_Abarth-2012',], 'HATCHBACK'),
    (['Ford-Ranger_SuperCab-2011',], 'PICKUP'),
]

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
    
    for tup in corrections:
        for label in tup[0]:
            c = Car.objects.get(label=label)
            c.body_style = tup[1]
            c.save()

def add_car(label):
    c = Car.objects.get_or_create(label=label)[0]
    # print('label:', label)
    label_split = label.split('-')
    make = label_split[0].replace('_', ' ')
    if make == 'Mercedes Benz':
        make = 'Mercedes-Benz'
    # print(make)
    c.make = make
    body_style = 'N/A'
    model = label_split[1].replace('_', ' ')
    try:
        if model.split(' ')[0] in ['Martin', 'Rover']:
            model = ' '.join(model.split(' ')[1:])
        if model.split(' ')[-1].upper() in body_list:
            body_style = model.split(' ')[-1].upper()
            model = ' '.join(model.split(' ')[:-1])
        if model.split(' ')[1].lower() in ['class', 'series']:
            model = '-'.join(model.split(' ')[:2]) +\
            ' ' + ' '.join(model.split(' ')[2:])
            # print('entered class/series loop:', model)
        if model.split(' ')[-1].upper() == 'CAB':
            body_style = 'PICKUP'
    except IndexError:
        pass
    # print(body_style)
    # print('model:', model)
    c.model = model
    c.body_style = body_style
    c.year = label_split[2]
    c.save()

if __name__ == '__main__':
    print('Starting classifier population script')
    populate()
    print('Classifier population script ended')
