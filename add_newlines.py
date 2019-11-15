from pathlib import Path

for filename in Path('services').rglob('*.py'):
    filename = str(filename)
    print("++++++++"+filename+"++++++++")

    f = open(filename, 'r+')
    content = f.read()

    keywords = ['return', 'class', 'pass']
    result = ''
    for line in content.split('\n'):
        result += line+'\n'
        for k in keywords:
            if k in line:
                result+='\n'
    result = result.replace('\n\n\n\n', '\n\n\n')
    print(result)
    f.close()
    f = open(filename, 'w')
    f.write(result)
    f.close() 