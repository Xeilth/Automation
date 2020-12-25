@echo off
color 0a
title Web Search
cls
CD %~dp0
CD ..
CD "%cd%\WS"
python WS2.py

