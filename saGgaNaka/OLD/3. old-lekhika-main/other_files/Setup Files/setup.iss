#define MyAppName "Lipi Lekhika"
#define MyAppVersion "1.0"
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
OutputBaseFilename=Lipi Lekhika Setup
SetupIconFile=D:\Softwares\Z\LipiLekhika\other_files\Setup Files\setup_icon.ico
Compression=lzma2/ultra64
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "D:\Softwares\Z\lekhika-bin\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "D:\Softwares\Z\lekhika-bin\assets\fonts\nirmala.ttf"; DestDir: "{fonts}"; FontInstall: "Nirmala UI"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\assets\fonts\ved.ttf"; DestDir: "{fonts}"; FontInstall: "Sanskrit Text"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\assets\fonts\modi.ttf"; DestDir: "{fonts}"; FontInstall: "Noto Sans Modi"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\assets\fonts\sharada.ttf"; DestDir: "{fonts}"; FontInstall: "Noto Sans Sharada"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\assets\fonts\brahmi.ttf"; DestDir: "{fonts}"; FontInstall: "Noto Sans Brahmi"; Flags: onlyifdoesntexist uninsneveruninstall
Source: "D:\Softwares\Z\lekhika-bin\assets\fonts\brahmi_supp.ttf"; DestDir: "{fonts}"; FontInstall: "Segoe UI Historic"; Flags: onlyifdoesntexist uninsneveruninstall

[Icons]
Name: "{autoprograms}\Lipi Lekhika\{#MyAppName}"; Filename: "{app}\lekhika.exe"; HotKey: "ctrl+f1"
Name: "{userdesktop}\{#MyAppName}"; Filename: "{app}\lekhika.exe"; Comment: "Type Indian Languages with Full Speed and Accuracy."
Name: "{autoprograms}\Lipi Lekhika\{#MyAppName} Normal"; Filename: "{app}\samanya.exe"
Name: "{autoprograms}\.{#MyAppName}"; Filename: "{app}\lekhika.exe"
Name: "{autoprograms}\Lipi Lekhika\User Mannual (English)"; Filename: "{app}\assets\User Mannual.pdf"
Name: "{autoprograms}\Lipi Lekhika\उपयोगकर्ता पुस्तिका (Hindi)"; Filename: "{app}\assets\उपयोगकर्ता पुस्तिका.pdf"
Name: "{autoprograms}\Lipi Lekhika\उपयोगकर्तृपुस्तिका (Sanskrit)"; Filename: "{app}\assets\उपयोगकर्तृपुस्तिका.pdf"

[Run]
Filename: "{app}\install.bat"; Flags: runhidden
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent