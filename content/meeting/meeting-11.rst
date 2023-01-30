**********************
Coding Week 10 Meeting
**********************

:date: 2021-08-14 22:47
:tags: gsoc, FOSSology
:category: report
:summary: This week I implemented CMake testing configuration and fixed most of the tests. As of now all but 5 tests are working fine.    
:slug: meeting-11
:status: published


.. raw:: html
  
  <div class="alert alert-info" role="alert">This week I implemented CMake testing configuration and fixed most of the tests. As of now all but 5 tests are working fine.</div>

Attendees
---------

- `Michael C. Jaeger <https://github.com/mcjaeger>`_
- `Anupam Ghosh <https://github.com/ag4ums>`_
- `Avinal Kumar <https://github.com/avinal>`_



Week 9 Progress
---------------

.. raw:: html

    <div class="alert alert-success" role="alert">
    <ul><li>Testing configuration for all agents added</li>
    <li>GitHub Actions Configuration added</li>
    <li>Fixed and refactored most of the tests</li>
    <li>Raised a pull request for all the works till now. <a href="https://github.com/fossology/fossology/pull/2075">#2075</a></li>
    <li>To test the current progress, follow the instructions <a href="https://github.com/avinal/FOSSology/wiki#test-the-new-system-only-gcc-with-make-and-ninja-tested-for-now">here</a></li>
    </ul>
    </div>

Discussions
-----------

- **I suspect that the Ojo regression test's expected data file is outdated**

  * Michael said that on their internal Jenkins CI, these tests are not being run currently, so this might be possible that the file is outdated.

- **Since some of the tests need Makefile to install while testing, CMake generated Makefiles and test Makefiles are conflicting, and hence we are forced to use Ninja for testing. What can I do about it?**

  * Michael suggested using :code:`--file=filename` flag with the make command and change the name of the test Makefile to something else. This will solve the problem.

- **Mimetype is detecting executables as shared lib, is that expected or needs to be fixed?**

  * Mimetype internally depends on the *file* command to get the mime-type. If the output of the *file* command is also the same then it is okay.

- **What is** :code:`folderlist` **in https://github.com/fossology/fossology/blob/master/src/delagent/agent_tests/Functional/ft_cliDelagentTest.php#L126 ?**

  * :code:`folderlist` is a view. Use :code:`createViews()` function.

- **Suggestions/Changes from Gaurav for fixing phpunit tests.**

  * Please note the changes in :code:`setUp()` function in :code:`src/lib/php/tests/test_common_license_file.php`
  * The test database name is given to the constructor of TestPgDb and can be anything as it gets deleted in :code:`teardown()`
  * The :code:`dbmanager` is provided by the object, no need to initialize global :code:`PG_CONN` (it will be exposed by the library in case some of the functions need it).
  * All the tables needs to be explicitly mentioned to :code:`createPlainTables()` and their corresponding :code:`createSequences()` (you can get them using :code:`\d tablename` from existing DB easily. Then call the :code:`alterTables()` to update the sequence. (I am not sure if :code:`createConstraints()` is required at all, try to remove)
  * :code:`tearDown()` is pretty easy, just need to call :code:`fullDestruct()`. For debugging, you can add :code:`exit(-1);` after any line you as suspecting, connect to DB and checkout the database, select/inspect tables.
  * There is also :code:`TestInstaller` class in case any of test case needs the whole mods-enabled with fossology.conf, VERSION, etc. Please check :code:`src/cli/tests/test_fo_copyright_list.php` for quick reference.


Conclusion and Further Plans
----------------------------

- Fix the remaining tests.
- Add week 8, 9 reports.
- Add Final Evaluation Report.
- Complete Final Evaluation.
    
    