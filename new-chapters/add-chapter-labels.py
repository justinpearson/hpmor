import os, re

for filename in os.listdir('originals'):
    if filename.endswith(".tex"):
        print('Processing ' + filename + '...')
        lines = open('originals/' + filename,'r').readlines()
        with open(filename,'w') as f:
            labeled = False
            for line in lines:
                    n = f.write(line)  # set to n to prevent console output
                    if r'chapter{' in line and not labeled:
                            # todo: delete any non a-zA-Z

                            regex = re.compile('[^a-zA-Z]')
                            # http://stackoverflow.com/questions/22520932/python-remove-all-non-alphabet-chars-from-string
                            #First parameter is the replacement, second parameter is your input string
                            # regex.sub('', 'ab3d*E')
                            #Out: 'abdE'
                            ch_fragment = line.split('{',maxsplit=1)[1]
                            n = f.write('\n\\label{ch-' + regex.sub('',ch_fragment) + '}\n')
                            labeled = True
    else:
        print("File " + filename + " not a .tex file.")


