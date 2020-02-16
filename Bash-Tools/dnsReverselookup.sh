#!/bin/bash
echo "enter network id : "
$id 
read id
for ip in {1..254}; do dig -x $id.$ip | grep $ip > dns.txt; done;
