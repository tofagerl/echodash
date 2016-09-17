if [ -f .env ]; then
  source .env
fi
COOKIE=${COOKIE:-yourcookie}
CSRF=${CSRF:-yourcsrftoken}
SERIAL=${SERIAL:-yourserial}
MAC=${MAC:-yourmacaddress}
DEVICE=${DEVICE:-yourdeviceId}
$(which python) server.py
