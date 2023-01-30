*********************
Coding Week 1 Meeting
*********************

:date: 2021-06-11 23:30
:tags: gsoc, FOSSology
:category: report
:summary: In this third meeting, I demoed the working build system, currently building executables and libraries, a lot of queries were resolved about writing version files and attaching commits and hashes to the build. 
:slug: meeting-2
:status: published

.. raw:: html
  
  <div class="alert alert-info" role="alert">In this third meeting, I demoed the working build system, currently building executables and libraries, a lot of queries were resolved about writing version files and attaching commits and hashes to the build. </div>

Attendees
---------

- `Michael C. Jaeger <https://github.com/mcjaeger>`_
- `Shaheem Azmal M MD <https://github.com/shaheemazmalmmd>`_
- `Gaurav Mishra <https://github.com/GMishx>`_
- `Anupam Ghosh <https://github.com/ag4ums>`_
- `Ayush Bhardwaj <https://github.com/hastagAB>`_
- `Avinal Kumar <https://github.com/avinal>`_


Week 1 Progress
---------------

.. raw:: html

    <div class="alert alert-success" role="alert">
    <p>This week was mainly focused on analyzing the previous build system and framing a skeleton for the new build system.
    <ul><li>Created the build configuration <a href="https://github.com/avinal/FOSSology/wiki/agents-spec#agents-configuration-list">analysis table</a>.</li>
    <li>Completed the basic skeleton.</li>
    <li>Completed the CMake configuration for libraries</li>
    <li>To test the current progress, follow the instructions <a href="https://github.com/avinal/FOSSology/wiki#test-the-new-system-only-gcc-with-make-and-ninja-tested-for-now">here</a></li>
    <li>Test on <a href="https://gitpod.io/#https://github.com/avinal/FOSSology/tree/avinal/feat/cmake-buildsystem">GitPod</a> right inside your browser. </li></ul></p>
    </div>
    <div class="embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item" src="/images/first-build-gitpod.webm" allowfullscreen></iframe>
    </div>
    <br>

Discussions
-----------

* **What are the flags needed for C and C++?**
  
  - The :code:`-g` flag enables debug.
  - The :code:`-O2` flag is used for optimizing.
  - In FOSSology these two flags are used together by default for all build purposes because it is desired to have an optimized binary but some level of debugging information is also desired.

* **The Makefiles have some compile-time preprocessor macro definitions that need to be passed to each build.** The Makefiles have all the path values passed as :code:`'"..value.."'` format *(double quote inside single quotes)*, however the commands produced by CMake have :code:`\"..value..\"` format *(escaped double quotes)*. Are they the same or it needs to be changed?
  
  - Currently, there is nothing to determine if they work the same or not, but if the compiler would not have accepted them then, it would have thrown an error. As long it is working these should be fine, but will need to be checked in the final build.

* **Are all libraries in FOSSology static?**
  
  - No, by default no library is static. The format :code:`lib<library-name>.a` is confusing but no need to worry about it for now, if this is working fine then no problem.
  - In general, this format denotes a static library.

* **How to add the version and commit information to the builds?**

  - I have gone through `this thread <https://cmake.org/pipermail/cmake/2018-October/068383.html>`_ on CMake's official mailing list. And they have suggested a lot of options, but unable to decide which option to use. Gaurav said he will see into this thread and for now, I should try writing a shell script and test if that works. 
  - Same can be tested for the version too.

* **What is** :code:`_squareVisitor.h.pre` **used for?**
  
  - They are used to generate source code at build time.

* **Is there any inheritance structure in the build system?** *(Michael)*

  - For now, I am writing separate modules for the default operations needed in most configurations. The final structure will be decided in the final build.

* **Where are all the binaries produced?** *(Gaurav)*

  - They are located in the build folder with the same directory structure as the original project.
  - While installing the same will be used and none of the source folders are ever disturbed.

* **Are all flags taken from the Makefiles itself?** *(Anupam)*

  - Yes and No, there are some flags that CMake uses by default, they can be altered by changing the value for :code:`CMAKE_C_FLAGS` and :code:`CMAKE_CXX_FLAGS`. One can also append their flags. Since not all compilation requires all the flags, I have taken the default one into cache variables, and others are appended while configuring for a particular project. 


Conclusion and Further Plans
----------------------------

* Try the :code:`monkbulk` in monk and :code:`makefile.sa` in nomos. 
* Try adding the version and commit hash info.
* Implement writing version files for each build.
* Add proper comments in the :code:`CMakeLists.txt` files.

