"""
Patches a repo index.rst into the system top index.rst.
"""

import sys, os

dict_ = {
    'hdl': 'HDL',
    'no-os': 'no-OS',
    'doctools': 'Doc Tools',
    'documentation': 'System Level',
}

name = sys.argv[1]
if name not in dict_:
    sys.exit(f"Error: {name} not known.")

if name == "no-os":
    file = f"repos/{name}/doc/sphinx/source/index.rst"
else:
    file = f"repos/{name}/docs/index.rst"
if not os.path.isfile(file):
    sys.exit(f"Error: {file} does not exist")

toctree = []
print(file)
with open(file, "r") as f:
    data = f.readlines()

    if ".. toctree::\n" not in data:
        sys.exit(-1)

    in_toc = False
    print("getting")
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
print(toctree)
file = sys.argv[2]
if not os.path.isfile(file):
    sys.exit(f"Error: {file} does not exist")

with open(file, "r") as f:
    data_ = f.readlines()
    # Find end of toctree
    if ".. toctree::\n" in data_:
        i = data_.index(".. toctree::\n")
        for i in range(i + 1, len(data_)):
            if data_[i][0:3] != '   ' and data_[i] != '\n':
                break
    else:
        i = len(data_) - 1

    header = data_[:i]
    body = data_[i:]

    for tc in toctree:
        header.extend(data[tc[0]:tc[1]])
        header.append('\n')

    header.extend(body)

with open(file, "w") as f:
    for line in header:
        f.write(line)
