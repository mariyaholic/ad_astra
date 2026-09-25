@echo off
rem Run the experimental multi-archive pipeline from the repository root.
rem Usage:  experimental\run.cmd archives
rem         experimental\run.cmd run experimental\campaigns\<id>.yaml
rem Sandbox root: %CYGNUS_MULTI_ROOT% if set, else experimental\.
setlocal
set "HERE=%~dp0"
cd /d "%HERE%.."
set "PYTHONPATH=%CD%\src;%CD%\experimental;%PYTHONPATH%"
python -m experimental.cygnus_multi %*
endlocal