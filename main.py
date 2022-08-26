import requests
import argparse

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



def get_parser():
    '''
    Парсит параметры командной строки и возвращает объект парсера
    '''
    parser = argparse.ArgumentParser(description='Show weather from https://wttr.in')
    parser.add_argument('locations', nargs='+', help='locations one or more')
    parser.add_argument('--options', default='nTqM', help='See https://wttr.in/:help. Default: "nTqM"')
    parser.add_argument('--lang', default='ru', help='Language. See https://wttr.in/:help. Default: "ru"')

    return parser.parse_args()

def main():

    args = get_parser()

    get_weather(*args.locations, lang=args.lang, options=args.options)

if __name__ == '__main__':
    main()

