***********************
Coding Week 4 Meeting-2
***********************

:date: 2021-07-02 22:22
:tags: gsoc, FOSSology
:category: report
:summary: In this eighth meeting questions related to post install generation were asked. This was a short meeting.  
:slug: meeting-6
:status: published

.. raw:: html
  
  <div class="alert alert-info" role="alert">In this eighth meeting questions related to post install generation were asked. This was a short meeting.  </div>

Attendees
---------

- `Gaurav Mishra <https://github.com/GMishx>`_
- `Avinal Kumar <https://github.com/avinal>`_


Week 4 Progress
---------------

.. raw:: html

    <div class="alert alert-success" role="alert">
    <ul><li>Version parsing logic implemented.</li>
    <li>VERSION and COMMIT_HASH added to every executables.</li>
    <li>Installing part is complete except <code>cli</code>.</li>
    <li>Symbolic Links are installing and working fine.</li>
    <li>Version, Symbolic Links, <code>VERSION</code> file generation, <code>version.php</code> generation are now more modular and called via a single function for each agent</li>
    <li>Most dependencies are now moved to single configuration file.</li>
    <li>Vendor directory generation and installing are now working.</li>
    <li>To test the current progress, follow the instructions <a href="https://github.com/avinal/FOSSology/wiki#test-the-new-system-only-gcc-with-make-and-ninja-tested-for-now">here</a></li>
    </ul>
    </div>

Discussions
-----------

* **Why all the symbolic links in cli points to** :code:`fo_wrapper` **script?**

  - The :code:`fo_wrapper` script calls the PHP script on the symbolic link that called the fo_wrapper. It also initializes any requirement before calling the scripts.
  
* **How to generate all the other configuration in** :code:`/usr/local/etc/fossology` **directory?**

  - You can find the input files for all these configurations in the :code:`install/defcon` directory. 

* **What are** :code:`OBSOLETEFILES` **in** :code:`www/ui/Makefile` **?**

  - They are kept for compatibility purposes. Although they have been removed in the current versions of FOSSology, if a user installs a new version on top of an older instance, then we should explicitly remove those files.

* **I have created a separate folder for generating vendor directory. Is that okay?**

  - Yeah, it should be fine, But it would be better to rename it to something else. Or even better if moved to *www* itself. Since these files are used by www.

Conclusion and Further Plans
----------------------------

- Move :code:`vendor` scripts to :code:`www` directory.
- Implement installing for FOSSology cli.
- Implement installing configuration scripts.
- Finish installation for testing

