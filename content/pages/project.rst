*******
Project
*******

:status: published

Build System
------------

FOSSology’s build system is based on multilevel Make files that work together to supply a build infrastructure for the project. Although make is a robust build system but it is too outdated and slow compared to modern build systems. Although build configurations are not supposed to be updated as often as source files, there are few noticeable problems with make. This project will migrate the build system to a more user-friendly and popular CMake. 

Workflow (Continuous Integration) 
---------------------------------

FOSSology has been using free Travis CI for all its continuous builds, tests, and deployment purposes throughout the organization. GitHub Actions supplies better integration, faster build times and is versatile in many other ways. This project aims at improving the overall CI/CD for the project as well as upgrade the targets and virtual platforms to the latest compatible versions.