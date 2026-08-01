@echo off

behave --tags=@smoke

allure serve reports\allure-results

pause
