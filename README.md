# DirectoryManager

**DirectoryManager** is a Python-based program that allows users to interact with files and directories in their file system through a command-line interface.It enables users to create, delete, and rename files and folders.

## Features:

1. **Create Files or Folders**
   - The user can create a new file or folder by providing a name for it.
   - The program checks if a file or folder with the same name already exists to avoid conflicts.

2. **Delete Files or Folders**
   - The user can delete existing files or folders.
   - The program asks for confirmation before deletion to avoid accidental data loss.
   - Folders are deleted along with their contents.

3. **Rename Files or Folders**
   - The user can rename an existing file or folder.
   - The program checks if the element exists before performing the rename operation.

## Requirements:

- Python 3.x
- Libraries:
  - [colorama](https://pypi.org/project/colorama/)
  - [art](https://pypi.org/project/art/)

## Installation
   ```bash
   git clone https://github.com/your-username/DirectoryManager.git
  ```
  ```bash
   pip install -r requirements.txt
  ```

## Usage
  ```bash
  cd DirectoryManager
  ```
  ```bash
  python main.py
  ```

   
