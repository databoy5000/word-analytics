import os
import json
from modules import main_package

documents = os.listdir('./assets')
documents.sort()

output_filename = 'words_data.json'
output_path = f'./data/{output_filename}'

words_data = main_package.get_data(documents)

with open(output_path, 'w') as outfile:
    json.dump(words_data, outfile)