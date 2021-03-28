# What is Spamazon?
An Amazon web scraping, and graphing utility made over the course of 48 hours in python by a team of talented coders consisting of:
- Paul O'Bar 
- Michael Stepp
- Aaron Brown
- Dylan Manuel

A video walkthrough of our project is coming soon!

# Features

**Savable graphs**

Save your graph with the power of mathplotlib integration

**Copy and Past URL lookup**

Graphing reviews is as simple as copying and pasting the URL into Spamazon!

**Interesting Loading screen?**

Enjoy reading the titles of reviews as they come pouring in!

# Installation

**Requirements**

To install Spamazon you'll first need to install [**python3**](https://www.python.org/downloads/) 3.8.5 or above. Next, you'll need [**BeautifulSoup4**](https://pypi.org/project/beautifulsoup4/) along with [**Mathplotlib**](https://matplotlib.org/stable/users/installing.html), both can be installed easily using pip. Finally and most importantly you'll need to install [**splash and docker**](https://splash.readthedocs.io/en/stable/) we recommend viewing their installation notes as they lead you through installation and launching of splash.

**Running**

To run Spamazon simply make sure you have your splash server open on its default port (8050) and type in "python3 Spamazon.py" without the parentheses. You'll be prompted to paste in you Amazon URL, the program is designed to accept the landing page URL for nearly all product hosted on Amazon. Next, you'll be prompted to enter the number of reviews you wish to be collected for plotting, a **large number of reviews will correlate to a longer loading time**. Finally press y to start the program in full, with every page of reviews collected you'll be shown a glimpse of their content.



