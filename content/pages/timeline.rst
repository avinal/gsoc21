********
Timeline
********
:status: published
:summary: FOSSology’s build system is based on multilevel makefiles that work together to provide a build infrastructure for the project. Although make is a robust build system but it is too outdated and slow compared to modern build systems.

.. raw:: html

    <div>
    <span>Time spent: <a href="https://wakatime.com/badge/github/avinal/fossology"><img src="https://wakatime.com/badge/github/avinal/fossology.svg" ></a></span></div>
    <link rel="stylesheet" href="/theme/css/timeline.css">
    <div class="uk-container uk-padding">
    <div class="uk-timeline">
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2021-06-06">Community Bonding <br>(May 17th - June
                                    6th, 2021)</time></h4>
                            <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>  
                        </div>
                        <p><i class="fas fa-users"></i> Meetings:  
                        <a href="https://gsoc.avinal.space/posts/report/meeting-0.html">0</a>
                        <a href="https://gsoc.avinal.space/posts/report/meeting-1.html"> 1</a>
                        </p>
                    </div>
                    <div class="uk-card-body">
                        <p class="uk-text-progress">
                        <ul>
                            <li>Discussing and collaborating with fellow participants and getting familiar with the
                                FOSSology community and projects.</li>
                            <li>Since CMake is new for our FOSSology community, I will learn and bring in the resources
                                so that people get comfortable with it before the coding period starts.</li>
                            <li>Going through the codebase and plan strategies for the migration, his includes
                                identification of various types, segregation of libraries, executables, and
                                dependencies.</li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-06-13">Coding Week 1 <br>(June 7th - June
                                    13th,
                                    2021)</time></h4>
                                    <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div>
                        <p><i class="fas fa-users"></i> Meetings:  
                        <a href="https://gsoc.avinal.space/posts/report/meeting-2.html">2</a>
                        </p>
                    </div>
                    <div class="uk-card-body">
                        <p>
                        <ul>
                            <li>Plan the priority order of migration, and create lists for all different configuration
                            </li>
                            <li>Create CMake configuration for libraries.</li>
                            <li>There are approximately 8 libraries, since configuration are not that complex, it should
                                take no longer than 1 week of time to complete</li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-06-27">Coding Week 2 & 3 🚩<br>(June 14th -
                                    June 27th, 2021)</time></h4>
                                    <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div>
                        <p><i class="fas fa-users"></i> Meetings:  
                        <a href="https://gsoc.avinal.space/posts/report/meeting-3.html">3</a>
                        <a href="https://gsoc.avinal.space/posts/report/meeting-4.html"> 4</a>
                        </p>
                    </div>
                    <div class="uk-card-body">
                        <p>
                        <ul>
                            <li>If libraries are complete, migrate the agents one by one, since FOSSOlogy is based on a
                                modular architecture, many agents can be independently migrated.
                            </li>
                            <li>There are some 27 agents, 2 agents per day should take 2 weeks of time, hence I have
                                merged these weeks.</li>
                            <li>Time may vary for different agents to be migrated to CMake but on average this should
                                take 2 weeks of time.</li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-07-04">Coding Week 4 <br>(June 28th - July
                                    4th,
                                    2021)</time></h4>
                                    <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div>
                        <p><i class="fas fa-users"></i> Meetings:  
                        <a href="https://gsoc.avinal.space/posts/report/meeting-5.html">5</a>
                        <a href="https://gsoc.avinal.space/posts/report/meeting-6.html"> 6</a>
                        </p>
                    </div>
                    <div class="uk-card-body">
                        <p>
                        <ul>
                            <li>By now all the agents and libraries are migrated and now the top-level CMakeLists.txt
                                should be created. Since this file will be complex and will need all the child
                                configuration to work the testing and completion should approximately take 1 week of
                                time.
                            </li>
                            <li>This week will also check the overall gains in terms of performance and stability of the
                                new build system.</li>
                            <li>This is also the minimum requirement for the build system to be said working and to add
                                more configurations.
                            </li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-07-11">Coding Week 5 🚩<br>(July 5th - July
                                    11th,
                                    2021)</time></h4>
                                    <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div>
                        <p><i class="fas fa-users"></i> Meetings:  
                        <a href="https://gsoc.avinal.space/posts/report/meeting-7.html">7</a>
                        </p>
                    </div>
                    <div class="uk-card-body">
                        <p>
                        <ul>
                            <li>This week will continue the development of the Top-level CMake configuration.
                            </li>
                            <li>More configuration will be added for Install, Test, Uninstall, Package</li>
                            <li>If completed, testing will start and will continue for the next week
                            </li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-07-11">Coding Week 6 <br>(July 12th - July
                                    18th, 2021)</time></h4>
                            <span class="uk-label uk-label-evaluation uk-margin-auto-left">First Evaluation</span><span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div> 
                        <a href="https://gsoc.avinal.space/posts/report/first-evaluation.html">First Evaluation Report</a>
                    </div>
                    <div class="uk-card-body">
                        <p>
                        <ul>
                            <li>The build system is a very crucial element of the project, hence it must be tested
                                thoroughly before final rolling.
                            </li>
                            <li>This week I will continue the development of all required configuration and testing of
                                the new Build System.</li>
                            <li>By the end of this week the new build system will be able to properly build the project
                                and use the configurations, this also marks the end of the first phase and first
                                evaluation.
                            </li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-07-11">Coding Week 7 <br>(July 19th - July
                                    25th,
                                    2021)
                                </time></h4>
                                <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div>
                        <p><i class="fas fa-users"></i> Meetings:  
                        <a href="https://gsoc.avinal.space/posts/report/meeting-8.html">8</a>
                        </p>
                    </div>
                    <div class="uk-card-body">
                        <p>
                        <ul>
                            <li>With all the build system working, this week will be used to migrate the CI from Travis
                                to GitHub Actions starting with the C/C++ agent’s test
                            </li>
                            <li>Now the C++ agent tests will be executed using the new Build System</li>
                            <li>If completed then the PHPUnit test migration will start.
                            </li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-07-11">Coding Week 8 🚩<br>(July 26th - August
                                    1st,
                                    2021)
                                </time></h4>
                                <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div>
                        <p><i class="fas fa-users"></i> Meetings:  
                        <a href="https://gsoc.avinal.space/posts/report/meeting-9.html">9</a>
                        </p>
                    </div>
                    <div class="uk-card-body">
                        <p>
                        <ul>
                            <li>Complete the PHPUnit CI migration
                            </li>
                            <li>Add Docker tests</li>
                            <li>Start implementing source install test CI
                            </li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-07-11">Coding Week 9 <br>(August 2nd - August
                                    8th, 2021)
                                </time></h4>
                                <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div>
                        <p><i class="fas fa-users"></i> Meetings:  
                        <a href="https://gsoc.avinal.space/posts/report/meeting-10.html">10</a>
                        </p>
                    </div>
                    <div class="uk-card-body">
                        <p>
                        <ul>
                            <li>Complete Source Install CI</li>
                            <li>Start implementing workflow caching</li>
                            <li>Fixing bugs and clearing backlogs</li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-07-11">Coding week 10 🚩<br>(August 9th - August 15th, 2021) </time></h4>
                            <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div>
                        <p><i class="fas fa-users"></i> Meetings:  
                        <a href="https://gsoc.avinal.space/posts/report/meeting-11.html">11</a>
                        </p>
                    </div>
                    <div class="uk-card-body">
                        <p>
                        <ul>
                            <li>Checking the build system</li>
                            <li>Checking the CI/CD</li>
                            <li>Completing reports and documentation </li>
                            <li>Update the existing documentation and readme for the new build system and CI</li>
                        </ul>
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <div class="uk-timeline-item">
            <div class="uk-timeline-icon">
                <span class="uk-badge"><span uk-icon="check"></span></span>
            </div>
            <div class="uk-timeline-content">
                <div class="uk-card uk-card-default uk-margin-medium-bottom uk-overflow-auto">
                    <div class="uk-card-header">
                        <div class="uk-grid-small uk-flex-middle" uk-grid>
                            <h4 class="uk-card-title"><time datetime="2020-07-11">Final Evaluations 🚩<br>(August 16th -
                                    August 23rd, 2021)
                                </time></h4>
                                <span class="uk-label uk-label-success uk-margin-auto-left">Completed</span>
                        </div>
                    </div>
                    <div class="uk-card-body">
                        <p>
                            Code and report submission: <a href="https://gsoc.avinal.space/posts/gsoc/final-evaluation.html">Final Evaluation Report</a>
                        </p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    </div>
    <script src='https://cdn.jsdelivr.net/npm/uikit@3.4.2/dist/js/uikit.min.js'></script>

