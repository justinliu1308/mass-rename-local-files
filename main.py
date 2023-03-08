import os
import re
from preview_output import preview_new_filenames

path = r"C:\Users\justi\Desktop\Python\mass_rename_local_files\old_filenames"
old_filenames = os.listdir(path)

def generate_new_filenames(old_filenames):
    # Creates list of new filenames
    new_filenames = []
    for name in old_filenames:
        # If filename is snake_case
        if '_' in name:         
            name = name.replace("_", " ")    
        # If filename is UpperCamelCase
        elif '_' not in name and '-' not in name:
            name = re.sub(r"(\w)([A-Z])", r"\1 \2", name)
            # adds space before each capital letter ONLY if preceeding letter is lowercase
                # changes 'PhaseTwo' to 'Phase Two'
                # changes 'PhaseII' to 'Phase II' and not 'Phase I I'
        # Filename format uncertain
        else:
            name = 'no_change'
        new_filenames.append(name)
    return new_filenames

def rename_files(old_filenames, new_filenames):
    # Renaming each file in path
    for i in range(len(old_filenames)):
        if new_filenames[i] == 'no_change':
            continue
        else:
            os.rename(old_filenames[i], new_filenames[i])
                 
if __name__ == "__main__":
    new_filenames = generate_new_filenames(old_filenames)
    action, count = preview_new_filenames(old_filenames, new_filenames)
    if action == True:
        rename_files(old_filenames, new_filenames)
        if count == 1:
            print(f'{count} file renamed.')
        else:
            print(f'{count} files renamed.')
