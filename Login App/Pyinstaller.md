# Creating an Executable Application using Pyinstaller
#### If you want to convert the Python script into an executable file, you can use PyInstaller. Follow these steps:

## Prerequisites:
* Ensure PyInstaller is installed. You can install it using pip:
   ```bash
   python -m pip install pyinstaller
   ```
### Generating the Executable:
1. Open the Command Prompt or terminal and navigate to the directory where your Python script is located.
2. Run the following command: 
  ```bash
    pyinstaller --add-data "path to opencv":"cv2" --add-data "path to pillow":"PIL" --add-data "path to sqlite3":"sqlite3" Login_App.py
  ``` 
  Replace **path to** with the actual path to the module on your system.<br>
*or*<br>
**Refer ``` pyinstaller.txt```** 

3. The **Login_App.py** file will be converted into an executable. After the process completes:
   * The executable will be located in the dist folder of the project directory.
   * Additional files might appear in the build folder.
  
### Project Directory Structure After Generating Executable
```
  Login App/
  ├── Login_App.py
  ├── requirements.txt
  ├── Login_App.spec
  ├── build/
        └── .....
  ├── dist/
        └── Login_App/
                  └── _internal
                  └── Login_App.exe
  
  ```
### Running the Executable:
   * Navigate to the dist folder:
     ```bash
     cd dist/Login_App
     ```
   * Run the executable:
     ```bash
     Login_App.exe
     ```


## Important Note:
1. Ensure that all required modules *(e.g., cv2, PIL, Sqlite)* are properly installed in your Python environment before creating the executable.
2. If you're using a virtual environment, specify the correct paths to the libraries in the *--add-data* flags.
