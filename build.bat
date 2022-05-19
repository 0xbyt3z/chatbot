pyinstaller .\gui.py --clean -w -F --upx-dir=upx
copy data.pth dist
copy intents.json dist