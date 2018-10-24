#!/usr/bin/env bash

echo "zookeeper:"
ps aux | grep -v grep | grep 'QuorumPeerMain' | awk '{print $2}'

echo "kafka:"
ps aux | grep -v grep | grep 'kafka.Kafka' | awk '{print $2}'