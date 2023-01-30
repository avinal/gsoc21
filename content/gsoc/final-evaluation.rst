***********************
Final Evaluation Report
***********************

:date: 2021-08-19 23:07
:tags: gsoc, FOSSology
:category: report
:summary: In the second phase of GSoC 2021 @ The FOSSology Project, I worked on testing and packaging configuration. I also migrated the CI services from Travis CI to GitHub Actions. 
:slug: final-evaluation
:status: published

.. role:: rd

.. role:: gr

.. role:: or

.. role:: html-raw(raw)
    :format: html

.. raw:: html

    <style> 
    .rd {color:red;font-weight:bold} 
    .gr{color:green;font-weight:bold}
    .or{color:orange;font-weight:medium} 
    ul{margin-bottom:0}
    </style>

The CMake Build system
----------------------

FOSSology is quite an old and mature project. The project has been using bare metal **Makefiles**. As the project is growing with new agents and modernization it was required to have a modern build system. 

The FOSSology is a suite of well-integrated and synchronized sub-projects (called agents) written in C, C++, and PHP. Most of the major agents are in C, C++ and that made CMake an obvious choice for a new build system for FOSSology. CMake is a versatile set of build, test, and packaging tools and is the most popular choice of C/C++ developers. CMake can be extended to create a build system for other languages too via custom scripts. 


GitHub Actions CI/CD
--------------------

.. image:: /images/ci.png
    :class: float-md-right rounded border border-info ml-3
    :alt: A CI Meme
    :width: 350

Since the FOSSology project moved on Github, it has used only the free Travis CI service for OSS projects. 
At the time of writing the Travis CI has reduced its free tier CI services. GitHub Actions provides faster builds. Since GitHub Actions is a fully managed service by GitHub, we don’t need to know how to scale and operate the infrastructure to run it. 

It is straightforward to use with GitHub because when we fork a repository, the actions automatically get forked. This allows you to test and build projects very efficiently and even run them closer to the developer. Also, you have readily available access to the GitHub API, making it more popular among developers.

Improvements over previous build system and CI
----------------------------------------------

The new build system and CI brings a lot of improvements and features. The list below describes them.

- CMake enforces out-of-source builds. This was already possible with the previous build system but not a strict requirement. This feature keeps the source code clean and makes cleaning the build artifacts easy. (Just remove the build folder :)
- One of the major improvements over the previous build system is faster build times. CMake generates parallel build-enabled configurations for all generators. In our tests, the new build system is at least twice as fast as the previous one. With further improvement in configuration, we will be able to further cut the build times. 
- Previously FOSSology can only be built using *Unix Makefiles*. With CMake, we can now use many other popular generators such as *Ninja*.
- Now it is also very flexible to choose different compilers. This will help support more platforms and architecture in the future. As of now, we are experimenting with Clang compilers. 
- FOSSology is quite an old project and a lot of agent testing code was written in the last decade. Initially, none of them were compatible with the new build system, but we were able to hack most of the test code using better-improved methods. Test times have also improved.
- Migrating from Travis CI to GitHub Actions was another big move and for the most part, it removes the dependency on a third-party CI service. Along with that GitHub Actions provides better build times, tons of new features, and better integration with other GitHub services. 




Deliverables
--------------

.. raw:: html

    <div class="alert alert-info" role="alert">
    <ul class="simple">
    <li>Final Pull Request <a class="badge badge-info" href="https://github.com/fossology/fossology/pull/2075">#2075</a></li>
    <li>Pull Request Branch <a class="badge badge-info" href="https://github.com/avinal/fossology/tree/avinal/feat/buildsystem">avinal/feat/buildsystem</a></li>
    <li>Working Branch (individual commits) <ul>
    <li><a class="badge badge-info" href="https://github.com/avinal/fossology/tree/avinal/feat/cmake-buildsystem">avinal/feat/cmake-buildsystem</a></li>
    <li><a class="badge badge-info" href="https://github.com/avinal/fossology/tree/avinal/feat/testing">avinal/feat/testing</a></li>
    </ul></li>
    <li>Project Issue <a class="badge badge-info" href="https://github.com/fossology/fossology/issues/1913">#1913</a></li>
    <li>Project Discussion <a class="badge badge-info" href="https://github.com/fossology/fossology/discussions/1931">#1931</a></li>
    <li>Weekly Reports<ul>
    <li><a class="badge badge-info" href="https://gsoc.avinal.space">Personal Blog</a></li>
    <li><a class="badge badge-info" href="https://fossology.github.io/gsoc/docs/2021/buildsystem/">FOSSology Official Blog</a></li>
    </ul></li></ul>
    </div>


**CMake Build System Tasks**

.. table::
    :class: table table-sm table-hover table-bordered table-responsive
    :widths: 5 15 10 10 20 15 25
    :align: center

    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | #  | Agents           | Build     | Install   | Testing            | Packaging | Remarks        |
    +====+==================+===========+===========+====================+===========+================+
    | 1  | adj2nest         | :gr:`YES` | :gr:`YES` |                    | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 2  | buckets          | :gr:`YES` | :gr:`YES` |                    |  :gr:`YES`|                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 3  | cli              | :gr:`YES` | :gr:`YES` | - :rd:`Functional` | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 4  | copyright        | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           |                |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 5  | debug            |           | :gr:`YES` |                    | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 6  | decider          | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           |                |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 7  | deciderjob       | :gr:`YES` | :gr:`YES` | - :gr:`Functional` | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 8  | delagent         | :gr:`YES` | :gr:`YES` | - :rd:`Functional` |           |                |
    |    |                  |           |           | - :rd:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 9  | demomod          | :or:`YES` | :or:`YES` | - :or:`Functional` | :or:`NO`  | *(Not Used)*   |
    |    |                  |           |           | - :or:`Unit`       |           |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 10 | example_wc_agent | :or:`YES` | :or:`YES` | - :or:`Functional` |  :or:`NO` | *(Not Used)*   |
    |    |                  |           |           | - :or:`Unit`       |           |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 11 | clib             | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           |                |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 12 | cpplib           | :gr:`YES` | :gr:`YES` | - :gr:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 13 | phplib           | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           | 1 functional   |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` | test needs fix |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 14 | maintagent       | :gr:`YES` | :gr:`YES` |                    | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 15 | mimetype         | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           |                |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 16 | monk             | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           |                |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 17 | ninka            | :or:`YES` | :or:`YES` | - :or:`Functional` | :or:`NO`  | *(Deprecated)* |
    |    |                  |           |           | - :or:`Unit`       |           |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 18 | nomos            | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           |                |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 19 | ojo              | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           | 1 functional   |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` | test needs fix |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 20 | pkgagent         | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           |                |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 21 | readmeoss        | :gr:`YES` | :gr:`YES` |                    | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 22 | regexscan        | :or:`YES` | :or:`YES` |                    |  :or:`NO` | *(Deprecated)* |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 23 | reportImport     | :gr:`YES` | :gr:`YES` |                    | :gr:`YES` |                |               
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 24 | reuser           | :gr:`YES` | :gr:`YES` | - :gr:`Functional` | :gr:`YES` |                |                
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 25 | reso             | :gr:`YES` | :gr:`YES` |                    | :gr:`YES` |                |                  
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 26 | scheduler        | :gr:`YES` | :gr:`YES` | - :rd:`Functional` |           | Tests needs    |
    |    |                  |           |           | - :rd:`Unit`       | :gr:`YES` | fix            |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 27 | softwareHeritage | :gr:`YES` | :gr:`YES` |                    | :gr:`YES` |                |                 
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 28 | spasht           | :gr:`YES` | :gr:`YES` |                    | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 29 | spdx2            | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           | 1 Test failing |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` | in CI          |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 30 | unifiedreport    | :gr:`YES` | :gr:`YES` | - :gr:`Functional` | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 31 | ununpack         | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           | Unit tests     |
    |    |                  |           |           | - :rd:`Unit`       | :gr:`YES` | needs fix      |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 32 | wget_agent       | :gr:`YES` | :gr:`YES` | - :gr:`Functional` |           |                |
    |    |                  |           |           | - :gr:`Unit`       | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+
    | 32 | www              | :gr:`YES` | :gr:`YES` | - :rd:`UI`         | :gr:`YES` |                |
    +----+------------------+-----------+-----------+--------------------+-----------+----------------+


**GitHub Actions CI Tasks**    

.. table::
    :class: table table-sm table-hover table-bordered table-responsive
    :widths: 5 25 70
    :align: center
    
    +---+------------------------+----------------------------------------------------------+
    | # | CI Tasks               | Status                                                   |
    +===+========================+==========================================================+
    | 1 | :gr:`build`            | Added Ubuntu 20.04 GCC 8, 9 and Clang, GCC 7 not working |
    +---+------------------------+----------------------------------------------------------+
    | 2 | :gr:`c/cpp unit test`  | Added, delagent, scheduler and ununpack not working      |
    +---+------------------------+----------------------------------------------------------+
    | 3 | :gr:`phpunit tests`    | Added, delagent and scheduler  functional not working    |
    +---+------------------------+----------------------------------------------------------+
    | 4 | :rd:`cahching`         | Not implemented                                          |
    +---+------------------------+----------------------------------------------------------+
    | 5 |:rd:`source install`    | Not implemented                                          |
    +---+------------------------+----------------------------------------------------------+
   
(:gr:`GREEN`: COMPLETED, :rd:`RED`: INCOMPLETE, :or:`ORANGE`: NOT NEEDED/DEPRECATED)
    


How it works and how to use it?
-------------------------------

.. raw:: html

    <div class="embed-responsive embed-responsive-16by9">
        <iframe class="embed-responsive-item" src="/images/second-build.webm" allowfullscreen></iframe>
    </div>

The new build system retains the modular and hierarchical structure of the previous build system.  On the other hand, the new build system provides several new flags to control the build. The new build system forces out-of-source build instead of the previous in-source builds. This keeps the source clutter-free and reduces the chance of accidentally deleting source files. *Testing still needs some in-source artifacts, this will be solved once all the tests are fixed according to the new build system.* 

Each agent is a complete CMake sub-project with its independent configuration for building, installing, and testing. That means a single agent can be built and installed separately and even removed from the default build without breaking other builds. The directory structure is as below.

.. code-block:: bash

    .
    ├── build                           # temporary directory for build artifacts
    ├── cmake                           # CMake modules for FOSSology
    │   ├── FoPackaging.cmake           # CMake Packaging configurations
    │   ├── FoUtilities.cmake           # Custom CMake utilities 
    │   ├── FoVersionFile.cmake         # VERSION version.php CMake template file   
    │   ├── SetDefaults.cmake           # CMake defaults for this project   
    │   ├── TestInstall.make.in         # Template makefile for install during tests
    │   └── VERSION.in                  # VERSION file template
    ├── src                             
    │   ├── agent-1                     # Agent sub-project
    │   │   ├── agent                   # Agent's source code directory
    │   │   │   ├── agent-source-code
    │   │   │   └── CMakeLists.txt
    │   │   ├── agent_tests             # Agent's test directory    
    │   │   │   ├── Unit
    │   │   │   ├── Functional
    │   │   │   └── CMakeLists.txt
    │   │   ├── ui                      # Agent's UI source code
    │   │   │   ├── templates
    │   │   │   └── agent-ui-code
    │   │   └── CMakeLists.txt          # Agent's top-level CMake configuration
    :   :
    │   ├── other agents
    :   :
    │   └── CMakeLists.txt              # Source intermediate CMake configuration
    :
    ├── other directories and files
    :
    └── CMakeLists.txt                  # FOSSology Top-level CMake configuration 


The :code:`cmake` directory contains customized CMake modules and templates for FOSSology. This directory is required for all the operations. The general workflow of the new build system as well as how to use it as described below.

1. Since the new build system is still in review. You must fork FOSSology and pull the `#2075 <https://github.com/fossology/fossology/pull/2075>`_ pull request branch. Once you are in FOSSology root, run these commands.

    .. code-block:: bash

        git fetch https://github.com/avinal/fossology avinal/feat/buildsystem:buildsystem
        git checkout buildsystem


2. The first step towards building is to create a temporary directory for storing intermediate files and build artifacts. By convention we use a directory named :code:`build`, but you can use any name. (**NOTE: For testing do not use other names**)

    .. code-block:: bash

        mkdir build
        cd build


3. In the next steps, we will configure the CMake project and generate the required configurations. You can use several flags to control the build. Given below are the flags available for this project.

    .. table::
        :class: table table-sm table-hover table-bordered table-responsive

        +-----------------------------------+--------------------------------------------+--------------------+
        | CMake Flags                       | Description                                | Default            |
        +===================================+============================================+====================+
        | **-DCMAKE_INSTALL_PREFIX=<path>** | Sets the install prefix.                   | :code:`/usr/local` |
        +-----------------------------------+--------------------------------------------+--------------------+
        | **-DAGENTS="agent1;agent2..."**   | Only configure these agents.               | ALL AGENTS         |
        +-----------------------------------+--------------------------------------------+--------------------+
        | **-DOFFLINE=<ON/OFF>**            | Controls vendor generation, ON=NO          | **OFF**            |
        +-----------------------------------+--------------------------------------------+--------------------+
        | **-DCMAKE_BUILD_TYPE=<type>**     | - :code:`Debug`                            |                    |
        |                                   | - :code:`Release`                          |  :code:`Debug`     |
        |  - Controls build type aka        | - :code:`RelWithDebInfo`                   |                    |
        |    level optimisation             | - :code:`MinSizeRel`                       |                    |
        +-----------------------------------+--------------------------------------------+--------------------+
        | **-DTESTING=<ON/OFF>**            | Controls testing config generation         |  **OFF**           |
        +-----------------------------------+--------------------------------------------+--------------------+
        | **-DMONOPACK=<ON/OFF>**           | Package adj2nest and ununpack seperately   | **OFF**            |
        +-----------------------------------+--------------------------------------------+--------------------+
        | **-GNinja**                       | Use Ninja instead of Unix Makefiles        | *Unix MakeFiles*   |
        +-----------------------------------+--------------------------------------------+--------------------+

    There are lots of inbuilt CMake command-line options you can see them in the official `documentation <https://cmake.org/cmake/help/v3.10/manual/cmake.1.html>`_. Once you have chosen your flags we can now configure the project using the following commands.

    .. code-block:: bash
        
        # From build folder
        cd <name-of-build-directory>
        cmake <flags> ..


4. The next step is to build the project. You can use parallel jobs to build faster. For more options you can type :code:`cmake --help` or :code:`make --help` or :code:`ninja --help`. 

    .. code-block:: bash

        # Common build command for all generators, 
        # Default number of parallel builds depends on generator used
        cmake --build . --parallel <no-of-processes>

        # For Unix Makefiles, no parallel build by default
        make -j <no-of-processes>

        # For Ninja, 8+ parallel build by default (depends on system)
        ninja -j <no-of-processes>


5. Installing is also as easy as building. You can choose to install only certain components even if you have built the whole project. If you directly invoke the install command without building the project, it will automatically build the project first.

    .. code-block:: bash

        # For Unix Makefiles
        make install

        # For Ninja
        ninja install


6. While testing has some issues, but most of the testing is working fine. For now, you must build and run any test from the FOSSology root directory only. You can choose to configure a single agent if you want to test one agent only. See :code:`ctest --help` for controlling test runs.

    .. code-block:: bash

        # Common testing command
        ctest --parallel <no-of-processes>

        # For Unix Makefiles
        make test

        # For Ninja
        ninja test


7. You can package FOSSology, the packaging currently lacks copyright and conf files. But for testing purposes, you can use the following commands. Similar to installing, if you run the package command without building the project, it will automatically build the project first. See :code:`cpack --help` for more packaging options.

    .. code-block:: bash

        # Common testing command
        cpack

        # For Unix Makefiles
        make package

        # For Ninja
        ninja package


Known Issues and Drawbacks
--------------------------

Although the transition from Makefiles to CMake and Travis CI to GitHub Actions is almost complete and working as expected. But it is not free of drawbacks and issues. This section outlines the known issues at the time of writing. 

.. image:: https://imgs.xkcd.com/comics/conference_question.png
    :class: float-md-right rounded border border-info ml-3
    :alt: A Bug Meme
    :width: 350


- Coverage builds may fail with linking errors.
- Packaging prefix is the same as the install prefix. This requires the developer to set the install prefix manually before packaging to produce packages with the correct directory structure.
- Testing and packaging must be used from the FOSSology root directory. Not doing so may or may not configure the project as intended.
- Previously tests were written hardcoded for the Makefiles. But new build system requires all artifacts to be generated in a separate directory. This required me to add symbolic links wherever a generated script or file is expected. Tests can still leave some artifacts inside source folders.
- There is no easy way to install a particular agent from the FOSSology root directory.
- Packages don't contain copyright, readme, and license files. CMake doesn't provide a way to include these files. This is being tracked by issue `#21832 <https://gitlab.kitware.com/cmake/cmake/-/issues/21832>`_.
- While packaging the symbolic links may or may not be dereferenced and hence results in copying the folder too in the target directory.
- Running tests locally may require switching to :code:`fossy` user.
- While configured for testing, it may give permission errors.
- Scheduler, Ununpack, and Delagent unit and functional tests are not working. I have added an issue `#2084 <https://github.com/fossology/fossology/issues/2084>`_ to track the progress on fixing these tests.
- CMake doesn't generates uninstall targets. The closest thing to uninstall is `this snippet <https://gitlab.kitware.com/cmake/community/-/wikis/FAQ#can-i-do-make-uninstall-with-cmake>`_. This will be later added to the FOSSology.


Challenges Faced
----------------

While this whole project was challenging, some aspects of it were unforeseen and more challenging. When I decided to go on with this project I just had enough CMake knowledge to write a configuration for a very small project. I had never used CMake on this big scale. On the other side, the FOSSology community is largely unknown to CMake so for all of us it was learn, practice, and implement. With support from mentors, I was able to overcome this challenge with flying colors.

The other challenge was to understand the old build system, how they are all connected and what is the flow. The complexity can be imagined by the fact that the most of code and configurations were written in the decade before the last decade and haven't changed much since then.

The most challenging task was to make tests work with the new build system. Since tests were mostly hardcoded and the new build system refactored many of the files and directory, the tests were failing initially. The testing part took me the most time. All thanks to my mentor Gaurav I was able to hack them to suit the new build system.

Related Resources and Links
---------------------------

- Fix FOSSology agent tests issue `#2084 <https://github.com/fossology/fossology/issues/2084>`_ 
- feat(CI): Migrate API docs generation and deployment to GitHub Actions pull request `#1917 <https://github.com/fossology/fossology/pull/1917>`_
- feat(CI): Migrate Static Checks and Analysis to GitHub Actions from Travis CI `#1919 <https://github.com/fossology/fossology/pull/1919>`_  


Future Development Plans
------------------------

There is a lot to do with the new build system and CI and it will probably take a year or to reach a maturity point. I was able to meet most of the goals but some of them are remaining. 

- Fix the tests, probably renovate them from the ground up.
- Find a hack for packaging problems.
- Improve and optimize the build.
- Modernise the source code, remove old, bloated code and replace them according to new standards.


What did I learn from this project?
-----------------------------------

This Google Summer of Code was the busiest time of my life for all good reasons. I learned a lot about license compliance and how it all works in the software industry. The next big thing is CMake. As I mentioned I was just a novice user of CMake. Now I am confident that given any other large project I will be able to migrate it/improve it. I got to learn PHP, of which I did not know a single word before GSoC. And finally, I learned about packing and testing. I had these courses but implementing them myself and fixing them was a wholesome experience. 

Other than that I improved on my communication and presentation skills. Collaborating with fellow participants was one of the great things that happened during GSoC.


Acknowledgments
---------------

Google Summer of Code is the best thing that has happened to me this year so far. Although there are numerous people to say thanks to, I want to mention key people who were my motivation and support during this period. 

First of all, I want to thank and appreciate my mentors `Gaurav Mishra <https://github.com/GMishx>`_, `Michael C. Jaeger <https://github.com/mcjaeger>`_, `Anupam Ghosh <https://github.com/ag4ums>`_, and `Shaheem Azmal M MD <https://github.com/shaheemazmalmmd>`_. Without the help and support from them, all this would not have been possible. They are very polite, knowledgeable, and helpful. 


Finally, I want to thanks, my family and friends. I got to meet many awesome developers as my fellow participants from around the world, I wish we will do more collaboration in the future.

