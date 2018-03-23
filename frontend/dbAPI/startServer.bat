%echo off%

%PATHOFSCRIPT% = C:\Users\Daveberth\Documents\Uni\KI\Projekt\KI4SG\frontend>

cd %PATHOFSCRIPT%
wait(10)
node server.js
set /p=Hit ENTER to stop Node Server