# rename-filenames
Windows Explorer and the Start Menu are terrible at searching for files unless you remember the exact and complete filename to search for. While VScode is much better at this, 

main.py renames all local snake_case and UpperCamelCase Python filenames to a consistent Windows-searchable and human-friendly naming convention, Title Case. Or more accurately in this case, what the result of the Python function title() would be:
- Official Title Case naming convention: 'The Name of the File.txt'
- title() and also my desired naming convention: 'The Name Of The File.txt'

## Why is this useful?
My hundreds of Python files were named using either snake case or upper camel case, and I later discovered Windows cannot search filenames using the latter convention. With so many files where I only remember keywords in the filename, I was wasting time searching for files. See the below Windows 11 example.

Local directory:
![alt text](https://github.com/justinliu1308/rename-python-files/blob/main/directory-screenshot.png)

To search for a file successfully, you need to remember the start of the filename or the full filename entirely:
![alt text](https://github.com/justinliu1308/rename-python-files/blob/main/working-search-1.png)

Otherwise, the search fails:
![alt text](https://github.com/justinliu1308/rename-python-files/blob/main/failed-search-1.png)





12/6/22: Realized Windows Explorer can't search for words if they're not separated by a space or underscore or at the start of the file name.

Creating this script to rename all of my hundreds of Python scripts to searchable names
