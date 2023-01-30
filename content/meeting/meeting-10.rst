*********************
Coding Week 9 Meeting
*********************

:date: 2021-08-06 22:47
:tags: gsoc, FOSSology
:category: report
:summary: This week I worked on CMake testing configuration. Most of the time was spent understanding the previous testing architecture.    
:slug: meeting-10
:status: published


.. raw:: html
  
  <div class="alert alert-info" role="alert">This week I worked on CMake testing configuration. Most of the time was spent understanding the previous testing architecture.</div>

Attendees
---------

- `Gaurav Mishra <https://github.com/GMishx>`_
- `Anupam Ghosh <https://github.com/ag4ums>`_
- `Avinal Kumar <https://github.com/avinal>`_


Week 9 Progress
---------------

.. raw:: html

    <div class="alert alert-success" role="alert">
    <ul><li>Initial CMake testing configuration added.</li>
    <li>Few tests working, e.g copyright, nomos</li>
    <li>Improved packaging configurations</li>
    <li>To test the current progress, follow the instructions <a href="https://github.com/avinal/FOSSology/wiki#test-the-new-system-only-gcc-with-make-and-ninja-tested-for-now">here</a></li>
    </ul>
    </div>

Discussions
-----------
   
- **Is this a necessity that tests must be run as the fossy user? Because when I run tests as me they as for permissions. But proceeds as the fossy user.**
   
  * No this is not required and this should not happen. They run under fossy as they sometimes require writing into /srv/fossology. But if they can run under other users that is an enhancement.
    
- **I am getting a lot of install issues in C/C++ agent tests?**
      
  .. code-block:: bash
    
    Start 3: delagent_unit_test
    
    3: Test command: /home/avinal/Documents/my_git/fossology/build/src/delagent/agent_tests/test_delagent
    3: Test timeout computed to be: 10000000
    3: install: cannot stat '/home/avinal/Documents/my_git/fossology/build/src/delagent/agent_tests/..//../../install/defconf/Db.conf': No such file or directory
    3: install: cannot stat '/home/avinal/Documents/my_git/fossology/build/src/delagent/agent_tests/..//VERSION': No such file or directory
    3: sh: 1: ../../../testing/db/createTestDB.php: not found
    3: Failed to run ../../../testing/db/createTestDB.php -c /home/avinal/Documents/my_git/fossologbuild/src/delagent/agent_tests/testconf -e, exit code is:127 .
    3/8 Test #3: delagent_unit_test ...............***Failed    0.02 sec
    
  * Not sure about the reason. I was suspecting Makefile but since they are gone now, I think PHP files are calling some shell commands causing this. 
      
    
- **Suggestions/Changes from Gaurav for fixing tests.**
    
  * For clib-tests, it needs to be called from PHP file (via PHPUnit) as it requires setting up a dummy repo. Check the :code:`src/lib/c/test/Makefile`
  * For missing services.xml, the test cases include :code:`src/lib/php/common-container.php` which loads the file. It expects it to be in current dir. Can be solved in two ways
    
    - Create another common-container.php just for test cases with correct paths.
    - Edit the current file and take the help of environment variables. For example, if a test variable is exported in env, find the XML relative to it otherwise continue as normal and this variable can be exported by CMake during the test.
      
  * Scheduler tests do need :code:`fossology_testconfig` from Makefile.deps which set up the srv and create test configurations, DB, etc.
      
    - Another shell script can be written to do all that and call it from CMake. The PHP file called makes everything required in /tmp so not an issue.
    - The locations like :code:`LOG_DIR, FOSSDB_CONF`, etc. in CMakeLists.txt can be changed to some other values. I am guessing this is the reason you were asked for the fossy password.
      
  * File :code:`src/copyright/agent_tests/Functional/cli_test.sh` needs to be edited to take paths relative to build dir. It can also be made into a .in file which is generated from CMake? So every path can easily be updated.
  * For PHP agents with missing version.php issue, there is a hack possible
      
    - Check https://www.php.net/manual/en/function.set-include-path.php
    - Another hack will be to use soft links for version.php in the source.
      
  * Other PHP issues like :code:`PHP Fatal error: Uncaught Error: Class 'Fossology\Lib\Agent\Agent' not found` can only be solved by editing composer.json before doing composer install (look for autoload: psr-4 ).
  * For delagent, pkgagent, mimetype issues, something can be done here: https://github.com/avinal/fossology/blob/avinal/feat/testing/src/testing/db/c/libfodbreposysconf.c#L349
    
    
Conclusion and Further Plans
----------------------------
    
- Raise a pull request for all the progress till now.
- Refactor the test source code according to suggestions.
- Implement remaining testing configurations.
        
        