from pathlib import Path
from collections import defaultdict
import json

forbidden_files = []

for filename in Path('services').rglob('models/*.py'):
    filename = str(filename)
    if filename not in forbidden_files:
        print("++++++++"+filename+"++++++++")

        name = filename.split('/')[-1].replace('.py', '')
        class_name = ''.join([x.title() for x in name.split('_')])
        print("NOME = " + name)
        print("CLASS_NAME = " + class_name)
        print("+++++++++++++++++++++++++++++++++++++++++++")
        f = open(filename, 'r+')
        content = f.read()

        ## typos ##
        content = content.replace('klass', 'character_class')
        content = content.replace('Klass', 'CharacterClass')
        content = content.replace('costitution', 'constitution')
        content = content.replace('desterity', 'dexterity')

        print('\n\n~~~~~~~~~~~~~~~~~\n\n')
        
        f.close()
        f = open(filename, 'w')
        f.write(content)
        f.close()