test_dict = {
    'name': 'Tim',
    'age': 30,
    'loca': 'Dallas',    
}
print(test_dict['age'])
print(test_dict['name'])
test_dict['job'] = 'SW Dev'
print(test_dict['job'])
test_dict['age'] = 31
print(list(test_dict.keys()))
print(list(test_dict.values()))

#-------------------------------

class_25 = {
    'stu1': {
        'name': 'Alice',
        'grade': 75,
        'phone': '281-330-8004',
        'address': {
            'street': '1215 Fake St.',
            'citystate': 'Dallas, TX',
            'zip': '75126',
        }
    },
    'stu2':{  
        'name': 'Bob',
        'grade': 85,
        'phone': '281-867-5309',
        'address': {
            'street': '1120 Not Real Rd.',
            'citystate': 'Boston, MS',
            'zip': '65487',
        }
    },
        'stu3':{  
        'name': 'Lemmy',
        'grade': 10,
        'phone': 'n/a',
        'address': {
            'street': '2525 West Ave',
            'citystate': 'Seattle, WS',
            'zip': '90210',
        }
    },
}

print(f'{class_25['stu2'].get('name')} {class_25['stu2'].get('address')}')
