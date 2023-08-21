@echo off

echo This program will install all dependencies that you need.
echo The following dependencies are needed: Pip, and OpenCV.

REM Install pip
python -m ensurepip --default-pip
if errorlevel 1 goto error

REM Install OpenCV using pip
python -m pip install opencv-python
if errorlevel 1 goto error

REM Install PIL using pip
python -m pip install pillow
if errorlevel 1 goto error

echo Installation completed successfully.
goto end

:error
echo An error occurred during installation.
pause

:end
pause
