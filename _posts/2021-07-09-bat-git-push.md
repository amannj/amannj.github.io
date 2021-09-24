---
layout: post
title: "How To Use a Windows Bat File to Schedule, Git Add, Commit and Push to GitHub"
date: 2021-07-09
---

Let's say you want to use a Windows bat file to automatically run Git to add, commit and push to GitHub. 

For the sake of simplicity, we will assume that we want to automatise the Python script for which we created a Windows Scheduler task in [this](https://amannj.github.io/blog/2020/12/16/windows-scheduler) blog post. Even though the content of this particular Python script does not merit such a configuration, in a more realistic scenario, it could, say, contain a web scrapper which, you might want to run at regular intervals, and push the obtained data to GitHub automatically.

In this post we will assume that you have a fully functional set-up with Git installed on your computer, and you also have linked your local project to your GitHub account, e.g., by cloning it. Furthermore, we assume you have followed [this](https://amannj.github.io/blog/2020/12/16/windows-scheduler) blog post up until **Step 2**  and want the bat file you just created to automatically run Git to add, commit and push to Github. This can be done in a few lines of code as demonstrated below.

<br>

### Adding Git Commands to Your Bat File

For this purpose, we change the generic structure of the batch file to run our Python script in **Step 2** of the aforementioned blog post from this

```
"<Path to python.exe>" "<Path to my.py>"
```

to this:

```
"<Path to python.exe>" "<Path to my.py>"

git add .
git commit -m 'scheduled commit'
git push
```


Note, however, that the above will not work in some cases, for example, if there are no changes made to the repository. In such a case you can instead use

```
"<Path to python.exe>" "<Path to my.py>"

git add --all
git diff-index --quiet HEAD || git commit -m "scheduled commit"
git push
```

where
- `git add --all` will add all unstaged files of the entire working tree;
- the next line will then make a commit (`git commit -m "scheduled commit"`) only if Git observes a change, i.e. differences, vis-a-vis the HEAD version `git diff-index --quiet HEAD`: In case `git diff` has exit code zero, `git commit` will be executed.


A final word of caution: In case Git is not in your path, you will have to replace `git` with `"C:\Program Files\Git\bin\git.exe"` in the code chunks above.

<br>

### A more complete example

In the case of the Windows Scheduler task discussed in [this](https://amannj.github.io/blog/2020/12/16/windows-scheduler) blog post where Git is not in our path, we would end up with the chunk below, where we also added `timeout /t 5` to sleep in the batch file [anywhere between 4 and 5 seconds](https://stackoverflow.com/questions/1672338/how-to-sleep-for-five-seconds-in-a-batch-file-cmd/1672375#1672375) before commiting and pushing to GitHub:

```
"C:\Users\<Your Name>\AppData\Local\Programs\Python\Python38\python.exe" "C:\Users\<Your Name>\Desktop\my.py"

timeout /t 5

"C:\Program Files\Git\bin\git.exe" add --all
"C:\Program Files\Git\bin\git.exe" diff-index --quiet HEAD || git commit -m "scheduled commit"
"C:\Program Files\Git\bin\git.exe" push
```

<br>

### Next steps

Now that you have updated your bat file according to your needs, you can continue with **Step 2** from [this](https://amannj.github.io/blog/2020/12/16/windows-scheduler) blog post to use Windows Scheduler to time its automatic execution.


