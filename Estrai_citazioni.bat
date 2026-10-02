@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
title Estrattore di citazioni

rem --- Trova Python ---
set "PY=python"
where python >nul 2>nul || set "PY=py"
%PY% --version >nul 2>nul
if errorlevel 1 (
  echo Python non e' installato.
  echo Scaricalo da https://www.python.org/downloads/ e spunta "Add Python to PATH".
  pause
  exit /b
)

rem --- Installa pypdf la prima volta ---
%PY% -c "import pypdf" >nul 2>nul || %PY% -m pip install --quiet pypdf

rem --- Fonti: file trascinati sull'icona, oppure chiede un link/percorso ---
set "FONTI=%*"
if "%FONTI%"=="" (
  echo Trascina uno o piu' file su questa icona, oppure incolla qui un link.
  set /p "FONTI=Link o percorso della fonte: "
)
if "%FONTI%"=="" exit /b

echo.
set "TEMA="
set /p "TEMA=Parole chiave della storia (es. Groenlandia Trump acuerdo): "

for /f %%i in ('%PY% -c "import datetime;print(datetime.datetime.now().strftime('%%Y%%m%%d_%%H%%M'))"') do set "ORA=%%i"
if not exist "risultati" mkdir "risultati"
set "OUT=risultati\citazioni_%ORA%.md"
set "CSV=risultati\citazioni_%ORA%.csv"

echo.
%PY% citazioni.py %FONTI% -t "%TEMA%" -o "%OUT%" --csv "%CSV%"
if errorlevel 1 (
  echo.
  echo Qualcosa e' andato storto: leggi il messaggio qui sopra.
  pause
  exit /b
)

start "" notepad "%OUT%"
echo.
echo Fatto. Risultati salvati nella cartella "risultati".
echo (il file .csv si apre con Excel)
pause
