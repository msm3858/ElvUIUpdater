echo "Current working directory: %cd%"
call %cd%\venv\Scripts\activate.bat
call python main.py -b "D:\\BlizzardLibrary\\World of Warcraft\\_retail_\\Interface\AddOns" -e "extracted_elvui"
echo "DONE"
call deactivate