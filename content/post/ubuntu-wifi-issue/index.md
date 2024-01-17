---
title: How to fix 'No WiFi Adapter' issue in Ubuntu 20.04
subtitle: In case you are using a (now) outdated version of Ubuntu and run into some weird WiFi issue.
summary: In case you are using a (now) outdated version of Ubuntu and run into some weird WiFi issue.

image:
  caption: Photo by Gabriel Heinzer on Unsplash
  focal_point: Smart

# Date published
date: '2021-01-10T00:00:00Z'
  
# Date updated
lastmod: '2021-01-10T00:00:00Z'

# Link this post with a project
projects: []  

authors:
  - admin

tags:
  - Tutorial  
  - General
  - IT
  - Ubuntu
  - WiFi

categories:
  - Tutorial
---

In case you have, just like me, come across the issue that Ubuntu 20.04 greets you with a *'no wifi adapter'* error message after running some updates, this here did the trick for me: 

1. Connect your laptop to the internet (either ethernet, your phone etc.).
2. Run the following two commands in the terminal (hit `Ctrl` + `t`):


- `sudo apt-get purge bcmwl-kernel-source`

- `sudo apt-get install broadcom-sta-source broadcom-sta-dkms broadcom-sta-common`

Reboot and everything should be running smoothly again! 
