#define MyAppName "Lipi Lekhika"
#define MyAppVersion "1.17"
#define MyAppPublisher "Lipi Lekhika"
#define MyAppURL "https://lipilekhika.pages.dev"
#define MyAppExeName "lekhika.exe"

[Setup]
AppId={{22557AB2-F097-42ED-AF75-C6DFD96F27C4}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={userpf}\{#MyAppName}
DisableDirPage=yes
DisableProgramGroupPage=yes
OutputBaseFilename=Setup
SetupIconFile=setup_icon.ico
Compression=lzma2/ultra
SolidCompression=yes
WizardStyle=modern
PrivilegesRequired=lowest

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "D:\Softwares\Z\bin\\pc\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\Softwares\Z\bin\\pc\resources\fonts\Nirmala.ttf"; DestDir: "{autofonts}"; FontInstall: "Nirmala UI"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\bin\\pc\resources\fonts\Vedic.ttf"; DestDir: "{autofonts}"; FontInstall: "Sanskrit Text"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\bin\\pc\resources\fonts\Modi.ttf"; DestDir: "{autofonts}"; FontInstall: "Noto Sans Modi"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\bin\\pc\resources\fonts\Siddham.ttf"; DestDir: "{autofonts}"; FontInstall: "Noto Sans Siddham"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\bin\\pc\resources\fonts\Granth.ttf"; DestDir: "{autofonts}"; FontInstall: "Noto Sans Grantha"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\bin\\pc\resources\fonts\Brahmi.ttf"; DestDir: "{autofonts}"; FontInstall: "Noto Sans Brahmi"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\bin\\pc\resources\fonts\Sharada.ttf"; DestDir: "{autofonts}"; FontInstall: "Satisar Sharada"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\bin\\pc\resources\fonts\Sharada1.ttf"; DestDir: "{autofonts}"; FontInstall: "Noto Sans Sharada"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\bin\\pc\resources\fonts\Tamil-Extended.ttf"; DestDir: "{autofonts}"; FontInstall: "Agastya Sans"; Flags: onlyifdoesntexist uninsneveruninstall

[Icons]
Name: "{userdesktop}\Lipi Lekhika"; Filename: "{app}\lekhika.exe"; Comment: "Type Indian Languages with Full Speed and Accuracy"
Name: "{userprograms}\Lipi Lekhika\Additional Information"; Filename: "{app}\resources\Additional Information.pdf"
Name: "{userprograms}\Lipi Lekhika"; Filename: "{app}\lekhika.exe"; HotKey: "shift+f2"; Comment: "Type Indian Languages with Full Speed and Accuracy"

[Setup]
LicenseFile="D:\Softwares\Z\bin\\pc\resources\LICENCE.txt"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent