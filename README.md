# echodash
This project is quite simple: Whenever the Dash button configured in environment variables is pressed, play or pause is sent to Amazon via a REST service, and whatever you were listening to last restarts, or pauses. 
## Setup
You're going to need some information to get this running. 
* A login cookie from alexa.amazon.com in the variable `COOKIE`
* Your device ID in the variable `DEVICE`
* Your device serial in the variable  `SERIAL`
* The MAC address of your Dash button in the variable `MAC`

The first three should be easy to find. Install [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) for Chrome, go to [Amazon's Alexa SPA](https://alexa.amazon.com), login and capture a few commands with Postman. (You might need the standalone version of Postman to capture the cookie, but there are other ways of getting that cookie. Google it.)

The MAC address of your Dash is a little more complicated, but (https://medium.com/@edwardbenson/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8#.y2pjafhf2)[this article] by (https://medium.com/@edwardbenson)[Ted Benson] should be enough to get you started.

### sudo
You might need to run the script as root in order to get the privileges necessary to intercept ARP probes. Fair warning: this is dumb, and the reason I want to run the server in Docker ASAP!

## Docker
The Dockerfile does not currently work. It runs the script, but does not detect any ARP probes. This is probably not a networking issue, but rather an issue with the library I’m using to detect them. I will try switching to Scapy when I get the chance. 
