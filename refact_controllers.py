from pathlib import Path
from collections import defaultdict
import json

def format_parser(parser):
        parse = ''
        ident = ''
        for k in json.dumps(parser, indent=4, sort_keys=True).split('\n'):
            if ('{' not in k) and ('}' not in k):
                parse += k.replace('    "', '').replace(': 1','').replace(')",', ')').replace(' ",', '').replace('"', '')+'\n'
                ident = parse.split('parser')[0]
        
        half_ident = ident[0:len(ident)//2]
        parse = parse.replace('parser', 'self.parser')
        
        return parse, ident, half_ident
        
forbidden_files = ['services/base_controller.py', 'services/resources/controller/dice_controller.py', 'services/resources/controller/attribute_controller.py']

for filename in Path('services').rglob('*_controller.py'):
    filename = str(filename)
    if filename not in forbidden_files:
        print("++++++++"+filename+"++++++++")

        name = filename.split('/')[-1].replace('_controller.py', '')
        class_name = ''.join([x.title() for x in name.split('_')])
        cn_controller = class_name+'Controller'

        f = open(filename, 'r+')
        content = f.read()
        content = content.replace('from json import dumps, loads', '')
        content = content.replace(f'from models.{name} import {class_name}\n', 'from services.base_controller import BaseController\n')
           

        ## typos ##
        content = content.replace('klass', 'character_class')
        content = content.replace('Klass', 'CharacterClass')
        content = content.replace('costitution', 'constitution')
        content = content.replace('desterity', 'dexterity')
        
        
        ## parser do new ##
        new_parser = defaultdict(lambda: 0)
        flag = 0
        for line in content.split('\n'):
            if 'def new(self):' in line:
                flag = 1
            if 'parse_result' in line:
                flag = 0
            if flag and ('parser' in line):
                new_parser[line]=1
                
        ## parser do edit ##
        edit_parser = defaultdict(lambda: 0)
        flag = 0
        for line in content.split('\n'):
            if 'def edit(self, identifier):' in line:
                flag = 1
            if 'parse_result' in line:
                flag = 0
            if flag and ('parser' in line):
                edit_parser[line]=1
                

        ## remove metodos comuns ##
        common_methods = ''
        flag = 0
        for line in content.split('\n'):
            if flag and flag != -1:
                common_methods += line+'\n'
            if 'init' in line and flag != -1:
                common_methods += line+'\n'
                flag = 1
            if 'return target_data' in line:
                flag = -1
        
        content = content.replace(common_methods, '')
        
        
        
        ## add set_parser + basecontroller ##
        new_parse, ident, half_ident = format_parser(new_parser)
        edit_parse, ident, half_ident = format_parser(edit_parser)

        def_new_pars = half_ident+'def set_new_parser(self):\n' 
        def_edit_pars = half_ident+'def set_edit_parser(self):\n' 
        ret_pars = ident+'return self.parser\n'
        
        new_parse = def_new_pars+new_parse+'\n'+ret_pars+'\n\n'
        edit_parse = def_edit_pars+edit_parse+'\n'+ret_pars+'\n\n'
        
        content = content.replace(f'class {cn_controller}:', f'class {cn_controller}(BaseController):\n{new_parse}{edit_parse}') 
        
        #print (content)
        #print("\n\n\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n\n\n")
        #print(json.dumps(parser, indent=4, sort_keys=True))
        f.close()
        f = open(filename, 'w')
        f.write(content)
        f.close()