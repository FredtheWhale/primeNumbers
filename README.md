# primeNumbers
This program will test, identify, and collect prime numbers using Python

I created this project because I was considering building a cluster computer with raspberry pis. I liked the idea of building the computer but didn't know what I would do with it once i was finished; so, i thought that I would test for prime numbers. (I'm not currently into bit coin mining).

I was going to build this in C but initially decided that I wanted to build it with functions. As I was writing it, the functions didn't make sense; so, I ended up writing it into a single program.

Please know that I am not a guru with Python. this program is fully functional and I've been running it for a couple days on a raspberry pi and on my windows computer ... i'm currently testing over 11 million without an issue. If you have code efficiencies, please feel free to update with a branch.

If you review the code, you will notice a lot of print statements that have been commented out. As i build the program, I used those print statements to tell me how far the program had progressed and they allowed me to troubleshoot. it seem useful to leave in the statements for future work.

Also, please note that I have an output file written into the code - it's currently set to post to your C:. if you're using a raspberry pi, you'll want to adjust that for the desktop. Part of the purpose of this file is that if you have to stop the program or restart the computer, the program will reference this file, load its contents into the list, and begin searching from the last number in the file ... therefore, you won't have to restart.


I hope you enjoy it.


PS, My next step with this program is to see what alterations are required for a cluster computer. If you have insight, I certainly appreciate your help.


