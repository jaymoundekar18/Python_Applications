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
    pyinstaller --add-data "path to deep_translator":"deep_translator" Text_Translator.py
  ``` 
  Replace **path to** with the actual path to the module on your system.<br>
*or*<br>
**Refer ``` pyinstaller.txt```** 

3. The **Text_Translator.py** file will be converted into an executable. After the process completes:
   * The executable will be located in the dist folder of the project directory.
   * Additional files might appear in the build folder.
  
### Project Directory Structure After Generating Executable
```
  Text Translator/
  ├── Text_Translator.py
  ├── requirements.txt
  ├── Text_Translator.spec
  ├── build/
        └── .....
  ├── dist/
        └── Text_Translator/
                  └── _internal
                  └── Text_Translator.exe
  
  ```
### Running the Executable:
   * Navigate to the dist folder:
     ```bash
     cd dist/Text_Translator
     ```
   * Run the executable:
     ```bash
     Text_Translator.exe
     ```


## Important Note:
Ensure that all required modules *(e.g., deep_translator)* are properly installed in your Python environment before creating the executable.
