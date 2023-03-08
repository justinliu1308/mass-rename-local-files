# mass-rename-local-files
Windows Explorer and the Start Menu are terrible at searching for files unless you remember the exact and complete filename to search for. While VScode doesn't have a problem with this if you search there, you may find a need to rename all your files for other organizational reasons.

main.py renames all local snake_case and UpperCamelCase Python filenames to a consistent Windows-searchable and human-friendly naming convention: Title Case. Or more specifically in this script, what the result of the Python function title() would be.
- Official Title Case naming convention: 'The Name of the File.txt'
- title() and the output naming convention here: 'The Name Of The File.txt'

## Usage
1. Set the 'path' variable in main.py to your local path containing files to be renamed
2. In the terminal, navigate to the same path
3. Run main.py

## Why is this made?
On my local drive, I had hundreds of Python files named using either snake case or upper camel case, and I was wasting time searching for files on Windows if I didn't have VS Code open. A small issue, but easy to fix. See the below Windows 11 example.

Local directory:
![alt text](https://github.com/justinliu1308/rename-python-files/blob/main/directory-screenshot.png)

To search for a camel-case-named file successfully, you need to remember the start of the filename or the full filename entirely:
![alt text](https://github.com/justinliu1308/rename-python-files/blob/main/working-search-1.png)

Otherwise, the search fails:
![alt text](https://github.com/justinliu1308/rename-python-files/blob/main/failed-search-1.png)
