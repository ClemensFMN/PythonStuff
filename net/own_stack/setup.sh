#!/bin/bash


mknod /dev/net/tap c 10 200
ip tuntap add name tap mode tap
ip link set dev tap up
ip route add dev tap 10.0.0.0/24
ip address add dev tap local 10.0.0.5