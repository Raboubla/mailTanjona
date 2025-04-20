import PyInstaller.__main__

PyInstaller.__main__.run([
    '--name=Crypto-Invest-Expert',
    '--onefile',
    '--windowed',
    '--add-data=template1.txt;.',
    '--add-data=template2.txt;.',
    '--add-data=template3.txt;.',
    '--add-data=template4.txt;.',
    'app.py'
]) 