
===================================
Spider - An Uber-Simple Web Crawler
===================================

Overview
========

Spider is an uber-simple web crawling and web scraping tool, used to crawl
websites and extract structured data from their pages.

Requirements
============

* Python 2.7 and above. May work with Python 3.4 and above (not tested).

    Most operating systems other than Windows already have Python installed by
    default. To check that Python is installed, open a command line (typically
    by running the "Terminal" program), and try the following:

    .. code-block:: bash

     $ python
     Python 2.7.12 (default, Nov 19 2016, 06:48:10)
     [GCC 5.4.0 20160609] on linux2
     Type "help", "copyright", "credits" or "license" for more information.
     >>> 1 + 1
     2
     >>> you can type expressions here .. use ctrl-d to exit

    If python is not installed, see the
    `python.org downloads <https://www.python.org/downloads/>`_ page.

* Should work on Linux, Windows, Mac OSX, BSD

Pre-Flight Check
^^^^^^^^^^^^^^^^

These instructions are intended specifically for installing ``pip``, a tool
for installing and managing Python packages. Before you start playing around
with **Spider** tool, make sure you have ``pip`` installed on your system.
``pip`` will help you install the packages **Spider** depends on. 

Installing ``pip``
------------------

``pip`` is already installed if you're using Python 2 >=2.7.9 or
Python 3 >=3.4 binaries downloaded from
`python.org <https://www.python.org/>`_, but you'll need to upgrade ``pip``.
On Ubuntu Precise (12.04) and later, ``pip`` is included in the distribution,
so to install it (if required) and to upgrade it as any other package::

    $ sudo apt-get install python-pip python-dev build-essential
    $ sudo pip install --upgrade pip

For other OS flavours please follow the steps in
`Installing pip <https://pip.pypa.io/en/stable/installing/>`_.

Quick Run
=========

Clone this repository in the usual way, for example::

    $ git clone https://github.com/debayanray/simple-web-crawler.git
    $ cd simple-web-crawler

Install the dependencies::

    ~/simple-web-crawler$ sudo pip install -r requirements.txt

Run the sample test of ***Spider*** on "http://wiprodigital.com"::

    ~/simple-web-crawler$ python test_spider.py

A sample output of this is stored in ``sample_out.txt`` file.
Please have a look `here <https://github.com/debayanray/simple-web-crawler/blob/master/sample_output.txt>`_

Usage
=====

In brief, for using this tool, use *Spider* object as::

    >>> import spider
    >>> from spider import parsers
    >>> web_spider = spider.Spider("http://wiprodigital.com")
    >>> web_spider.add_parser(parsers.EmailParser())
    >>> web_spider.add_parser(parsers.ImageParser())
    >>> web_spider.weave(max_depth=2)
    >>> web_spider.display_weave_result(indent=4)

Thank you for your support. Cheers!
