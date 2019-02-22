# Writeup 2 - OSINT

Name: Glenn Seidell
Section: 0101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Glenn Seidell

## Assignment Writeup

### Part 1 (45 pts)

1
Elizabeth Moffet
Found on Twitter with UserSearch from intelTechniques username tool

2
Job: Banking CEO @ http://1337bank.money
Found in twitter bio

3
Twitter: https://twitter.com/v0idcache
Reddit: https://www.reddit.com/user/v0idcache

4
from Mx toolbox:
IP address of 1337bank.money: 142.93.136.81
Server is running: Werkzeug/0.14.1 Python/3.7.2

from censys:
OS
Ubuntu
Network
DIGITALOCEAN-ASN - DigitalOcean, LLC (US)
Location : Amsterdam

5
Found on http://1337bank.money/secret_directory with help from robots.txt
Congrats! Flag is: CMSC389R-{h1ding_fil3s_in_r0bots_L0L}

6
from nmap 142.93.136.81:
22/tcp  open     ssh
80/tcp  open     http
135/tcp filtered msrpc
139/tcp filtered netbios-ssn	
445/tcp filtered microsoft-ds 
1337/tcp open     waste
11211/tcp filtered memcache

7
From Censys:
Ubuntu

8
From https://www.reddit.com/user/v0idcache/comments/atc1f7/x/
CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}

### Part 2 (75 pts)

Bruteforcing the server on port 1337 took a long time as script wasnt very fast. Guessing every password in rockyou.txt with v0idcache as the username was going to take a long time. I was going to try to optimise the script but then the server went down.

