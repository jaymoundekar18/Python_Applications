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
    pyinstaller --add-data "path to opencv":"cv2" --add-data "path to facenet_pytorch":"facenet_pytorch" --add-data "path to pillow":"PIL" Face_Extraction.py
  ``` 
  Replace **path to** with the actual path to the module on your system.<br>
*or*<br>
**Refer** ``` pyinstaller.txt```

3. The **Face_Extraction.py** file will be converted into an executable. After the process completes:
   * The executable will be located in the dist folder of the project directory.
   * Additional files might appear in the build folder.
  
### Project Directory Structure After Generating Executable
```
  Face Extraction/
  ├── Face_Extraction.py
  ├── requirements.txt
  ├── Face_Extraction.spec
  ├── build/
        └── .....
  ├── dist/
        └── Face_Extraction/
                  └── _internal
                  └── Face_Extraction.exe
  
  ```
### Running the Executable:
   * Navigate to the dist folder:
     ```bash
     cd dist/Face_Extraction
     ```
   * Run the executable:
     ```bash
     Face_Extraction.exe
     ```


## Important Note:
1. Ensure that all required modules *(e.g., cv2, facenet_pytorch, PIL)* are properly installed in your Python environment before creating the executable.
2. If you're using a virtual environment, specify the correct paths to the libraries in the *--add-data* flags.
