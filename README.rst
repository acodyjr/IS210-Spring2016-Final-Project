#####################
Bar|$plit
#####################

Bar|$plit is a program designed to make sure everyone pays their fair share during a group happy hour or group meal. 

Personas
========


Sarah the Soda Drinker
--------------------------------------------

Details
^^^^^^^

Enjoys spending time with friends and organizes group lunches and dinner, but is not a drinker or extravagant with her meal choices.

Goals
^^^^^^

Wants to avoid the inevitable suggestion of just splitting the bill based on number of group members, which causes Sarah to pay significantly more than she’s consumed. She enjoys the company of her friends but doesn’t want to foot the bill constantly.


Problem Scenario
=================

The bill arrives at the end of the night and one person is left in the dark with a pencil and the back of the receipt to try to make sense of each person’s responsibility and tip contribution.

Current Alternatives
------------------------------------

Taking the time to do the math with a pad and paper in the restaurant. The group can also request individual bills, but is usually required to do so at the start of the meal, and people often forget.

Value Proposition
----------------------------------

A quickly delivered result considering various tip amounts based on level of service.


User Stories
============

Sarah’s Story
----------------------------

As Sarah the Soda Drinker, I want to accurately calculate my portion of the total bill so that I can leave knowing I am not overspending my personal budgets especially on items that I did not order or consume.

Acceptance Stories
====================

| **Scenario 01: Calculating Individual Tabs**
| Given that I have a known number in a group,
| And that I have an itemized receipt,
| And that the members only want to pay for themselves,
| When I enter the number of members in the group
| Then I will be able to enter their item costs individually
| And the output will produce individual tabs factoring tip.
|
| **Scenario 02: Calculating Even-Split Tabs**
| Given that I have a known number in a group,
| And that we have the total amount due,
| And that the members wish to split the tab proportionally,
| When I enter the number of members in the group,
| Then I can select ``Split Evenly``
| And the output will evenly split the total tab and add tip.


Instructions
============

Installation
---------------------
No additional modules are needed outside of barsplit.py.

Using the Program
---------------------------------
Execute the program to initiate the series of prompts needed to complete the calculations. No external file is needed to import as all information is based on user input realtime. Follow the on-screen prompts to enter valid data and to determine the type of calculation desired.