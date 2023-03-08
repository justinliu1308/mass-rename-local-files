import os
import re

path = r"C:\Users\justi\Desktop\Python\rename-python-files\old-filenames"
old_filenames = os.listdir(path)
new_filenames = []

# Creating new list of new filenames
for name in old_filenames:
    if '_' in name:         # filename is snake_case
        name = name.replace("_", " ")    
    elif '_' not in name:   # filename is UpperCamelCase
        name = re.sub(r"(\w)([A-Z])", r"\1 \2", name)
        # adds space before each capital letter only if preceeding letter is lowercase
            # changes PhaseTwo to Phase Two
            # changes PhaseII to Phase II and not Phase I I
    else:                   # filename format uncertain
        print(f'The filename "{name}" was not modified due to naming convention not recognized by this program.')
    new_filenames.append(name)

# old filename:
print(old_filenames)
# new filename: 
print(new_filenames)

# Renaming each file in path
# for i in range(len(old_filenames)):
#     os.rename(old_filenames[i], new_filenames[i])