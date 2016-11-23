#!/bin/env python2
# -*- mode: Python; tab-width: 4; indent-tabs-mode: nil; -*-
# ex: set tabstop=4 :
"""
 Generate logstash config to categorize expenses.
 Likely to require customization.
"""

TEMPLATE = """
    grok {{
        match => {{ "{}" => "{}" }}
        add_field => {{
            category => "{}"
        }}
    }}
"""

CATEGORIES = {
    "description": {
        'COMIS.DE INTR.': ['banking', 'fees', 'recurring'],
        'Taxa anuala card': ['banking', 'fees', 'recurring'],
        'PLATA AUTOMATA DOB.': ['banking', 'interest'],
        'IMPOZIT RETINUT': ['tax', 'interest', 'gov'],
        'COMISION': ['banking', 'fees'],
        'Comision': ['banking', 'fees'],
        'Schimb valutar': ['banking', 'exchange'],
        'com PDF ORANGE': ['banking', 'fees', 'recurring'],
        'PRIMARIA MUNICIPIU': ['local auth', 'taxes', 'gov'],
        'CAS pers. fizice': ['taxes', 'gov'],
        'bugetul de stat': ['taxes', 'gov'],

        'LUKOIL ': ['gas', 'car', 'transport'],
        'OMV ': ['gas', 'car', 'transport'],
        'MOL ': ['gas', 'car', 'transport'],
        'SHELL ': ['gas', 'car', 'transport'],
        'CRODUX ': ['gas', 'car', 'transport'],
        'UBER ': ['Uber', 'transport'],
        'HRVATSKE AUTOCESTE ': ['roadtax', 'transport'],

        'ALLIANZTIRIAC': ['insurrance'],

        'ROUMASPORT SRL ': ['Dechatlon', 'sportsware', 'shopping'],
        'HERVIS SPORTS ': ['Hervis', 'sportsware', 'shopping'],
        'INTERSPORT': ['Intersport', 'sportsware', 'shopping'],
        'Adidas ': ['sportsware', 'shopping'],
        'ADIDAS ': ['sportsware', 'shopping'],

        'FLORARIA MARIA ': ['flowers', 'gift'],
        'ALEFLOR ': ['flowers', 'gift'],
        'ANA FLOR ': ['flowers', 'gift'],

        'NOBILA CASA ': ['home', 'shopping'],
        'DIEGO ': ['home', 'shopping'],
        'IKEA ': ['Ikea', 'home', 'shopping'],
        'LEROY MERLIN ': ['home', 'shopping'],
        'KIKA ': ['Kika', 'home', 'shopping'],
        'DEDEMAN ': ['Dedeman', 'home', 'shopping'],
        'JYSK ': ['home', 'shopping'],
        'LAVANDA HOUSE ': ['home', 'shopping'],

        'FARMACIA ': ['drugs', 'health'],
        'VITAFARM ': ['drugs', 'health'],
        'ELMAFARM ': ['drugs', 'health'],
        'DUCFARM ': ['drugs', 'health'],
        'NOVOGYNPRO ': ['health'],
        'PROMEDICAL ': ['health'],
        'MEDICO CHIRURGICAL ': ['health'],
        'CABINET OFTA ': ['health', 'vision'],
        'CRYSTAL OPTIC ': ['health', 'vision'],

        'CARREFOUR ': ['Carrefour', 'groceries', 'shopping', 'supermarket'],
        'PROFI MAG': ['groceries', 'Profi'],
        'AUCHAN ': ['groceries', 'Auchan', 'supermarket', 'shopping'],
        'PBZTKONZUM ': ['groceries', 'Konzum', 'supermarket', 'shopping'],
        'KONZUM ': ['groceries', 'Konzum', 'supermarket', 'shopping'],
        'SPAR ': ['groceries', 'Spar', 'supermarket', 'shopping'],
        'LIDL ': ['groceries', 'Lidl', 'supermarket', 'shopping'],
        'BILLA ': ['groceries', 'Billa', 'supermarket', 'shopping'],
        'KAUFLAND ': ['groceries', 'Kaufland', 'supermarket', 'shopping'],
        'CORA ': ['Cora', 'supermarket', 'shopping', 'groceries'],
        'TESCO ': ['Tesco', 'supermarket', 'shopping', 'groceries'],
        'SELGROS ': ['Selgros', 'supermarket', 'shopping', 'groceries'],
        'DM ': ['dm', 'shopping'],

        'ATM ': ['cash'],
        'AG HERMES': ['cash'],


        'WIZZ AIR ': ['travel', 'plane'],
        'Hotel on Booking.com': ['travel', 'accomodation'],

        'E.ON ENERGIE': ['home', 'utilities', 'heat'],
        'AFEE CLUJ MOBILPAY MUNICIPIUL ': ['home', 'utilities', 'electric'],
        'cod client [0-9]+ |NLC ': ['home', 'utilities', 'electric'],
        'WWW.MYLINE-EON.RO': ['home', 'utilities', 'heat'],
        'CPO ': ['home', 'utilities', 'water'],

        'Suma originala [0-9.]+ HUF': ['hungary'],
        'Suma originala [0-9.]+ USD': ['usa'],
        'Suma originala [0-9.]+ EUR': ['europe'],
        'Suma originala [0-9.]+ HRD': ['croatia'],


        'GOOGLE *Google Storage': ['recurring', 'Google', 'it'],
        'Amazon web services': ['Amazon', 'it'],
        'g.co/payhelp': ['Google', 'recurring'],
        'PDF ORANGE': ['Orange', 'mobile', 'recurring'],
        'ORANGE.RO': ['Orange', 'mobile', 'recurring'],
        'TELEKOM.RO ': ['Telekom', 'internet', 'recurring'],
        'ORANGE-convorbiri mobil': ['Orange', 'mobile', 'recurring'],
        'DirectDebit ORANGE': ['Orange', 'mobile', 'recurring'],
        'DIGICARE.RCS-RDS.RO': ['Digi', 'mobile', 'recurring', 'internet'],
        'CODE 42 SOFTWARE': ['Crashplan', 'recurring', 'it'],

        'MAGAZIN MARIA ': ['fashion', 'shopping'],
        ' ORSAY ': ['fashion', 'shopping'],
        'COCCODRILLO ': ['fashion', 'shopping'],
        'H&M ': ['fashion', 'shopping'],
        'H & M ': ['fashion', 'shopping'],
        'LACE WORLD ': ['fashion', 'shopping'],
        'NEXTDIRECTORY': ['fashion', 'shopping'],
        'C & A Moda': ['fashion', 'shopping'],
        'C&A MODA': ['fashion', 'shopping'],
        'LC WAIKIKI': ['fashion', 'shopping'],
        'PEPCO ': ['fashion', 'shopping'],
        'OUT WEAR ': ['fashion', 'shopping'],
        'ZARA ': ['fashion', 'shopping'],
        'TOM TAILOR ': ['fashion', 'shopping'],
        'HEAVY TOOLS ': ['fashion', 'shopping'],
        'RESERVED ': ['fashion', 'shopping'],
        'LEE COOPER ': ['fashion', 'shopping'],
        'JOLIDON ': ['fashion', 'shopping'],
        'CAMAIEU MODA ': ['fashion', 'shopping'],
        'ANDU ': ['fashion', 'shopping'],
        'KIK ': ['fashion', 'shopping'],
        'PIMKIE ': ['fashion', 'shopping'],
        'PENTI ': ['fashion', 'shopping'],

        'Deichmann ': ['shoes', 'shopping'],
        'BENVENUTI ': ['shoes', 'shopping'],
        'GEOX ': ['shoes', 'shopping'],
        'HUMANIC ': ['shoes', 'shopping'],
        'MAGAZIN BIGSTEP ': ['shoes', 'shopping'],

        'DINOLAND ': ['toys', 'shopping'],
        'NORIELTOYS ': ['toys', 'shopping'],

        'PIZZA ': ['food', 'restaurant'],
        'ENGELS BISTRO ': ['food', 'restaurant'],
        'HORA ': ['food', 'restaurant'],
        'MATEI CORVIN ': ['food', 'restaurant'],
        'ROATA FAGET ': ['food', 'restaurant'],
        'EXPRES CATERING ': ['food', 'restaurant'],
        'PANEMAR MORARIT ': ['groceries', 'food'],
        'MADO ': ['food', 'fastfood'],
        'DELICIU CARTOFILOR ': ['food', 'fastfood'],
        'PAPRIKA ': ['food', 'fastfood'],
        'COSM FAN ': ['food', 'meat'],

        'PAYPAL': ['Paypal', 'supermarket'],
        'Amazon.com': ['Amazon', 'supermarket', 'shopping'],
        'garagemal': ['GarageMall', 'supermarket', 'shopping'],
        'ALTEX ': ['Altex', 'supermarket', 'shopping'],
        'EMAG.RO ': ['eMag', 'supermarket', 'shopping'],
        'eMAG ': ['eMag', 'supermarket', 'shopping'],
        'pcgarage': ['PcGarage', 'shopping', 'it'],
        'AMAZON SERVICES-KINDLE': ['Amazon', 'books', 'education'],
        'Amazon Services-Kindle': ['Amazon', 'books', 'education'],

    },
    "to_from_account": {
        'RO68RZBR0000010012852302': ['savings', 'internal'],
        'RO34CITI0000000724821022': ['income', 'hp'],
        'RO67BTRL01301205R83284XX': ['home', 'utilities'],
        'RO86RZBR0000060010893012': ['home', 'utilities', 'trash', 'recurring'],
    }
}


def generate():
    """ Generate the config from the global CATEGORIES dict """
    for field, matches in CATEGORIES.items():
        for match, category in matches.items():
            yield TEMPLATE.format(field, match, ', '.join(category))


if __name__ == "__main__":
    with open('logstash.conf.d/21-categories.gen.conf', 'w+') as conf:
        conf.write('filter {')
        for each in generate():
            conf.write(each)
        conf.write('}\n')
