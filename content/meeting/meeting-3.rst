*********************
Coding Week 2 Meeting
*********************

:date: 2021-06-18 23:30
:tags: gsoc, FOSSology
:category: report
:summary: In this fourth meeting, a lot of questions were discussed related to the existing build system and what things we have to drop or modify. 
:slug: meeting-3
:status: published

.. raw:: html
  
  <div class="alert alert-info" role="alert">In this fourth meeting, a lot of questions were discussed related to the existing build system and what things we have to drop or modify. </div>

Attendees
---------

- `Michael C. Jaeger <https://github.com/mcjaeger>`_
- `Shaheem Azmal M MD <https://github.com/shaheemazmalmmd>`_
- `Gaurav Mishra <https://github.com/GMishx>`_
- `Avinal Kumar <https://github.com/avinal>`_


Week 2 Progress
---------------

.. raw:: html

    <div class="alert alert-success" role="alert">
    <p>This week was mainly focused on creating CMake configuration for libraries, executables and coverage.
    <ul><li>Added the configuration for libraries and executables</li>
    <li>Resolved parallel build problems with coverage configs</li>
    <li>Implemented generated source configurations</li>
    <li>To test the current progress, follow the instructions <a href="https://github.com/avinal/FOSSology/wiki#test-the-new-system-only-gcc-with-make-and-ninja-tested-for-now">here</a></li>
    </ul></p>
    </div>
    <div class="embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item" src="/images/second-build.webm" allowfullscreen></iframe>
    </div>
    <br>

Discussions
-----------

* **Should I generalize the coverage build for each agent?**
  
  - Coverage depends on the agent_tests and may or may not be available for all the agent. So follow the Makefiles and add the configuration as it is in them.
  - Leave coverage for them who don't have it already in their Makefiles.
  
* **What are :code:`$(AGENTLIB) $(REPO) $(DB)` in the Makefiles?**

  - They seems to be remains of previous build configuration. Until there is a problem, ignore if you can not find the definitions.

* **Can I refactor the directory structure of nomos and monk, it will help keep the source code generation out of source directory?**

  - Yeah, sure. As long as it does not affects the working of the project you may refactor them to suit your needs.

* **I am facing problems with due to headers included using angled brackets, can I change them to double quotes instead?**

  - Yeah that would be okay, anyway the general practice is to add user header files using double quotes.

* **Using -Werror flag in regexscan causes build to fail, should I remove it?**

  - Since :code:`regexscan` is not the part of default build you can ignore it.

* **In scheduler source code the preprocessor macro value  for FOSSDB_CONF is different from that in lib, is that correct?**

  - We have made some changes, please change it to the same as in lib.


Conclusion and Further Plans
----------------------------

* Try adding the version and commit hash info.
* Implement writing version files for each build.
* Add proper comments in the :code:`CMakeLists.txt` files.
* Complete the coverage build configuration 
* Start implementing the install configurations

