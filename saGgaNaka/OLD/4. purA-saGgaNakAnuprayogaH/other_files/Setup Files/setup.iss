#define MyAppName "Lipi Lekhika"
#define MyAppVersion "1.4"
#define MyAppPublisher "शुभमानन्दगुप्तेन स्वयं चालितः"
#define MyAppURL "https://www.lipilekhika.com"
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
DefaultDirName={autopf}\{#MyAppName}
DisableDirPage=yes
DisableProgramGroupPage=yes
OutputBaseFilename=Setup
SetupIconFile=setup_icon.ico
Compression=lzma2/ultra
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "D:\Softwares\Z\lekhika-bin\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\Softwares\Z\lekhika-bin\resources\fonts\nirmala.ttf"; DestDir: "{fonts}"; FontInstall: "Nirmala UI"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\resources\fonts\ved.ttf"; DestDir: "{fonts}"; FontInstall: "Sanskrit Text"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\resources\fonts\modi.ttf"; DestDir: "{fonts}"; FontInstall: "Noto Sans Modi"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\resources\fonts\sharada.ttf"; DestDir: "{fonts}"; FontInstall: "Noto Sans Sharada"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\resources\fonts\brahmi.ttf"; DestDir: "{fonts}"; FontInstall: "Noto Sans Brahmi"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\resources\fonts\siddham.ttf"; DestDir: "{fonts}"; FontInstall: "Noto Sans Siddham"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\resources\fonts\granth.ttf"; DestDir: "{fonts}"; FontInstall: "Noto Sans Granth"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\resources\fonts\tamil_extend.ttf"; DestDir: "{fonts}"; FontInstall: "Agastya Sans"; Flags: onlyifdoesntexist uninsneveruninstall

[Icons]
Name: "{autoprograms}\Lipi Lekhika"; Filename: "{app}\lekhika.exe"; HotKey: "shift+f2"
Name: "{userdesktop}\Lipi Lekhika"; Filename: "{app}\lekhika.exe"; Comment: "Type Indian Languages with Full Speed and Accuracy."
Name: "{autoprograms}\Lipi Lekhika\Lipi Lekhika Normal (Lipi Parivartak)"; Filename: "{app}\samanya.exe"
Name: "{autoprograms}\Lipi Lekhika\Note on Additional Scripts"; Filename: "{app}\resources\Note on Additional Scripts.txt"
[Setup]
LicenseFile="D:\Softwares\Z\lekhika-bin\LICENCE"
[Run]
Filename: "{app}\install.cmd"; Flags: runhidden
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent