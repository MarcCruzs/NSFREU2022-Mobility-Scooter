
****Traveling Router Info : "GL-AR300M-eea-NOR"****

****Password: "goodlife"****

****Software to access the two Rasberry Pi: "VNC Viewer"****

For us to collect data of the gyroscope and accelerometer from the raspberry pi + sensehat the only way we can connect is to use a remote-controlled desktop software so that we can access in real-time to check if the code is running, collecting data and modify the code all at the same time, but it needs a common access point or common network that allow each system to show their IP address. The travelling router makes this stuff easy by allowing us to connect the two raspberry pi without any ethernet cable or any traces of bandwidths, plus factor is that from us we can connect to this router for almost 75 meters - 100 meters. 
	
## Quick tutorial to VNC Viewer ##

Download the VNC Viewer and register for an account, once login insert the IP address. If you guys started with a new raspberry pi, please modify the bios system that would enable the VNC viewer. For one to access the bios system of raspberry pi you need to open the terminal and type "-sudo su" and them type "raspiconfig" when you're in the bios system go directly to VNC viewer options.  If those command lines doesn't work please watch this tutorial (Link).

## This below things need to connect to router's wifi on that very top is the info connect ##
_Raspberry Pi B: 192.168.8.150_
_Raspberry Pi A: 192.168.8.237_
Your laptop or phone that has the remote controlled desktop software to connect to those IP address

## Failed Attempts ##

We tried our attempts on using the "Eduroam" and "CPPGuest" as our common network/accesspoint but this doesn't allow us to use the remote-controlled desktop software due to IT protocols in the campus. Stacking on that problem this doesn't allow us to show IP address. We tried contacting the IT department and creating a ticket on their upper management and labeled it as a "high priority" but this takes alot of time that can be used in data collection. More likely they will not give us a green light to use any of this stuff.
We used a hotspot as an alternative for router this created complication on the data collection, firstly hotspot aren't stable hence can't be trusted to be "on" all the time and it the phone who started the hotspot needs to be near the two raspberry pi and to see the if those two are running you need to have either a phone or laptop to view them as near as possible to the hotspot. This attempt challeged our physical capabilites to jog or run near the mobility scooter in long amount of time. 

## Future Work: ##

First of all please do not change the wifi's name that resembles to our association or anything that mentions this Research or any of your guys' name. They have protocol that doesn't allow one student to have a private router, this was mentioned to one of the emails that Dr.Chen's email that IT people have this kind of rules. Please check the IT protocols to see some loopholes.

I haven't tried this attempt due to my anxiety that it may trigger one of the IT protocols and to create things complicated for the future researchers, but I had a brute force/backdoor method to make the "Eduroam" as common network by replicating one of the computers around the CS lab and your system private IP address, you can copy those IP address and change those two  raspberry pi IP address to it. This will make some ease but we haven't see how stable "Eduroam" is in college campus ground and with the alot of people showing up in this upcoming semester.

Invest spare time on automation that sends out csv files in one cloud storage system or discord. Discord bot is one of the attempts I have doing but didn't got the time to it due to data processing and catching up the paper works in my research program.


https://docs.google.com/document/d/1hl65HeF4huXwYAs16MPh2f4Kte3bt-E79pvwCwHbuqg/edit?usp=sharing
