picture-automatization script
automatically transfers .png .jpg .jpeg .gif .webp .svg files from selected folder to the destination folder

in pict-automatization.py:
```
old_folder = os.path.join('*for example - path to download folder*')
new_folder = os.path.join('*path to destination folder*')
```
run:
1. install python 3.6+
2. install watchdog
```
pip install watchdog
```
3. install pyinstaller
```
pip install pyinstaller
```
4. select folders in .py file
5. build in executable file
```
pyinstaller -F -w pict-automatization.py
```
6. in foder dist run executable file
