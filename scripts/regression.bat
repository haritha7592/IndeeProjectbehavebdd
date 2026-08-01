@echo off

behave --tags=@regression

allure serve reports\allure-results

pause