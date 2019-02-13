@echo off
for /f "tokens=1,2,3 delims==" %%a in (config.ini) do (
if %%a==pgnfile set pgnfile=%%b
if %%a==ordopath set ordopath=%%b
if %%a==debugfile set debugfile=%%b
)



start powershell -noexit -command "Get-Content %pgnfile% -Wait"
start powershell -noexit -command "Get-Content %debugfile% -Wait"

:repeat
echo -----------------------------------------------------------------------------------------------------
%ordopath% -q -W -D -G -J -o %pgnfile%_ordo_summary.txt -a 0 -s 1000 -U "0,1,2,3,5,4,7,9,8,10" -p  %pgnfile%
type %pgnfile%_ordo_summary.txt
echo -----------------------------------------------------------------------------------------------------
echo %date% %time%
timeout /t 10 /nobreak

goto repeat
exit
