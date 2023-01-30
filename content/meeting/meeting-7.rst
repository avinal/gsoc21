*********************
Coding Week 5 Meeting
*********************

:date: 2021-07-09 22:22
:tags: gsoc, FOSSology
:category: report
:summary: This week was dedicated to perfecting CMake Installation Configuration. The installation was tested and bugs were discussed. 
:slug: meeting-7
:status: published

.. raw:: html
  
  <div class="alert alert-info" role="alert">This week was dedicated to perfecting CMake Installation Configuration. The installation was tested and bugs were discussed. </div>

Attendees
---------

- `Gaurav Mishra <https://github.com/GMishx>`_
- `Avinal Kumar <https://github.com/avinal>`_


Week 5 Progress
---------------

.. raw:: html

    <div class="alert alert-success" role="alert">
    <ul><li>CMake Installation Configuration is almost complete.</li>
    <li>FOSSology can be installed completely via CMake</li>
    <li>Post install script generation also added</li>
    <li>To test the current progress, follow the instructions <a href="https://github.com/avinal/FOSSology/wiki#test-the-new-system-only-gcc-with-make-and-ninja-tested-for-now">here</a></li>
    </ul>
    </div>

Discussions
-----------

* There are permission problems while running bash script of :code:`nomos`, :code:`monk` and :code:`genvendor`.

  - One possible fix can be to add :code:`bash` before each bash scripts. 
  - The other fix is to modify shebang line in each script from :code:`#!/bin/sh` to :code:`#!/bin/bash`.

* In copyright agent same files are being compiled thrice, this is slowing down the build.

  - I am working on it. The problem is occurring because of three different executables. 
  - I will try to combine the common objects together.

* There are some redundant files in the installation. And VERSION file is missing in :code:`/usr/local/share/fossology`. 

Conclusion and Further Plans
----------------------------

- Fix copyright build.
- Remove redundant files and folders.
- Fix permission issues.
- 
