picture-automatization script
automatically transfers files with extensions .png .jpg .jpeg .gif .webp .svg from selected folder to the destination folder

in pict-automatization.py:
old_folder = '*for example - path to download folder*'
new_folder = '*path to destination folder*'

run:
1. install python 3.6+
2. pip install watchdog
3. pip install pyinstaller
4. pyinstaller -F -w pict-automatization.py
5. in foder dist run executable file