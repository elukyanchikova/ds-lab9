# ds-lab9
## 1st instance
rs.status()
```json
MongoDB shell version v4.2.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("6f477ad7-cc58-47ad-900a-7484046a2a11") }
MongoDB server version: 4.2.1
{
        "set" : "lab9",
        "date" : ISODate("2019-10-31T15:13:32.725Z"),
        "myState" : 1,
        "term" : NumberLong(1),
        "syncingTo" : "",
        "syncSourceHost" : "",
        "syncSourceId" : -1,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572534812, 1),
                        "t" : NumberLong(1)
                },
                "lastCommittedWallTime" : ISODate("2019-10-31T15:13:32.661Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572534812, 1),
                        "t" : NumberLong(1)
                },
                "readConcernMajorityWallTime" : ISODate("2019-10-31T15:13:32.661Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572534812, 1),
                        "t" : NumberLong(1)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572534812, 1),
                        "t" : NumberLong(1)
                },
                "lastAppliedWallTime" : ISODate("2019-10-31T15:13:32.661Z"),
                "lastDurableWallTime" : ISODate("2019-10-31T15:13:32.661Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572534792, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572534792, 1),
        "electionCandidateMetrics" : {
                "lastElectionReason" : "electionTimeout",
                "lastElectionDate" : ISODate("2019-10-31T15:03:11.940Z"),
                "termAtElection" : NumberLong(1),
                "lastCommittedOpTimeAtElection" : {
                        "ts" : Timestamp(0, 0),
                        "t" : NumberLong(-1)
                },
                "lastSeenOpTimeAtElection" : {
                        "ts" : Timestamp(1572534181, 1),
                        "t" : NumberLong(-1)
                },
                "numVotesNeeded" : 2,
                "priorityAtElection" : 1,
                "electionTimeoutMillis" : NumberLong(10000),
                "numCatchUpOps" : NumberLong(27017),
                "newTermStartDate" : ISODate("2019-10-31T15:03:12.642Z"),
                "wMajorityWriteAvailabilityDate" : ISODate("2019-10-31T15:03:13.536Z")
        },
        "members" : [
                {
                        "_id" : 0,
                        "name" : "mongo1:27017",
                        "ip" : "172.31.33.59",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 1272,
                        "optime" : {
                                "ts" : Timestamp(1572534812, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-10-31T15:13:32Z"),
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572534191, 1),
                        "electionDate" : ISODate("2019-10-31T15:03:11Z"),
                        "configVersion" : 1,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 1,
                        "name" : "mongo2:27017",
                        "ip" : "172.31.31.136",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 631,
                        "optime" : {
                                "ts" : Timestamp(1572534802, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572534802, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-10-31T15:13:22Z"),
                        "optimeDurableDate" : ISODate("2019-10-31T15:13:22Z"),
                        "lastHeartbeat" : ISODate("2019-10-31T15:13:32.575Z"),
                        "lastHeartbeatRecv" : ISODate("2019-10-31T15:13:32.204Z"),
                        "pingMs" : NumberLong(2),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "mongo1:27017",
                        "syncSourceHost" : "mongo1:27017",
                        "syncSourceId" : 0,
                        "infoMessage" : "",
                        "configVersion" : 1
                },
                {
                        "_id" : 2,
                        "name" : "mongo3:27017",
                        "ip" : "172.31.45.28",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 631,
                        "optime" : {
                                "ts" : Timestamp(1572534802, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572534802, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-10-31T15:13:22Z"),
                        "optimeDurableDate" : ISODate("2019-10-31T15:13:22Z"),
                        "lastHeartbeat" : ISODate("2019-10-31T15:13:32.232Z"),
                        "lastHeartbeatRecv" : ISODate("2019-10-31T15:13:31.777Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "mongo1:27017",
                        "syncSourceHost" : "mongo1:27017",
                        "syncSourceId" : 0,
                        "infoMessage" : "",
                        "configVersion" : 1
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572534812, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572534812, 1)
}
```
rs.config()
```json
MongoDB shell version v4.2.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("b2736d94-2c22-4b83-ace6-29ec20285c11") }
MongoDB server version: 4.2.1
{
        "_id" : "lab9",
        "version" : 1,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "mongo1:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "mongo2:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "mongo3:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5dbaf7a54e838a355a78fa5f")
        }
}
```
## 2nd intance

rs.status()
```json
MongoDB shell version v4.2.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("67bb096a-20e1-4724-ba10-c72b6fa13c3c") }
MongoDB server version: 4.2.1
{
        "set" : "lab9",
        "date" : ISODate("2019-10-31T15:42:09.635Z"),
        "myState" : 1,
        "term" : NumberLong(2),
        "syncingTo" : "",
        "syncSourceHost" : "",
        "syncSourceId" : -1,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572536527, 1),
                        "t" : NumberLong(2)
                },
                "lastCommittedWallTime" : ISODate("2019-10-31T15:42:07.723Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572536527, 1),
                        "t" : NumberLong(2)
                },
                "readConcernMajorityWallTime" : ISODate("2019-10-31T15:42:07.723Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572536527, 1),
                        "t" : NumberLong(2)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572536527, 1),
                        "t" : NumberLong(2)
                },
                "lastAppliedWallTime" : ISODate("2019-10-31T15:42:07.723Z"),
                "lastDurableWallTime" : ISODate("2019-10-31T15:42:07.723Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572536459, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572536459, 1),
        "electionCandidateMetrics" : {
                "lastElectionReason" : "stepUpRequestSkipDryRun",
                "lastElectionDate" : ISODate("2019-10-31T15:24:36.872Z"),
                "termAtElection" : NumberLong(2),
                "lastCommittedOpTimeAtElection" : {
                        "ts" : Timestamp(1572535472, 1),
                        "t" : NumberLong(1)
                },
                "lastSeenOpTimeAtElection" : {
                        "ts" : Timestamp(1572535472, 1),
                        "t" : NumberLong(1)
                },
                "numVotesNeeded" : 2,
                "priorityAtElection" : 1,
                "electionTimeoutMillis" : NumberLong(10000),
                "priorPrimaryMemberId" : 0,
                "numCatchUpOps" : NumberLong(27017),
                "newTermStartDate" : ISODate("2019-10-31T15:24:37.693Z"),
                "wMajorityWriteAvailabilityDate" : ISODate("2019-10-31T15:24:38.714Z")
        },
        "members" : [
                {
                        "_id" : 0,
                        "name" : "mongo1:27017",
                        "ip" : "172.31.33.59",
                        "health" : 0,
                        "state" : 8,
                        "stateStr" : "(not reachable/healthy)",
                        "uptime" : 0,
                        "optime" : {
                                "ts" : Timestamp(0, 0),
                                "t" : NumberLong(-1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(0, 0),
                                "t" : NumberLong(-1)
                        },
                        "optimeDate" : ISODate("1970-01-01T00:00:00Z"),
                        "optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
                        "lastHeartbeat" : ISODate("2019-10-31T15:41:59.488Z"),
                        "lastHeartbeatRecv" : ISODate("2019-10-31T15:35:10.139Z"),
                        "pingMs" : NumberLong(1),
                        "lastHeartbeatMessage" : "Couldn't get a connection within the time limit",
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "configVersion" : -1
                },
                {
                        "_id" : 1,
                        "name" : "mongo2:27017",
                        "ip" : "172.31.31.136",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 2992,
                        "optime" : {
                                "ts" : Timestamp(1572536527, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-10-31T15:42:07Z"),
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572535476, 1),
                        "electionDate" : ISODate("2019-10-31T15:24:36Z"),
                        "configVersion" : 1,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                },
                {
                        "_id" : 2,
                        "name" : "mongo3:27017",
                        "ip" : "172.31.45.28",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 2347,
                        "optime" : {
                                "ts" : Timestamp(1572536527, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572536527, 1),
                                "t" : NumberLong(2)
                        },
                        "optimeDate" : ISODate("2019-10-31T15:42:07Z"),
                        "optimeDurableDate" : ISODate("2019-10-31T15:42:07Z"),
                        "lastHeartbeat" : ISODate("2019-10-31T15:42:07.959Z"),
                        "lastHeartbeatRecv" : ISODate("2019-10-31T15:42:07.797Z"),
                        "pingMs" : NumberLong(2),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "mongo2:27017",
                        "syncSourceHost" : "mongo2:27017",
                        "syncSourceId" : 1,
                        "infoMessage" : "",
                        "configVersion" : 1
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572536527, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572536527, 1)
}
```
rs.config()
```json
MongoDB shell version v4.2.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("fb6ef19d-4a94-4879-9cfd-3c0458baa3d3") }
MongoDB server version: 4.2.1
{
        "_id" : "lab9",
        "version" : 1,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
                {
                        "_id" : 0,
                        "host" : "mongo1:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 1,
                        "host" : "mongo2:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                },
                {
                        "_id" : 2,
                        "host" : "mongo3:27017",
                        "arbiterOnly" : false,
                        "buildIndexes" : true,
                        "hidden" : false,
                        "priority" : 1,
                        "tags" : {

                        },
                        "slaveDelay" : NumberLong(0),
                        "votes" : 1
                }
        ],
        "settings" : {
                "chainingAllowed" : true,
                "heartbeatIntervalMillis" : 2000,
                "heartbeatTimeoutSecs" : 10,
                "electionTimeoutMillis" : 10000,
                "catchUpTimeoutMillis" : -1,
                "catchUpTakeoverDelayMillis" : 30000,
                "getLastErrorModes" : {

                },
                "getLastErrorDefaults" : {
                        "w" : 1,
                        "wtimeout" : 0
                },
                "replicaSetId" : ObjectId("5dbaf7a54e838a355a78fa5f")
        }
}
```
## 3rd instance

rs.status()
```json
MongoDB shell version v4.2.1
connecting to: mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("bc20d082-4deb-4486-86c2-c69680c37cfa") }
MongoDB server version: 4.2.1
{
        "set" : "lab9",
        "date" : ISODate("2019-10-31T15:19:17.886Z"),
        "myState" : 2,
        "term" : NumberLong(1),
        "syncingTo" : "mongo1:27017",
        "syncSourceHost" : "mongo1:27017",
        "syncSourceId" : 0,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
                "lastCommittedOpTime" : {
                        "ts" : Timestamp(1572535152, 1),
                        "t" : NumberLong(1)
                },
                "lastCommittedWallTime" : ISODate("2019-10-31T15:19:12.672Z"),
                "readConcernMajorityOpTime" : {
                        "ts" : Timestamp(1572535152, 1),
                        "t" : NumberLong(1)
                },
                "readConcernMajorityWallTime" : ISODate("2019-10-31T15:19:12.672Z"),
                "appliedOpTime" : {
                        "ts" : Timestamp(1572535152, 1),
                        "t" : NumberLong(1)
                },
                "durableOpTime" : {
                        "ts" : Timestamp(1572535152, 1),
                        "t" : NumberLong(1)
                },
                "lastAppliedWallTime" : ISODate("2019-10-31T15:19:12.672Z"),
                "lastDurableWallTime" : ISODate("2019-10-31T15:19:12.672Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572535152, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572535152, 1),
        "members" : [
                {
                        "_id" : 0,
                        "name" : "mongo1:27017",
                        "ip" : "172.31.33.59",
                        "health" : 1,
                        "state" : 1,
                        "stateStr" : "PRIMARY",
                        "uptime" : 975,
                        "optime" : {
                                "ts" : Timestamp(1572535152, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572535152, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-10-31T15:19:12Z"),
                        "optimeDurableDate" : ISODate("2019-10-31T15:19:12Z"),
                        "lastHeartbeat" : ISODate("2019-10-31T15:19:15.920Z"),
                        "lastHeartbeatRecv" : ISODate("2019-10-31T15:19:16.385Z"),
                        "pingMs" : NumberLong(0),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "",
                        "syncSourceHost" : "",
                        "syncSourceId" : -1,
                        "infoMessage" : "",
                        "electionTime" : Timestamp(1572534191, 1),
                        "electionDate" : ISODate("2019-10-31T15:03:11Z"),
                        "configVersion" : 1
                },
                {
                        "_id" : 1,
                        "name" : "mongo2:27017",
                        "ip" : "172.31.31.136",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 975,
                        "optime" : {
                                "ts" : Timestamp(1572535152, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDurable" : {
                                "ts" : Timestamp(1572535152, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-10-31T15:19:12Z"),
                        "optimeDurableDate" : ISODate("2019-10-31T15:19:12Z"),
                        "lastHeartbeat" : ISODate("2019-10-31T15:19:16.526Z"),
                        "lastHeartbeatRecv" : ISODate("2019-10-31T15:19:16.595Z"),
                        "pingMs" : NumberLong(2),
                        "lastHeartbeatMessage" : "",
                        "syncingTo" : "mongo1:27017",
                        "syncSourceHost" : "mongo1:27017",
                        "syncSourceId" : 0,
                        "infoMessage" : "",
                        "configVersion" : 1
                },
                {
                        "_id" : 2,
                        "name" : "mongo3:27017",
                        "ip" : "172.31.45.28",
                        "health" : 1,
                        "state" : 2,
                        "stateStr" : "SECONDARY",
                        "uptime" : 1608,
                        "optime" : {
                                "ts" : Timestamp(1572535152, 1),
                                "t" : NumberLong(1)
                        },
                        "optimeDate" : ISODate("2019-10-31T15:19:12Z"),
                        "syncingTo" : "mongo1:27017",
                        "syncSourceHost" : "mongo1:27017",
                        "syncSourceId" : 0,
                        "infoMessage" : "",
                        "configVersion" : 1,
                        "self" : true,
                        "lastHeartbeatMessage" : ""
                }
        ],
        "ok" : 1,
        "$clusterTime" : {
                "clusterTime" : Timestamp(1572535152, 1),
                "signature" : {
                        "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                        "keyId" : NumberLong(0)
                }
        },
        "operationTime" : Timestamp(1572535152, 1)
}
```
