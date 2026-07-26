# Screenshot-Sorter
A .pyw file that runs in the background and automatically sorts screenshots. (Windows-Only)
You know that annoying feeling everytime you take a screenshot, it goes to the screenshots folder, and when you want it, it takes at least a minute to find it?
Well this one file fixes that problem entirely.
Running in the background silently, this one .pyw file automatically sorts your screenshots by year and month, and then renames them to the day. 
Your old unorganized screenshot folder will now have a date system, where there are folders of each year, and then folders of each month in them. 
All screenshots are also renamed to the day you took them, for example, a screenshot took on July 26th, 2026 would be named: July26_SS1, and then the second screenshot of that day would be July26_SS2, etc.
That screenshot would be in the July folder of the 2026 folder. 


Quick note:
Edit the downloaded file with your screenshots folder location if needed.

Steps to install:

Completely in Background AUTOMATIC:
1. Download File
2. Open Command Prompt through search bar, or press Win+R and type cmd
3. Run this command: python -m pip install watchdog, and this one: pip install watchdog
4. Press Win+R on keyboard and type: shell:startup
5. Drag the .pyw File into the shell:startup folder

Completely in Background MANUALLY:
1. Download File
2. Open Command Prompt through search bar, or press Win+R and type cmd
3. Run this command: python -m pip install watchdog, and this one: pip install watchdog
4. Press Win+R on keyboard
5. Type in: pythonw C:\Users\you\yourfolder\sort_screenshots.pyw and hit enter


CMD VISIBLE:
1. Download File
2. Open Command Prompt through search bar, or press Win+R and type cmd
3. Run this command: python -m pip install watchdog, and this one: pip install watchdog
4. Copy the path of the downloaded .pyw file, type: python C:\Users\you\yourfolder\sort_screenshots.pyw, and hit enter
5. Now this will keep it running, but the cmd file will have to be open :/
