#!/bin/env python2
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4 :
TEMPLATE="""
    grok {{
        match => {{ "description" => "{}" }}
        add_field => {{
            category => "{}"
        }}
    }}
"""

CATEGORIES = {
    'COMIS.DE INTR.': ['banking', 'fees', 'recurring'],
    'PLATA AUTOMATA DOB.': ['banking', 'interest'],
    'IMPOZIT RETINUT': ['tax', 'interest', 'gov'],
    'LUKOIL ': ['gas', 'car', 'transport'],
    'ROUMASPORT SRL ': ['Dechatlon', 'sportsware', 'shopping'],
    'FLORARIA MARIA ': ['flowers', 'gift'],
    'NOBILA CASA ': ['home', 'shopping'],
    'FARMACIA ': ['drugs', 'health'],
    'CARREFOUR ': ['Carrefour', 'groceries', 'shopping', 'supermarket'],
    'ATM ': ['cash'],
    'COMISION': ['banking', 'fees'],
    'Comision': ['banking', 'fees'],
    'PDF ORANGE': ['Orange', 'mobile', 'recurring'],
    'ORANGE-convorbiri mobil': ['Orange', 'mobile', 'recurring'],
    'com PDF ORANGE': ['banking', 'fees', 'recurring'],
    'Schimb valutar': ['banking', 'exchange'],
    'WIZZ AIR ': ['travel', 'plane'],
    'Amazon.com': ['Amazon', 'supermarket', 'shopping'],
    '|takarek': ['savings'],
    'plata consum luna': ['home', 'utilities'],
    '|Lichidare ': ['income'],
    'PRIMARIA MUNICIPIU ': ['local auth', 'taxes', 'gov'],
    'E.ON ENERGIE': ['home', 'utilities', 'heat'],
    'CORA ': ['Cora', 'supermarket', 'shopping', 'groceries'],
    'PIZZA ': ['food', 'restaurant'],
    'MAGAZIN MARIA ': ['fashion', 'shopping'],
    'PAYPAL': ['Paypal', 'supermarket']
}


def generate():
    for match, category in CATEGORIES.items():
        yield TEMPLATE.format(match, ', '.join(category))


if __name__ == "__main__":
    with open('21-categories.gen.conf', 'w+') as conf:
        conf.write('filter {')
        for each in generate():
            conf.write(each)
        conf.write('}\n')
