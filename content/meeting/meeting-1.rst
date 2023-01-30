***************************
Community Bonding Meeting 1
***************************

:date: 2021-06-04 22:30
:tags: gsoc, fossology, 
:category: meet
:summary: In this second meeting points over default Makefiles were discussed. Ninja can be used as an alternative for Makefiles.
:slug: meeting-1
:status: published

.. raw:: html
  
  <div class="alert alert-info" role="alert">In this second meeting points over default Makefiles were discussed. Ninja can be used as an alternative for Makefiles.</div>

Attendees
---------
- `Gaurav Mishra <https://github.com/GMishx>`_
- `Anupam Ghosh <https://github.com/ag4ums>`_
- `Avinal Kumar <https://github.com/avinal>`_


Discussions
-----------

* **What is the use of** :code:`Makefile.deps` **and** :code:`Makefile.process` **files?**
  
  - :code:`Makefile.deps` consists of many used and unused snippets. These snippets help setup the build and test environment for fossology. Since there are many directories that are hardcoded, special care is required while replacing this file.
  - :code:`Makefile.process` generates a master variable from list of variables. It assists the script in :code:`Makefile.conf` file. These files together generate a list of variables that can be used throughout the build process. 


* The build can be made faster using **Ninja** instead of **Make**.
* Ninja supports parallel builds by default.
* Print the flags used once the CMake configuration is working. That will help us debug the process.

Conclusion and Further Plans
----------------------------

* Write a *CMakeLists.txt* for **lib**.
* Push the working branch and update the link either on wiki or blog.

