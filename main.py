import requests
import argparse
import sys

def get_weather(*locations, lang='en', options='nTqu', host='wttr.in') -> str:
    '''
    Возвращает погоду в текстовой псевдографике
    options - https://wttr.in/:help
    '''
    payload = {'lang': lang, **{option: '' for option in options}}
    text = []

    for location in locations:
        url = f'https://{host}/{location}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        text.append(response.text)

    return '\n'.join(text)


def modifies_text(text):
    '''
    Убирает коипирайт-строку
    Добавляет заголовок по центру с названием локации
    '''
    bad_line = 'Все новые фичи публикуются здесь'
    header = 'Прогноз погоды:'
    char_pad = '='
    mod_text = []

    for line in text.split('\n'):
        if line.startswith(bad_line):
            continue
        elif line.startswith(header):
            location = line.split(':')[1].strip().capitalize()
            header_mod = get_padding(char_pad=char_pad, string=location)
            mod_text.append(header_mod)
        else:
            mod_text.append(line)
    return '\n'.join(mod_text)

def get_parser():
    '''
    Парсит параметры командной строки и возвращает объект парсера
    '''

    # Default values
    dflt_opt = 'nM'
    dflt_lang = 'ru'

    parser = argparse.ArgumentParser(description='Show weather from https://wttr.in')
    parser.add_argument('locations', nargs='+', help='locations one or more')
    parser.add_argument('--options', default=dflt_opt, help=f'See https://wttr.in/:help Default: {dflt_opt}')
    parser.add_argument('--lang', default=dflt_lang, help=f'Language. See https://wttr.in/:help Default: {dflt_lang}')

    return parser.parse_args()

def main():

    args = get_parser()

    text = get_weather(*args.locations, lang=args.lang, options=args.options)
    print(text)

if __name__ == '__main__':
    main()

