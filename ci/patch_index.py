"""
Patches a repo index.rst into the system top index.rst.
"""

import sys, os

dict_ = {
    'hdl': 'HDL',
    'doctools': 'Doc Tools',
}

name = sys.argv[1]
if name not in dict_:
    sys.exit(f"Error: {name} not known.")

file = f"repos/{name}/docs/index.rst"
if not os.path.isfile(file):
    sys.exit(f"Error: {file} does not exist")

toctree = []
with open(file, "r") as f:
    data = f.readlines()

    if ".. toctree::\n" not in data:
        sys.exit(-1)

    in_toc = False
    for i in range(0, len(data)):
        if in_toc:
            if data[i][0:12] == '   :caption:':
                data[i] = f"{data[i][0:12]} {dict_[name]}{data[i][12:]}"
                continue

            if data[i][0:3] == '   ' and data[i][0:4] != '   :':
                pos  = data[i].find('<')
                if pos == -1:
                    data[i] = f"   {name}/{data[i][3:]}"
                else:
                    data[i] = f"{data[i][:pos+1]}{name}/{data[i][pos+1:]}"

            if data[i][0:3] != '   ' and data[i] != '\n':
                toctree[-1] = [toctree[-1][0], i - 1]
                if data[i] == ".. toctree::\n":
                    toctree.append([i,i])
                else:
                    in_toc = False
                continue
        else:
            if data[i] == ".. toctree::\n":
                toctree.append([i,i])
                in_toc = True

file = sys.argv[2]
if not os.path.isfile(file):
    sys.exit(f"Error: {file} does not exist")

with open(file, "r") as f:
    data_ = f.readlines()
    # Find end of toctree
    i = data_.index(".. toctree::\n")
    for i in range(i + 1, len(data_)):
        if data_[i][0:3] != '   ' and data_[i] != '\n':
            break

    header = data_[:i]
    body = data_[i:]

    for tc in toctree:
        header.extend(data[tc[0]:tc[1]])
        header.append('\n')

    header.extend(body)

with open(file, "w") as f:
    for line in header:
        f.write(line)
