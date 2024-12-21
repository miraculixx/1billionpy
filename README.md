1billion loops with Python
==========================

This explores various options to optimize the Python implementation of the
[1billion loop problem](https://github.com/bddicken/languages).

Read more about [my findings on substack](https://scaledpython.substack.com/p/00ad0bd0-9b90-49b6-b067-c24d852d3f74?postPreview=paid&updated=2024-12-21T14%3A31%3A01.541Z&audience=everyone&free_preview=false&freemail=true)

Results in a nutshell
---------------------

<img src="./latency_comparison.gif">

How to run this
---------------

$ git clone https://github.com/miraculixx/1billionpy.git
$ cd 1billionpy
$ ./run

Note you need to install hyperfine, create a Python3.13
environment and install pypy before running. 