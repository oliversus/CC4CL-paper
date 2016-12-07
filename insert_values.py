#!/data/osus/Enthought/User/bin/python

import glob
import re
import os

path = '/cmsaf/esa_doku/ESA_Cloud_cci/publications/CC4CL_paper/'
variables = []
with open(path + 'latex_variables.txt') as f:
    for line in f:
        variables.append(line.split("="))

for tex in glob.glob(path + "*.tex"):
    with open(os.path.splitext(tex)[0] + "_test.tex", 'w') as new_f:
        with open(tex, 'r') as f:
            for line in f:
                if re.search('insertVariable{.*}[0-9]*\.{1}[0-9]*', line):
                    for word in line.split():
                        m = re.search('insertVariable{.*}[0-9]*\.{1}[0-9]*', word)
                        if m:
                            found = m.group()
                            variable, value = variables[[i for i, x in enumerate(variables) if x[0] in found][0]]
                            value_new = value.strip('\n')
                            value_old = re.search('[0-9]*\.[0-9]*', found).group()
                            replace = found.replace(value_old, value_new)
                            line = line.replace(found, replace)
                            # new_f.write(line_new)
                        #else:
                new_f.write(line)

    #os.remove(tex)
    #os.rename(os.path.splitext(tex)[0] + "_test.tex", tex)





