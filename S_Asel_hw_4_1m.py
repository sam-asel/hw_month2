study = {'name':'GeekTech',
        'address':['Токтогула 175'],
        'courses': ['Android','Backend', 'Frontend'],
        'bag': {'fails', 'errors', 'stack'}
}
del study['bag']

study['address'] = "Ибраимова 103"
study['instagramm'] = '@geektech_kg'
study['phone'] = '0557 052 018'

study['courses'].extend(['english', 'ios', 'Ux/Ui', ])
study['courses'] = tuple(study['courses'])


for k,v in study.items():
    print(f'{k}:{v}')


