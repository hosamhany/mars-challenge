
# Points Distribution Table

For each one of the tasks completed your team will get points. These Points will
be added at the end of the Challenge. The team that has the most points will win
 the challenge:

- [Challenge Competition](#challenge-competition)
- [Points per Tier](#points-per-tier)
- [Bonus Points](#bonus-points)
- [DevOps Points](#devops)

## Challenge Competition

|####|Name|Tier|Description|Points|
|----|----|----|-----------|------|
|CC-1|Level Up!|CC|Build and deploy a solution that can compete against other teams in an Official Game| 30|
|CC-2|Challenge Champion|CC| Winning the official competition| 20|

## Points Per Tier

### Tier 1 Sensors Array:

|####|Name|Tier|Description|Points|
|----|----|----|-----------|------|
|T1-1 |Sensor Software Running in Raspberry|Tier 1|Get the SensorSuite program running in the Raspberry Pi|5|
|T1-2 |My Sensor Containers|Tier 1| Build a container for each sensor in the SensorSuite. Use these containers for the rest of the challenge|10|
|T1-3 |Bridge The Gap|Tier 1|Run your *Flare* container in your cloud VM, and configure your other sensors to reach it|5|

### Tier 2 The Aggregator:

|####|Name|Tier|Description|Points|
|----|----|----|-----------|------|
|T2-1|Start the Aggregator|Tier 2| Run the Aggregator in your cloud VM, show it received data from your SensorSuite|5|
|T2-2|Data smarts| Tier 2| Modify the Aggregator to send all the RAW sensor and AVG data to a storage repository|5|
|T2-3|My Gateway Container|Tier 2| Build a container for the Aggregator. Use this container for the rest of the challenge|5|

### Tier 3 Data Repository:

|####|Name|Tier|Description|Points|
|----|----|----|-----------|------|
|T3-1 |Data Hog 1|Tier 3|Store all Sensor Data from system|5|
|T3-2 |Data Hog 2|Tier 3|Store all Logs from system|5|
|T3-3 |The Black Box|Tier 3| Create a separate storage for data backups|5|
|T3-4 |REX-Ray|Tier 3|Use REX-ray to mount external storage volume for persistence|10|

### Tier 4 Data Analysis Tier

|####|Name|Tier|Description|Points|
|----|----|----|-----------|------|
|T4-1|Analytic Brain|Tier 4| Setup a node or a cluster of Hadoop/Spark/F#(or any language/tool of your choice) to analyze data. This tier will help you to better anticipate change.|15|
|T4-2|My Analytic Container|Tier 4| Build a container with the Data Analysis tier. Use this container for the rest of the challenge|5|

### Tier 5 Team Client and Control Tier

|#####|Name|Tier|Description|Points|
|----|----|----|-----------|------|
|T5-1|Command and Control|Tier 5| Implement a service that can retrieve data from the Gateway/Game Controller, join the game, and use the sensor data to take actions to protect the base|5|
|T5-2|My C&C Container|Tier 5| Build a container with the C&C tier. Use this container for the rest of the challenge|5|

### Tier 6 Data Backup

|#####|Name|Tier|Description|Points|
|----|----|----|-----------|------|
|T6-1|For the Ages|Tier 6|Build a Backup service that takes data and performs backups and stores them in Tier 3 Data repository. Can be combined with the "The Black Box" for added points|5|
|T6-2|My Backup Service Container |Tier 6| Build a container with the Data Backup service tier. Use this container for the rest of the challenge|5|
|T6-3 |REX-Ray|Tier 6|Use REX-ray to mount external storage volume for persistence|10|

## DevOps

|#####|Name|Tier|Description|Points|
|----|----|----|-----------|------|
|DO-1|Service Discovery|DO| Implement Service Discovery between all the containers deployed in the solution| 5|
|DO-2|Service Monitoring|DO| Implement Service Monitoring of all containers deployed in the solution| 5|
|DO-3|Service Configuration|DO| Implement Service configuration for all the Tiers/containers| 5|
|DO-4|Service Orchestration|DO| Implement Service Orchestration for all the Tiers/containers| 5|
|DO-5|Docker Me up!|DO| Deployment of the implemented system using Docker Tooling| 15|
|DO-6|Kubernetes Me up!|DO| Deployment of the implemented system using Kubernetes Tooling| 15|
|DO-8|Deploy Me up!|DO| Deployment of the implemented system using Puppet/Ansible/Chef/Saltstack or other Tooling| 10|
|DO-9|Logging Router|DO|Deploy, connect and route the logs of the application using a logging router|10|

## Bonus Points

|####|Name|Tier|Description|Points|
|----|----|----|-----------|------|
|BC-1|DevOps Power|BC| Deploy a CD/CI tool-chain, DevOps style, that includes Tiers 1-5 so your team can develop the algorithm to survive the event|20|
|BC-2|Limited Resources|BC| The team commits to only drink water for the entire challenge. It is Mars after all!|10|
|BC-3|The FOSS|BC| The team commits to share all the information about what you are doing. Free and open-source software works even in Space!|10|
|BC-4|Evil Genius|BC| The team commits to not sharing any information with anybody. You and your team are Evil Geniuses!|10|
