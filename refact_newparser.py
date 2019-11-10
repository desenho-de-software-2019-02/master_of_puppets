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

        f = open(filename, 'r+')
        content = f.read()

        ## remove metodos comuns ##
        new_parser = ''
        flag = 0
        for line in content.split('\n'):
            if flag and flag != -1:
                new_parser += line+'\n'
            if 'set_new_parser' in line and flag != -1:
                new_parser += line+'\n'
                flag = 1
            if 'return self.parser' in line:
                flag = -1
        
        content = content.replace(new_parser, '')

        f.close()
        f = open(filename, 'w')
        f.write(content)
        f.close()