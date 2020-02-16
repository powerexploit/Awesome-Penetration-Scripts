#!/bin/bash
echo "Enter Class C Range: i.e. 192.168.1"
read range
for ip in {1..254..l};do host $range.$ip | grep "name pointer" | cut -d" " -fS;done
