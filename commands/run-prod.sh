#!/bin/sh
uwsgi --module wsgi --http 0.0.0.0:8000 --enable-threads --thunder-lock --ignore-sigpipe --ignore-write-errors --disable-write-exception
