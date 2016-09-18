# echodash
This project is quite simple: Whenever the Dash button configured in environment variables is pressed, play or pause is sent to Amazon via a REST service, and whatever you were listening to last restarts, or pauses.

**Should be run in Docker**
## Setup
You're going to need some information to get this running.
* A login cookie from alexa.amazon.com in the variable `cookie`
* Your device ID in the variable `device`
* Your device serial in the variable  `serial`
* The MAC address of your Dash button in the variable `mac`
* The CSFR token in the variable `csfr`

The first three should be easy to find. Install [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en) for Chrome, go to [Amazon's Alexa SPA](https://alexa.amazon.com), login and capture a few commands with Postman. (You might need the standalone version of Postman to capture the cookie, but there are other ways of getting that cookie. Google it.)

The MAC address of your Dash is a little more complicated, but (https://medium.com/@edwardbenson/how-i-hacked-amazon-s-5-wifi-button-to-track-baby-data-794214b0bdd8#.y2pjafhf2)[this article] by (https://medium.com/@edwardbenson)[Ted Benson] should be enough to get you started.

**Put those variables in a file called config.py, and the rest should be automatic.**

### sudo
You might need to run the script as root in order to get the privileges necessary to intercept ARP probes. Fair warning: this is dumb, and the reason you really want to run this in Docker.

## Docker
The Dockerfile finally works, but does not as yet output anything to log. This is not something I consider a serious bug, but if you can fix it, I would love a pull request.
