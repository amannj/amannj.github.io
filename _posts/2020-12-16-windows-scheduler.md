---
layout: post
title: "How To Schedule Python Scripts to Automate Tasks using Windows Scheduler on Windows 10"
date: 2020-12-16
---

In this tutorial I will go over the steps necessary to schedule a Python script using *Windows Scheduler*. This can be particularly useful if you want to re-run a particular programme at a prescribed time, for example for a web scraper.

For the purpose of this tutorial I will further assume that you have Python set up and running on your machine. For everything else, please follow the step-by-step guide below:

<br>

### Step 1: Create your Python script.

This should be self-explanatory. Let's assume we want to run the following script called `my.py` which does nothing but print today's date:

```
####################
# Content of my.py #
####################

import datetime

# Get date and time
todaysDate = datetime.datetime.today();
# Change display format (optional)
todaysDate = todaysDate.strftime("%Y-%m-%d %H:%M:%S")
# Print
print(todaysDate)
```

Now save your script! In my case, I'll simply save the Python script on my Desktop. 

```
C:\Users\<Your Name>\Desktop
```

where `<Your Name>` should be replaced with your Windows username.

<br>

### Step 2: Create Batch File to Run the Python Script

First, open *Notepad* and generate the following generic structure:

```
"<Path to python.exe>" "<Path to my.py>"
pause
```

In our example, the batch file will read as follows:

```
"C:\Users\<Your Name>\AppData\Local\Programs\Python\Python38\python.exe" "C:\Users\<Your Name>\Desktop\my.py"
pause
```

> **Note:** In case you want your batch file to run Git to automatically add, commit and push to GitHub, you will need a couple of extra lines of code which I discuss in [this](https://amannj.github.io/blog/2020/07/09/bat-git-push) blog post.

Next, save file with the 'bat' file extension; we'll call our file `run_mypy.bat` for now.

Finally, go ahead and check if the batch file triggers your Python script correctly. For this you simply have to double-click `run_mypy.bat`. If everything has worked out correctly, a command prompt should open now containing the following pieces of information (including the date and daytime which in this case is 2020-12-16 12:12:12):

```
C:\Users\<Your Name>\Desktop>"C:\Users\<Your Name>\AppData\Local\Programs\Python\Python38\python.exe" "C:\Users\<Your Name>\Desktop\my.py"
2020-12-16 12:12:12

C:\Users\<Your Name>\Desktop>pause
Press any key to continue . . .
```
<br>

### Step 3: Schedule Python Script using *Windows Scheduler*

- Open `Control Panel` and search for `Administrative Tools`.

- Select `Task Scheduler`. There, select option `Create Basic Task...` in the right panel.

- Give your Task a name (in this case we'll name the task *'Run mypy'*), and now define how often and when you want the task to be triggered. This step is rather self-explanatory.

- Once you have configured the trigger for your job to your satisfaction, click next and define the *Action* which you want the scheduled task to perform. In our case we want to `Start a program`.

- Click `Next` and then on `Browse`. Then navigate to where your batch file sits. In our case `C:\Users\<Your Name>\Desktop\run_mypy.bat`. 

- **IMPORTANT**: If you are planning on saving/appending data that you obtain from running the Python script, make sure make sure you also provide the location of your application folder in  `Start in (optional)`. This allows the Scheduler to access all of the relevant elements (files, folders etc.) of your project. In our case, this would be `C:\Users\<Your Name>\Desktop\`.

- Click `Next` again and the final screen will provide a summary of the new task you have just created. You can always navigate back and change its configuration. Once you're happy with your result click `Finish` and you're done!

- To check if the task you created works, access the `Task Scheduler Library` (left panel in *Task Scheduler*), select the task from the list of created tasks (middle panel), right-click and then click on `Run`. A terminal window should open returning the same result as when double-clicking `run_mypy.bat`.

  
This last step completes this tutorial. In case you want to learn more about *Windows Task Scheduler*, check out the [online documentation](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page).