# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['eddy.py'],
             pathex=['C:\\Projects\\Eddy-Source-master'],
             binaries=[],
             datas=[('C:\\Projects\\Eddy-Source-master\\static\\style.css', '.\static'),
                    ('C:\\Projects\\Eddy-Source-master\\static\\MCNP_template.html', '.\static'),
                    ('C:\\Projects\\Eddy-Source-master\\static\\SCALE_template.html', '.\static'),
                    ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Eddy_beta_0.2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Eddy')