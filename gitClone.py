#!/usr/bin/env python3

import git
import os

cloneList = {
    "git@github.com:blurer/archinstall.git",
    "git@github.com:blurer/pinger.git",
    "git@github.com:blurer/Homelab-Setup.git",
    "git@github.com:blurer/homeserver.git",
    "git@github.com:blurer/Home-Temp-Monitoring.git",
    "git@github.com:blurer/pyToDo.git",
    "git@github.com:blurer/sytems.git",
    "git@github.com:blurer/sake.git",
    "git@github.com:blurer/cryptoprice.dev.git",
    "git@github.com:blurer/terraform.git",
    "git@github.com:blurer/vpn-docker-dns.git",
    "git@github.com:blurer/cloud-resume.git",
    "git@github.com:blurer/Cisco-Automation.git",
    "git@github.com:blurer/root-startpage.git",
    "git@github.com:blurer/netools.git",
    "git@github.com:blurer/newAnfang.git",
    "git@github.com:blurer/netDevEng.git",
    "git@github.com:blurer/netlify-bryanlurer.git",
    "git@github.com:blurer/subnet-calc.git",
    "git@github.com:blurer/ubuntu-first-boot.git",
    "git@github.com:blurer/flask-webapp.git",
    "git@github.com:blurer/pinger.git",
    "git@github.com:blurer/time-n-temp.git",
    "git@github.com:blurer/pssh.git",
    "git@github.com:blurer/iperf-notes.git",
    "git@github.com:blurer/misc.git",
    "git@github.com:blurer/ip-tools.git",
    "git@github.com:blurer/bl-tools.git"
}

for x in cloneList:
    try:
        git.Git("/$HOME/dev/").clone(x)
        print('Cloned ',x)
    except:
        pass
        print('Ignored ',x)
        
        
