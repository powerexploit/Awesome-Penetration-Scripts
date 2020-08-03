#!/bin/bash
if [ $1 ];then ping $1 | grep 64;else echo usage : pingscanner.sh 192.168.0.x;fi
