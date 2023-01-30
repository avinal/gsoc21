***************************
Community Bonding Meeting 0
***************************

:date: 2021-05-28 21:00
:tags: gsoc, fossology, 
:category: meet
:summary: This meeting is the first of the recurring weekly GSoC project meetings. In this meeting the current status of progress according to the proposal was discussed and some topics related to current build system based on Make and the new build system based on CMake. 
:slug: meeting-0
:status: published


.. raw:: html
  
  <div class="alert alert-info" role="alert">This meeting is the first of the recurring weekly GSoC project meetings. In this meeting the current status of progress according to the proposal was discussed and some topics related to current build system based on Make and the new build system based on CMake.</div>

Attendees
---------
- `Gaurav Mishra <https://github.com/GMishx>`_
- `Anupam Ghosh <https://github.com/ag4ums>`_
- `Ayush Bhardwaj <https://github.com/hastagAB>`_
- `Avinal Kumar <https://github.com/avinal>`_


Discussions
-----------

* **The current progress according to schedule**

  - The blog on CMake is on the way. 
  - I have gone through the Makefiles to get a rough estimate of the work. 
  - Published the GSoC project blog 
  
* **How are agents related to each other in terms of compilation?**

  - Each agent is independently compiled and generally use the source code in :code:`lib` folder. If any agent needs other agent then it uses the library files instead.
   
* **Does every agent have a executable and library?**
  
  - Not necessarily, there are agents written in C, C++ and PHP, depending on what is the use the configuration can be different.


Conclusion and Further Plans
----------------------------

* It would be better if I get started by creating CMake configuration for any of the agent.
* Fork and create a branch for development and mention the same in blog or wiki. 
* Add a timeline section in blog or wiki as provided in the project proposal.
* Publish the CMake introductory blog.
* Prepare a prototype/plan for next week.
* Find out the best alternative for handling the global variables.

