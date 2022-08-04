# Router info and Future works in Data Collection #

****Router Name : "GL-AR300M-eea-NOR"****

****Password: "goodlife"****

****Software to access the two Rasberry Pi: "VNC Viewer"****

For us to collect data of the gyroscope and accelerometer from the raspberry pi + sensehat
the way we can connect is to use a remote-controlled desktop software so that we can 
access in real-time of the raspberry pi desktops to check if the code is running, 
collecting data and to modify the code
all at the same time. But it needs a common access point or common network that allow 
each system to show their IP address. The wireless router makes this stuff easy by 
allowing us to connect the two raspberry pis without any ethernet cable, any traces 
of bandwidths, and will not need a portable monitor.\
**NOTE: Can be decently far from raspberry pis. Max distance is around 75 meters - 100 meters.**
## Quick tutorial to VNC Viewer ##

Download the [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/) and register for an account, once login insert the IP address. If you guys started with a new raspberry pi, please modify the bios system that would enable the VNC viewer. For one to access the bios system of raspberry pi you need to open the terminal and type "-sudo su" and them type "raspiconfig" when you're in the bios system go directly to VNC viewer options.  If those command lines doesn't work please watch this tutorial (https://youtu.be/IfzBPi4FHpI).

## Connecting Raspberry Pis to VNC Viewer
After connecting to the wireless router wifi, go to VNC viewer software on laptop or phone and type
in IP addresses:

_Raspberry Pi B: 192.168.8.150_\
_Raspberry Pi A: 192.168.8.237_

If these IP addresses do not work. Go to the command line and hostname -I and that should give
the address when connected to the router wifi.
**NOTE: Laptop can log into both raspberry pi desktops at the same time, while the phone can
only do it one at a time**

## Failed Attempts: ##

We tried our attempts on using the "Eduroam" and "CPPGuest" as our common 
network/accesspoint but this doesn't allow us to use the remote-controlled desktop 
software due to IT protocols in the campus. Stacking onto this problem, it doesn't 
allow us to show IP address. We tried contacting the IT department and creating a 
ticket on their upper management and labeled it as a "high priority" but this takes 
alot of time that can be used in data collection. More likely they will not give us a 
green light to use any of this stuff. (View Future Works. This can be resolved faster during
the semester)\

We used a hotspot as an alternative from the router. This created complications in the 
data collection, firstly hotspot aren't stable hence can't be trusted to be "on" 
all the time and if the phone who started the hotspot needs to be near the two 
raspberry pi and to see the if those two are running you need to have either a 
phone or laptop to view them to be connected and near the hotspot. This attempt challenged 
our physical capabilities to jog or run near the mobility scooter in long amount of time. 

## WARNING: Things to Keep in Mind ##

First of all please do not change the wifi's name that resembles to our association or anything that mentions this Research or any of your guys' name. They have protocol that doesn't allow one student to have a private router, this was mentioned to one of the emails that Dr.Chen's email that IT people have this kind of rules. Please check the IT protocols to see some loopholes.

I haven't tried this attempt due to my anxiety that it may trigger one of the IT protocols and to create things complicated for the future researchers, but I had a brute force/backdoor method to make the "Eduroam" as common network by replicating one of the computers around the CS lab and your system private IP address, you can copy those IP address and change those two  raspberry pi IP address to it. This will make some ease but we haven't see how stable "Eduroam" is in college campus ground and with the alot of people showing up in this upcoming semester.

Invest spare time on automation that sends out csv files in one cloud storage system or discord. Discord bot is one of the attempts I have doing but didn't got the time to it due to data processing and catching up the paper works in my research program.


https://docs.google.com/document/d/1hl65HeF4huXwYAs16MPh2f4Kte3bt-E79pvwCwHbuqg/edit?usp=sharing
