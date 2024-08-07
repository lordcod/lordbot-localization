import orjson
import os
from pathlib import Path


path = Path(__file__).parent.absolute()


languages = ['da', 'de', 'en', 'es', 'fr', 'pl', 'ru', 'tr']

localization_data = {}

for lang in languages:
    with open(os.path.join(path, lang, 'Strings.json'), 'rb') as file:
        print('Process parsing', lang)
        for data in orjson.loads(file.read()):
            key = data['identifier'].strip('"')
            localization_data.setdefault(lang, {})
            localization_data[lang][key] = data['translation']

with open(os.path.join(path,'any_localization.json'), 'wb') as file:
    file.write(orjson.dumps(localization_data))
print('Saved localization')