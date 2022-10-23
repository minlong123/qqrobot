@echo off
title Mirai Console
java -cp "./libs/*" net.mamoe.mirai.console.terminal.MiraiConsoleTerminalLoader %*
pause