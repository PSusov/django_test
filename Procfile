#heroku config:set DISABLE_COLLECSTATIC=1
#heroku ps:scale web=1
web: gunicorn stat_tst.wsgi --log-file -
#web: python manage.py runserver 0.0.0.0
#web: bundle exec rails server -p 8000