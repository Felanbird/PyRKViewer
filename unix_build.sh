#!/bin/sh

pyinstaller -F --windowed --add-data ext/Iodine.dll:. main.py
