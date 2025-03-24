#!/bin/bash
if ping -c 2 8.8.8.8;then
    exit 0
else
    ipaddr=""
    ipaddr=$(ip -4 addr show | grep inet | awk -F" " '{print $2}' | awk -F"/" '{print $1}' | grep -v '^127' -m 1 )
    脚本路径 "${ipaddr}"
fi