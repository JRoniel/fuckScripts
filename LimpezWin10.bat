@echo off
title Limpeza segura do Windows
color 0A

echo =====================================
echo LIMPEZA DE ARQUIVOS TEMPORARIOS
echo =====================================
echo.

echo Limpando TEMP do usuario...
del /s /f /q "%temp%\*" >nul 2>&1
for /d %%x in ("%temp%\*") do rd /s /q "%%x" >nul 2>&1

echo Limpando TEMP do sistema...
del /s /f /q "C:\Windows\Temp\*" >nul 2>&1
for /d %%x in ("C:\Windows\Temp\*") do rd /s /q "%%x" >nul 2>&1

echo Limpando cache do Windows Update...
net stop wuauserv >nul 2>&1
net stop bits >nul 2>&1
del /s /f /q "C:\Windows\SoftwareDistribution\Download\*" >nul 2>&1
net start wuauserv >nul 2>&1
net start bits >nul 2>&1

echo Limpando cache DNS...
ipconfig /flushdns >nul

echo Limpando logs do sistema...
del /s /f /q "C:\Windows\Logs\CBS\*" >nul 2>&1

echo Limpando arquivos de erro...
del /s /f /q "C:\ProgramData\Microsoft\Windows\WER\ReportQueue\*" >nul 2>&1

echo Limpando cache da Microsoft Store...
wsreset.exe

echo Limpando cache do navegador Edge...
del /s /f /q "%localappdata%\Microsoft\Edge\User Data\Default\Cache\*" >nul 2>&1

echo Limpando cache do Chrome...
del /s /f /q "%localappdata%\Google\Chrome\User Data\Default\Cache\*" >nul 2>&1

echo.
echo =====================================
echo LIMPEZA FINALIZADA
echo =====================================
echo.

pause