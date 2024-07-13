import orjson
languages = ['da', 'de', 'en','es', 'fr','pl', 'ru', 'tr']

localization_data = {}

for lang in  languages:
    with open(f'{lang}/Strings.json', 'rb') as file:
        print(f'{lang}/Strings.json', lang, file)
        for data in orjson.loads(file.read()):
            key = data['identifier'].strip('"')
            localization_data.setdefault(lang, {})
            localization_data[lang][key] = data['translation']

open('any_localization.json', 'wb').write(orjson.dumps(localization_data))

