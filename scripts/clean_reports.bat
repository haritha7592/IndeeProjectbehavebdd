@echo off

REM =====================================================
REM Option 1: Delete the complete folders
REM =====================================================

REM if exist  reports\allure-results rmdir /s /q reports\allure-results
REM if exist reports\junit rmdir /s /q reports\junit
REM if exist reports\screenshots rmdir /s /q reports\screenshots
REM if exist  allure-results rmdir /s /q allure-results
REM if exist  screenshots rmdir /s /q screenshots

REM =====================================================
REM Option 2: Delete only the files inside the folders
REM (Folders will remain)
REM =====================================================

REM del /Q reports\allure-results\*.* 2>nul
REM del /Q reports\junit\*.* 2>nul
REM del /Q reports\screenshots\*.* 2>nul
REM del /Q reports\*.* 2>nul

echo Old reports cleaned.

pause
