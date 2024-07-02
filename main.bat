@echo off
echo Starting the setup process...

cd "%~dp0scripts"

echo Cleaning up old files in the extra folder...
cd extra

for /d %%i in (*) do (
    if /i not "%%i"=="ACPI" if /i not "%%i"=="OCSnapshot" if /i not "%%i"=="Resources" (
        echo Deleting folder: %%i
        rd /s /q "%%i"
    )
)

cd ..
python checkhardware.py
if %errorlevel% neq 0 (
    echo Failed to run checkhardware.py. Exiting...
    exit /b %errorlevel%
)

python testbuildOC.py
if %errorlevel% neq 0 (
    echo Failed to run testbuildOC.py. Exiting...
    exit /b %errorlevel%
)

python testbuildconfig.py
if %errorlevel% neq 0 (
    echo Failed to run testbuildconfig.py. Exiting...
    exit /b %errorlevel%
)

echo Cleaning up remaining files in the extra folder...
cd extra

for /d %%i in (*) do (
    if /i not "%%i"=="ACPI" if /i not "%%i"=="OCSnapshot" if /i not "%%i"=="Resources" if /i not "%%i"=="X64" (
        echo Deleting folder: %%i
        rd /s /q "%%i"
    )
)

cd ..

echo All scripts have been run and cleanup completed successfully. Setup process completed.

pause
