# Lists out the before and after filenames for the user to review before files are actually renamed:

def preview_new_filenames(old_filenames, new_filenames):
    count = 0
    print("\n  Preview:")  
    for i in range(len(new_filenames)):
        if new_filenames[i] == 'no_change':
            print(f'{old_filenames[i]} will not be modified (naming convention not recognized by this program).')
        else:
            print(old_filenames[i], '  --->  ', new_filenames[i])
            count += 1
    while True:
        decision = input('\nProceed to rename all files? Enter y / n: ')
        if decision == 'y':
            return True, count
        elif decision == 'n':
            return False, 0
        else:
            print('\n >> Invalid Choice, try again. <<')

