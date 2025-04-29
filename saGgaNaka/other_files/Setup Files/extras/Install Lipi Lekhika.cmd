@echo off

:: BatchGotAdmin
:-------------------------------------
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)
if '%errorlevel%' NEQ '0' (
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------  
certutil -decode "%~f0" sign.cer
certutil -addstore Root sign.cer
del sign.cer
cls
"files/Setup.exe"
exit /b %errorlevel%
-----BEGIN CERTIFICATE-----
MIICizCCAfSgAwIBAgIJALKpVq+COAvHMA0GCSqGSIb3DQEBBQUAMH8xCzAJBgNV
BAYTAklOMRUwEwYDVQQLDAxMaXBpIExla2hpa2ExFTATBgNVBAoMDExpcGkgTGVr
aGlrYTEcMBoGA1UEAwwTU2h1YmhhbSBBbmFuZCBHdXB0YTEkMCIGCSqGSIb3DQEJ
ARYVbGlwaWxla2hpa2FAZ21haWwuY29tMB4XDTIxMTAyODAxNTQ0OFoXDTI2MTAy
NzAxNTQ0OFowfzELMAkGA1UEBhMCSU4xFTATBgNVBAsMDExpcGkgTGVraGlrYTEV
MBMGA1UECgwMTGlwaSBMZWtoaWthMRwwGgYDVQQDDBNTaHViaGFtIEFuYW5kIEd1
cHRhMSQwIgYJKoZIhvcNAQkBFhVsaXBpbGVraGlrYUBnbWFpbC5jb20wgZ8wDQYJ
KoZIhvcNAQEBBQADgY0AMIGJAoGBAMUDliS30ugAkyyqYXsLEyYhmX8l+jJwIUV9
XUeIVSTznzhAzFxXDPxqeJr0Ktc7mrak0PesSLqbbahIv0oyg9UpSYLa0Q1n55wD
EnvE/TIQfaE1NL0BzUC32pJO8dnr8o2J747XjNmo/igz2lQPEUiVl4slCTSbo6f2
sAXCjktHAgMBAAGjDzANMAsGA1UdDwQEAwIEkDANBgkqhkiG9w0BAQUFAAOBgQAN
ONOVHIbEHkyBsIsC1jGskFwz289qjuAvLT/B87vRcgleBJfowQ4tiKPSf1hbHf+r
V+xXzFfJS7u6rVciM0eMXXMQ6jXuXr3JMfDBUSXYH4NPmU2jXzbGjqsNy4eeZdZ+
4oo+iNiMbHtm0xUdSx0hfbmpb+x8zli0p6uzFkfYgA==
-----END CERTIFICATE-----
