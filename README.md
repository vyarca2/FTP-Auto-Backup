# FTP-Auto-Backup

This repository contain the Python programs and scripts needed to automatically backup device folders to an FTP Server. This works on both Windows and Linux distros. The scheduler.sh file is meant to be run in a crontab job in Linux, while the folderupload.py file is scheduled using the Windows Task Scheduler. The details.py provides a simple Tkinter GUI to set the username, password, server IP and directory paths for the folderupload.py program. 
