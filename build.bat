pyinstaller .\gui.py -w -F --upx-dir=upx
copy data.pth dist
copy intents.json dist