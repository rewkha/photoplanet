#!/bin/bash

heroku config:set DJANGO_SETTINGS_MODULE=photoplanet.settings.heroku
heroku config:set INSTAGRAM_CLIENT_ID=90ab5f87d9814062965778036e2e4572
heroku config:set INSTAGRAM_CLIENT_SECRET=5f24034ea61a4bddb0f10137b31e9793
heroku config:set WEBSITE URL=http://infinite-gorge-6776.herokuapp.com/