@echo off
color 0a
title Interpreter
cls
CD /d %~dp0
CD ..
CD "%cd%\WB"
python interpreter.py

