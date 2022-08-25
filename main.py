import requests


def get_weather(*locations, lang='en', options='nTqu'):
    '''
    Печатает погоду переданных городов на консоль
    options - https://wttr.in/:help
    '''
    host = 'wttr.in'
    payload = {'lang': lang, **{option: '' for option in options}}

    for location in locations:
        url = f'https://{host}/{location}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print('='*80)
        print(response.text)


if __name__ == '__main__':

    locations = ('Шереметьево',
                 'Череповец',
                 'Лондон')

    get_weather(*locations, lang='ru', options='nTqM')

