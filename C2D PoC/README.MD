## Overview

In a racing environment, teams continuously collect and analyze data to make better decisions and outcompete their rivals. Most data collected is proprietary, and understandably, there is no incentive to share such information with other teams.

However, the nature of the race dictates that the winner is the team that outperforms the others, not necessarily the fastest one. Victory depends on being better compared to the competition.

This means that speed, downforce, and grip must always be evaluated in comparison to other teams. Whether the average speed of all teams is 200 km/h or 30 km/h, the goal remains to perform better than the rest. What matters more is not how fast you go, but how much faster you are than your competitors.

## Analytics in Racing 

During F1 race sessions, lap and sector times are usually the most used datapoints for benchmarking. These are publicly available datapoints that don't provide any insights into the specifics of the vehicle, and are generally used to understand the overall relative performance of a vehicle compared to other ones. 

This is what a general dashboard looks like:



## Distributed Analytics in Racing

Going beyond lap times data, and analyzing data coming from all the sensors installed on a vehicle (hundreds of sensors per car) is extremely important to understand the performance relative to certain areas.  

And that's where understanding a team's progress relative to other teams can help answer questions like "Are we working on the right components?" or "Are we improving this metric enough to outperform the others?" 

Just as benchmarking is used for lap times, where the data is made publicly available, so can benchmarking be used for private data such as aerodynamics, downforce, GPU and more - with the exception that the data remains private and anonymous.

This is where accessing more analytics —and particularly the aggregated means of all teams' private data— becomes valuable, and allows each team to analyze their performance relative to the average progress of the entire league.

This is what the architecture of distrubuted analytics look like using Ocean Nodes & Ocean's Compute-to-Data:

![alt text](https://github.com/oceanprotocol/Ocean-Autopilot/blob/3e17c53750ad828bb8e397a02728156b4230772f/C2D%20PoC/Distributed_Analytics.png)

This is what a Distributed Analytics Dashboard looks like:

