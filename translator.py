import orjson
languages = ['da', 'de', 'en','es', 'fr','pl', 'ru', 'tr']

localization_data = dict.fromkeys(languages, {})

for lang in  languages:
    with open(f'{lang}/Strings.json', 'rb') as file:
        print(lang)
        for data in orjson.loads(file.read()):
            print(data)
            key = data['identifier'].strip('"')
            print(key)
            localization_data[lang][key] = data['translation']

open('any_localization.json', 'wb').write(orjson.dumps(localization_data))
