# Crypto II Writeup

Name: Glenn Seidell
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Glenn Seidell

## Assignment Writeup

### Part 1 (70 Pts)

gpg --decrypt message.txt.gpg 
gpg --import key.asc

This outputs the instructions for the next part as well as the flag.

CMSC389R-{m3ss@g3_!n_A_b0ttl3}

### Part 2 (30 Pts)

ECB is still has large recognizable shapes while CBC looks like pure noise. This is because ECB encrypts each block with the same key resulting in identical blocks being encrypted identically. This results in recognizable patterns in the output. CBC uses the output of the last block as the key for the next block resulting in each block being encrypted diffenently even if they have the same contents. This makes CBC more secure because there is no information to be gained from the encrypted picture.
