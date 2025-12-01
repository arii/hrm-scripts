title:	Refactor: Centralize Spotify API Client
state:	OPEN
author:	google-labs-jules
labels:	
comments:	2
assignees:	
projects:	
milestone:	
number:	707
--
This pull request centralizes the Spotify API client, refactoring the polling and playlist services to use a new singleton service. This eliminates redundant code, improves maintainability, and restores critical error handling and test coverage that were identified as issues in a prior code review. All unit tests, linting, and build checks are passing.

Fixes #542

---
*PR created automatically by Jules for task [13582039671530638763](https://jules.google.com/task/13582039671530638763) started by @arii*
title:	Comprehensive Codebase & Configuration Cleanup
state:	OPEN
author:	google-labs-jules
labels:	
comments:	3
assignees:	
projects:	
milestone:	
number:	705
--
This submission includes a comprehensive cleanup of the codebase, which addresses several issues related to technical debt and maintainability. Key improvements include consolidating the Jest configuration, removing unused dependencies, cleaning up npm scripts, and deleting legacy files. These changes result in a more streamlined and efficient repository.

Fixes #406

---
*PR created automatically by Jules for task [4090864511577426108](https://jules.google.com/task/4090864511577426108) started by @arii*
title:	Create a script in package.json to lint all JavaScript files
state:	OPEN
author:	google-labs-jules
labels:	
comments:	1
assignees:	
projects:	
milestone:	
number:	704
--
This change adds a new script to `package.json` that executes the configured linter (ESLint) across all relevant JavaScript files in the project. This will help maintain code quality and identify potential issues early.

Fixes #556

---
*PR created automatically by Jules for task [10449798609748544848](https://jules.google.com/task/10449798609748544848) started by @arii*
title:	Heart Rate Data Processing and Analytics Utility
state:	OPEN
author:	google-labs-jules
labels:	
comments:	1
assignees:	
projects:	
milestone:	
number:	702
--
This change introduces a new backend utility for processing and analyzing raw heart rate data, including a new `HeartRateService` and workout lifecycle commands.

Fixes #546

---
*PR created automatically by Jules for task [4610950311134844260](https://jules.google.com/task/4610950311134844260) started by @arii*
title:	Fix Dashboard HRM Sync
state:	OPEN
author:	google-labs-jules
labels:	
comments:	1
assignees:	
projects:	
milestone:	
number:	701
--
Introduces a REGISTER_PLAYER WebSocket event to immediately notify the server upon a successful Bluetooth HRM connection.

Previously, the dashboard would only display a new player after the first heart rate data point was received, leading to a perceived delay and incorrect connection status.

This change ensures the dashboard updates in real-time, reflecting the true connection state of all HRM clients.

Fixes #650

---
*PR created automatically by Jules for task [3966413529771698294](https://jules.google.com/task/3966413529771698294) started by @arii*
title:	Create Reusable Dashboard Widget Component Library
state:	OPEN
author:	google-labs-jules
labels:	
comments:	1
assignees:	
projects:	
milestone:	
number:	700
--
This change introduces a reusable dashboard widget component library to ensure a consistent look and feel for displaying various pieces of information. It includes a generic `DashboardWidget` and a specialized `DataWidget` for displaying data with a label and unit. An example has been added to the main dashboard to demonstrate its usage.

Fixes #545

---
*PR created automatically by Jules for task [17838956238623354812](https://jules.google.com/task/17838956238623354812) started by @arii*
title:	Add Start/Stop Workout button and timer display
state:	OPEN
author:	google-labs-jules
labels:	
comments:	1
assignees:	
projects:	
milestone:	
number:	697
--
This change adds a new UI component, `WorkoutControls`, to the main dashboard. This component provides 'Start Workout' and 'Stop Workout' buttons and displays a running timer in MM:SS format. The component's state is managed locally and synchronized with the WebSocket server.

Fixes #660

---
*PR created automatically by Jules for task [11291284855433181111](https://jules.google.com/task/11291284855433181111) started by @arii*
title:	Apply Quick UI Fixes
state:	OPEN
author:	google-labs-jules
labels:	
comments:	1
assignees:	
projects:	
milestone:	
number:	695
--
This submission applies a series of quick UI fixes as requested, including background gradients, card depth, improved button styles, larger touch targets, and a connection status glow. All changes have been visually verified.

Fixes #673

---
*PR created automatically by Jules for task [10495086296896309504](https://jules.google.com/task/10495086296896309504) started by @arii*
title:	Enhance Data Visualization with Gradients and Typography
state:	OPEN
author:	google-labs-jules
labels:	
comments:	1
assignees:	
projects:	
milestone:	
number:	688
--
This commit introduces several visual enhancements to improve data readability and visual appeal at a distance, including updating the HR_ZONES constant, increasing the TimerDisplay font size, and applying a gradient text effect to the HrTile percentage display. It also fixes a build error by adding missing props to the `HrTile` component.

---
*PR created automatically by Jules for task [1476443866703477942](https://jules.google.com/task/1476443866703477942) started by @arii*
