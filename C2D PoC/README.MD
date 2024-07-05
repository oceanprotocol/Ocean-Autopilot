## Overview

In a racing environment, teams continuously collect and analyze data to make better decisions and outcompete their rivals. Most data collected is proprietary, and understandably, there is no incentive to share such information with other teams.

However, the nature of the race dictates that the winner is the team that outperforms the others, not necessarily the fastest one. Victory depends on being better compared to the competition.

This means that speed, downforce, and grip must always be evaluated in comparison to other teams. Whether the average speed of all teams is 200 km/h or 30 km/h, the goal remains to perform better than the rest. What matters more is not how fast you go, but how much faster you are than your competitors.

## Analytics in Racing 

During F1 race sessions, lap and sector times are usually the most used datapoints for benchmarking. These are publicly available datapoints that don't provide any insights into the specifics of the vehicle, and are generally used to understand the overall relative performance of a vehicle compared to other ones. 

This is what a general dashboard looks like:

![alt text](https://github.com/oceanprotocol/Ocean-Autopilot/blob/8d96fe28d3ce390cbdd1db73c0dc212f9498f9e0/C2D%20PoC/lap_times_aggregated_data_F1.png)


## Distributed Analytics in Racing

Analyses go beyond lap times data. There are over 250+ sensors installed on a vehicle and 1TB of data collected per vehicle per weekend, all which is extremely important to understand the performance relative to certain components.

Most of the data collected is kept private for internal analyses - this data includes but is not limited to suspension level/ride-height, fuel level, engine coolant temperatures, turbo temperatures, battery-pack temperatures, brake discs temperatures, brake pads temperatures, exhaust gas pressure, tyres pressure, engine oil pressure, gearbox oil pressure and down-force. 

So, just as benchmarking is commonly used for lap times where data is publicly shared across teams, so can benchmarking be used for private data such as the ones mentioned above to allow each team to analyze the performance of their components relative to the average progress of the entire league and eventually augment decision making and spur further innovation - all whilst keeping the data private and anonymized. 

This is what the architecture of distrubuted analytics look like using Ocean Nodes & Ocean's Compute-to-Data:

![alt text](https://github.com/oceanprotocol/Ocean-Autopilot/blob/3e17c53750ad828bb8e397a02728156b4230772f/C2D%20PoC/Distributed_Analytics.png)

This is what a Distributed Analytics Dashboard looks like:

