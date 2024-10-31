# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\balcaobib\\Documents\\UNITECNO\\MASPIA7UP\\UPNAL\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['C:\\Users\\balcaobib\\Documents\\UNITECNO\\MASPIA7UP\\UPNAL\\calculator.py', 'C:\\Users\\balcaobib\\Documents\\UNITECNO\\MASPIA7UP\\UPNAL\\maspia.py', 'C:\\Users\\balcaobib\\Documents\\UNITECNO\\MASPIA7UP\\UPNAL\\converter.py', 'utils'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
