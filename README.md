# rename-python-files
main.py renames all local snake_case and UpperCamelCase Python filenames to a consistent Windows-searchable and human-friendly naming convention (Title Case, or more accurately in this case, what the result of the Python function title() is.)

The need for this is as follows:

12/6/22: Realized Windows Explorer can't search for words if they're not separated by a space or underscore or at the start of the file name.

Creating this script to rename all of my hundreds of Python scripts to searchable names