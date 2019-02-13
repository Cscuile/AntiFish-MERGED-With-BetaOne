## Overview

cute-cli-monitor is a basic way of monitoring output from the cutechess-cli. The solution is currently running on Windows 10 (may work on Windows 7, but has not been tested) and will be ported to linux shortly.

The solution opens three terminal windows.
  * PGN Monitoring - A window that will display the latest (complete) game along with results.
  * Debug Monitoring - A window that will continuously output debug information for the engines
  * Tournament Monitoring - A window that uses Ordo to provide latest statistics on gameplay (*note that Ordo limitations apply here, perfect winners/losers will not be present in the output*)

## Files

The solution the following files:

  **Windows 10**
  * config.ini, the config file specifyling the absolute path location for your cutechess-cli debug and pgn output, as well as the absolute path to your Ordo binary.

  * cute-cli-monitor, a Windows batch file that controls the process and creates all the windows

## Output

The solution needs to be manually terminated (just close all the windows). The following files will be left behing
  * An Ordo summary of the tournament will be in the same directory as your PGN file, using the same name as your PNG file, with the suffix _ordo_summary.txt. If your PGN file was D:\test\output.pgn you would find this summary file located at D:\test\output.pgn_ordo_summary.txt
