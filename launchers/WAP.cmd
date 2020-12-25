@echo off
color 0a
title Web Access Point
cls
cd %~dp0
CD ..
CD "%cd%\WAP"
python WAP.py

