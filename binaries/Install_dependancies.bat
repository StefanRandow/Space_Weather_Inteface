@echo off

echo This program will install all dependencies that you need.
echo The following dependencies are needed: Pip, Pillow and OpenCV.

REM Install pip
python -m ensurepip --default-pip
if errorlevel 1 goto error

REM Install OpenCV using pip
python -m pip install opencv-python
if errorlevel 1 goto error

echo Installation completed successfully.
goto end

:error
echo An error occurred during installation.
pause

:end

rem Set the path to the Space-Weather-Interface folder
set "swi_folder=%~dp0.."

rem Set the path to the target file
set "target_file=%~dp0Space_Weather_Interface.bat"

rem Set the path to the shortcut file
set "shortcut_file=%swi_folder%\Space_Weather_interface.lnk"

rem Create the VBScript file
echo Set WshShell = CreateObject("WScript.Shell") > create_shortcut.vbs
echo Set objShortcut = WshShell.CreateShortcut("%shortcut_file%") >> create_shortcut.vbs
echo objShortcut.TargetPath = "%target_file%" >> create_shortcut.vbs
echo objShortcut.IconLocation = "%swi_folder%\images\icon\icon.ico%" >> create_shortcut.vbs
echo objShortcut.Save >> create_shortcut.vbs
echo WScript.Echo "Shortcut created: " ^& "%shortcut_file%" >> create_shortcut.vbs

rem Run the VBScript file
cscript //nologo create_shortcut.vbs

rem Delete the VBScript file
del create_shortcut.vbs

echo VBScript file executed and deleted.

cd ..
del setup.bat

pause
