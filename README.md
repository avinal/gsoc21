# New Build System and improving CI/CD workflow

<p align=center><a href="https://wakatime.com/badge/github/avinal/fossology"><img src="https://wakatime.com/badge/github/avinal/fossology.svg"></a></p>

This blog is for the project and meeting reports.

## Build System 

FOSSology’s build system is based on multilevel Make files that work together to supply a build infrastructure for the project. Although make is a robust build system but it is too outdated and slow compared to modern build systems. Although build configurations are not supposed to be updated as often as source files, there are few noticeable problems with make. This project will migrate the build system to a more user-friendly and popular CMake. 

## Workflow (Continuous Integration) 

Fossology has been using free Travis CI for all its continuous builds, tests, and deployment purposes throughout the organization. GitHub Actions supplies better integration, faster build times and is versatile in many other ways. This project aims at improving the overall CI/CD for the project as well as upgrade the targets and virtual platforms to the latest compatible versions. 

## Project Repository Information

### Working branch
https://github.com/avinal/fossology/tree/avinal/feat/cmake-buildsystem

### Working Discussion and issue
- https://github.com/fossology/fossology/discussions/1931
- https://github.com/fossology/fossology/issues/1913
