# Lists out the before and after filenames for the user to review before files are actually renamed:

def preview_new_filenames(old_filenames, new_filenames):
    for i in range(len(new_filenames)):
        print(old_filenames[i], '->', new_filenames[i])
    decision = input('Proceed to rename all files? Enter y / n: ')
    while True:
        if decision == 'y':
            return True
        elif decision == 'n':
            return False
        else:
            print('\n >> Invalid Choice, try again. <<\n')

            