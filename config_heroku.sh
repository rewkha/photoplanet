#!/bin/bash

heroku config:set DJANGO_SETTINGS_MODULE=photoplanet.settings.heroku
heroku config:set INSTAGRAM_CLIENT_ID=87a6eb3c66da4a2db689921f96b5eb48
heroku config:set INSTAGRAM_CLIENT_SECRET=b27c2e5e99644be5a1f94720bab84d79
heroku config:set WEBSITE URL=http://rewkha-planet.herokuapp.com/