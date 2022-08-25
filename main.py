import requests


def get_weather(*cities, lang='en', options='nTqu'):
    '''
    Печатает погоду переданных городов на консоль
    opt - https://wttr.in/:help
    '''
    host = 'wttr.in'
    payload = {'lang': lang, **{option: '' for option in options}}

    for city in cities:
        url = f'https://{host}/{city}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print('='*80)
        print(response.text)


if __name__ == '__main__':

    cities = ('Шереметьево',
              'Череповец',
              'Лондон')

    get_weather(*cities, lang='ru', options='nTqmM')

