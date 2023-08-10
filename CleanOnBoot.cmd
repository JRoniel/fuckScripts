# FUNCIONALIDADE:
# LIMPA MEMORIA TEMPORARIA E ENCERRA TAREFAS DESNCESSARIAS

@echo off
color a
del /q /f /s %windir%\Temp
%windir%\system32\rundll32.exe advapi32.dll,ProcessIdleTasks
timeout 7
