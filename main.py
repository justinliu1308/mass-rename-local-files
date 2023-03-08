import os, re
path = ""
old_filenames = os.listdir(path)
new_filenames = []

# Creating new list of new filenames
for name in old_filenames:
    if '_' in name:         # filename is snake_case
        name = name.replace("_", " ")    
    elif '_' not in name:   # filename is UpperCamelCase
        name = re.sub(r"(\w)([A-Z])", r"\1 \2", name)   # adds space before each capital letter
    else:                   # filename format uncertain
        pass
    print(name)
    new_filenames.append(name)

# old filename:
print(old_filenames)
# new filename: 
print(new_filenames)

# Renaming each file in path
# for i in range(len(old_filenames)):
#     os.rename(old_filenames[i], new_filenames[i])