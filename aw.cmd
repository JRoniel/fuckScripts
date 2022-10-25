# FUNCIONALIDADE:
# LIMPA MEMORIA TEMPORARIA E ENCERRA TAREFAS DESNCESSARIAS
# OTIMO PARA SER EXECUTADO LOGO APÓS A INICIALIZAÇÃO DO COMPUTADOR.

@echo off
color a
title AW - Delivery 0.3v
del /q /f /s %windir%\Temp
%windir%\system32\rundll32.exe advapi32.dll,ProcessIdleTasks
start /min https://web.whatsapp.com/
timeout 7
