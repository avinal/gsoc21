************
Hello CMake!
************

:status: published
:date: 2021-05-24 23:56
:slug: introduction-to-cmake
:category: cmake
:tags: cmake, gsoc, fossology, gsoc21
:summary: CMake stands for Cross-platform Make. Normally, a build tool like Make will parse a configuration file (Makefile) that contains all the commands required to build an artifact based on the source files and other resources inside the project.

.. role:: html-raw(raw)
    :format: html

I proposed a new architecture for FOSSology that uses CMake instead of bare-metal Make as a Google Summer of Code 2021 project. Although these tutorials will be useful for anyone interested in learning CMake they are specifically tailored to the FOSSology project. This is the first blog on CMake in this series. In this blog, I will discuss CMake syntax and various features.

:html-raw:`<h3>What is CMake?</h3>
<img class="float-md-right rounded border border-info ml-3" src="/images/cmake.png" style="max-width:300px;">`

CMake stands for Cross-platform Make. Normally, a build tool like Make will parse a configuration file (Makefile) that contains all the commands required to build an artifact based on the source files and other resources inside the project. On the other hand, CMake will also parse a configuration file (CMakeLists.txt), but instead of directly build the artifact, it’ll generate another configuration file that will build the artifact.

This approach is very common in Computer Science and is called *adding another level of indirection*. In short, you may say that:

:html-raw:`<div class="alert alert-secondary" role="alert">With just one configuration file you’ll be able to generate different configuration files to build your project for different platforms (Make, Visual Studio, etc).</div>` 

Another nice CMake feature is the so-called out-of-source build. Any file required for the final build, executables included, will be stored in a separated build directory (usually called build/). This prevents cluttering up the source directory and makes it easy to start over again: just remove the build directory and you are done.
 
:html-raw:`<h3>CMake Syntax</h3><img class="float-md-left mt-3 mr-3" src="https://imgs.xkcd.com/comics/compiling.png" style="max-width:310px;">`

CMake unlike Make is a configuration language itself. CMake supplies a rich library of inherent functions as well as common programming language features like conditions, looping, macros, and functions. In addition to that CMake is highly modular and you can always write a CMake module yourself independent of any project. Specifically for C/C++ programming, it supplies commands to find and link libraries automatically and lot many features. 


:html-raw:`<h4>Language Rules</h4>`

As mentioned above CMake is a language itself hence there are some language rules related to syntax, comments, variables, etc.  

* There are two types of comment in CMake, both start with :code:`#` character. The first one is line comments, as clear by name it is delimited by a newline. The other one is bracket comment and can span until the matching brackets are found. 

    .. code-block:: cmake

        # This is a line comment and it ends with the line.
        #[[This is a bracket comment and it can span up to multiple lines.
        But it is only supported in CMake 3.0 or later.]]


* Variables in CMake are like any other programming language. They are case-sensitive and have any alphanumeric characters. In general, it is recommended using upper case names as variables. They can be assigned and unassigned using :code:`set` and :code:`unset` commands. A variable can be referenced using :code:`${VARIABLE_NAME}`. 
  
  :html-raw:`<div class="alert alert-danger" role="alert">CMake reserves some types of identifers:<ul><li>begin with <b>CMAKE_</b> (upper-, lower-, or mixed-case)</li><li>begin with <b>_CMAKE_</b> (upper-, lower-, or mixed-case)</li><li>begin with <b>_</b> followed by the name of any CMake Command</li></ul></div>`


* The CMake commands are case insensitive in the latest version (3.0) of CMake. That means :code:`message()`, :code:`Message()` or :code:`MESSAGE()` are all same. 


:html-raw:`<h4>Basic CMake Commands</h4>`
  
* The :code:`project()` command is used to set the name of the CMake project and optionally a language that is used by the project. Every top-level CMake configuration must have this option set. The syntax is as below:

    .. code-block:: cmake

        project (projectname [CXX] [C] [Java] [NONE])


  If no language is specified then CMake defaults to supporting C/C++. If :code:`NONE` is specified then no language support is enabled.  

* The :code:`set()` command is used to set a variable to a value or lists of values. It is one of the most used CMake commands. The accompanying command is :code:`unset()`. The :code:`unset()` command is used to unset a variable or remove a variable from the current scope. The syntax for the three commands are:

    .. code-block:: cmake

        set (BLOG_TITLE "CMake Introduction")                # assign single value
        set (BLOG_TAGS "gsoc" "cmake" "fossology" "gsoc21")  # assign a list of values
        
        unset (BLOG_TITLE)                                   # unset BLOG_TITLE


* The :code:`message()` command can be used to display formatted messages with different alert modes. There are lots of `modes <https://cmake.org/cmake/help/v3.20/command/message.html#general-messages>` of displaying messages. The syntax is :

    .. code-block:: cmake

        message ([<mode>] "message text" ...)

        message(NOTICE "Hey this is ${BLOG_TITLE}")         # Example message with variable


* The :code:`cmake_minimum_required()` is used to set the minimum CMake version to use to generate the build files. If any older version is used than specified then the user gets an error message. It must be specified at the top of the *CMakeLists.txt* file.

    .. code-block:: cmake

        cmake_minimum_required (VERSION 3.0)

    
* The commands :code:`add_executable()` and :code:`add_library()` specifies what executables and libraries to build and what source files must be used to build them. One of the two commands must be used for any binary generation. 

    .. code-block:: cmake
    
        add_executable(<name> [WIN32] [MACOSX_BUNDLE] 
            [EXCLUDE_FROM_ALL] 
            [source1] [source2 ...])

        add_library(<name> [STATIC | SHARED | MODULE]
            [EXCLUDE_FROM_ALL]
            [<source>...])


:html-raw:`<h4>Flow Control</h4>`

CMake provides three flow control structures. They are conditional statements (:code:`if`), looping constructs (:code:`foreach` and :code:`while`) and procedure definitions (:code:`function` and :code:`macro`). I will explain each of them one by one.

* **Conditional Statements**
  The :code:`if` command in CMake is just like the :code:`if` command in any other language. It evaluates its expression and based on that either executes the code in its body or optionally the code in the :code:`else` clause.

    .. code-block:: cmake

        if (FOO)
            # do something here
        elseif (BAR)
            if (NESTED_BAR)
                # do something nested here
            endif(NESTED_BAR)
            # do something else
        else ()
            # do something here
        endif (FOO)


  You can use many operators to form complex conditions. Available options are **NOT**, **AND**, **OR**, **COMMAND**, **DEFINED**, **EXISTS**, **IS_DIRECTORY**, **IS_ABSOLUTE**, **MATCHES**, **IS_NEWER_THAN**,  and operators for numerical comparisons **EQUAL**, **LESS**, **GREATER**, **STRLESS**, **STREQUAL**, **STRGREATER**.

* **Looping Constructs**
  The :code:`foreach` command enables you to execute a group of CMake commands repeatedly on the members of a list.The first argument of the foreach command is the name of the variable that will take on a different value with each iteration of the loop. The remaining arguments are the list of values over which to loop.

    .. code-block:: cmake

        foreach(<loop_var> <items>)
            <commands>
        endforeach()

        
  The :code:`while` command provides for looping based on a test condition. The format for the test expression in the :code:`while` command is the same as that for the :code:`if` command described earlier.

    .. code-block:: cmake
    
        while(<condition>)
            <commands>
        endwhile()

  It is worth mentioning that foreach loops can be nested and that the loop variable is replaced prior to any other variable expansion. This means that in the body of a foreach loop you can construct variable names using the loop variable.


* **Procedure Definitions**
  A function in CMake is very much like a function in C or C++. You can pass arguments into it, and the arguments passed in become variables within the function. The first argument is the name of the function to define. All additional arguments are formal parameters to the function.

    .. code-block:: cmake

        function(<name> [<arg1> ...])
            # write the function body here
            <commands>
        endfunction()


  Macros are defined and called in the same manner as functions. The main differences are that a macro does not push and pop a new variable scope, and the arguments to a macro are not treated as variables but are string replaced prior to execution. This is very much like the differences between a macro and a function in C or C++. The first argument is the name of the macro to create. All additional arguments are formal parameters to the macro.

    .. code-block:: cmake

        macro(<name> [<arg1> ...])
            # write macro definition here
            <commands>
        endmacro()
        

:html-raw:`<h3>A Hello CMake example</h3>`

This example compiles a simple *hello_cmake* program. This example and the terminal commands are used in Linux context, however there is very little difference in different platforms. Make sure to `install CMake <https://cmake.org/install/>`_ for your platform.

* Create a folder and create a file named :code:`hello_cmake.cpp` in that. You may add your own code. Here is my example code.

    .. code-block:: cpp

        #include<iostream>

        int main() {
            std::cout << "Hello CMake\n";
            return 0;
        }


* Create another file named :code:`CMakeLists.txt` and add the following script in that file.
  
    .. code-block:: cmake

        cmake_minimum_required(VERSION 3.0)

        # set project name
        project(hello_cmake)

        # print compiler info
        message("The compiler is ${CMAKE_CXX_COMPILER}")

        # add executable
        add_executable(Hello_cmake hello_cmake.cpp)


* Create another directory :code:`build` and run the following commands.

    .. code-block:: bash

        # create folder and change directory
        mkdir build && cd build

        # run cmake config
        cmake ..

        # build project
        cmake --build .

You will be able to see a :code:`Hello_cmake` binary in the *build* folder. Hooray you have successfully built a project using CMake. For more `read here <https://cmake.org/cmake/help/v3.20/guide/tutorial/index.html>`_. In the next blog I will explain how to create CMake configuration for a more complex project. 

:html-raw:`<p align=center>Thanks!`


:html-raw:`<h3>References and Credits</h3>`

* `CMake Website <https://cmake.org>`_
* `CMake Documentation <https://cmake.org/cmake/help/latest/index.html>`_
* `Mastering CMake Book <https://www.kitware.com/what-we-offer/#books>`_
* `CMake Tutorial <https://cmake.org/cmake/help/v3.20/guide/tutorial/index.html>`_
* `You (C)Make Me Happy <https://prateekvjoshi.com/2014/02/01/cmake-vs-make/>`_
* `Compiling xkcd.com <https://xkcd.com/303/>`_
