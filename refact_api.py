from pathlib import Path
from collections import defaultdict
import json
        
forbidden_files = ['services/resources/views/dice_api.py', 'services/resources/views/attribute_api.py']

for filename in Path('services').rglob('*_api.py'):
    filename = str(filename)
    if filename not in forbidden_files:
        print("++++++++"+filename+"++++++++")

        name = filename.split('/')[-1].replace('_api.py', '')
        class_name = ''.join([x.title() for x in name.split('_')])
        print("NOME = " + name)
        print("CLASS_NAME = " + class_name)
        print("+++++++++++++++++++++++++++++++++++++++++++")
        f = open(filename, 'r+')
        content = f.read()
#        content = content.replace('api = Namespace(', f'from models.{name} import {class_name}\nfrom services.base_controller import Context\napi = Namespace(')
        
        new_controller = f'controller = {class_name}Controller(model={class_name}, request=request)'
        old_controller = f'controller = BaseController(strategy={class_name}Controller(), model={class_name}, request=request)'

        content = content.replace(old_controller, new_controller)        
#        content = content.replace('namespace\')\n', f'namespace\')\n{get_controller}')
#        content = content.replace('instance', 'controller')
#        content = content.replace(f'controller = {class_name}Controller(request)', 'controller = get_controller()')

        ## typos ##
#        content = content.replace('klass', 'character_class')
#        content = content.replace('Klass', 'CharacterClass')
#        content = content.replace('costitution', 'constitution')
#        content = content.replace('desterity', 'dexterity')

        #print(content)

        print('\n\n~~~~~~~~~~~~~~~~~\n\n')
        
        f.close()
        f = open(filename, 'w')
        f.write(content)
        f.close()