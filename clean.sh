#!/usr/bin/env bash

ps aux | grep -v grep | grep 'kafka.Kafka\|QuorumPeerMain' | awk '{print $2}' | xargs kill -9
rm -rf /tmp/kafka-logs /tmp/zookeeper

