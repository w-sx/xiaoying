@echo off
create-version-file version_file.yaml --outfile version_file.txt
pyinstaller -w -D -n xiaoying --version-file version_file.txt src/main.py
pause