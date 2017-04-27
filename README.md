# GradDesign
My Graduation Project

This is codes for my Graduate Project

flash.py and html.py is used for obtaining the CPU percentage.

# Dependencies
Python library: psutil


# Arguments

### For GPU acceleration `disabled` cases:
flash.py \<pid_MainPage> \<pid_FlashPlayer> \<timelength>

html.py \<pid_page> \<timelength>

### For GPU acceleration `enabled` cases:
flash3.py \<pid_MainPage> \<pid_FlashPlayer> \<pid_GPUprocess> \<timelength>

html3.py \<pid_page> \<pid_GPUprocess> \<timelength>

Where pid-concerned arguments can be found in Chrome or Chromium-based Browsers at \"More Tools - Task Management\"


# Bug Fixes
- 170424 I found that flash.py and html.py doesn`t work well, because a used Anaconda Python Realease and it brings psutil 5.0.1. Then I reinstalled psutil latest version 5.2.2 and it works.
