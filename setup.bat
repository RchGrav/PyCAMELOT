@echo off
set /p project_path=Enter the path to your project: 
REM Create the virtual environment
python -m venv %project_path%\venv

REM Activate the virtual environment
call %project_path%\venv\Scripts\activate.bat

REM Install pipreqs
pip install pipreqs

REM Generate requirements.txt
pipreqs %project_path%

REM Install requirements
pip install -r %project_path%\requirements.txt

echo.
echo Requirements installed successfully.
pause