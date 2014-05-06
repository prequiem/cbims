#!/bin/bash
  set -e
  LOGFILE=/home/peter/Website/cbims/cbims/cbims.log
  LOGDIR=$(dirname $LOGFILE)
  NUM_WORKERS=2
  # user/group to run as
  USER=root
  GROUP=root
  cd /home/peter/Website/cbims/cbims/
  test -d $LOGDIR || mkdir -p $LOGDIR
  exec gunicorn_django -w $NUM_WORKERS -b 127.0.0.1:8080\
    --user=$USER --group=$GROUP --log-level=debug \
    --log-file=$LOGFILE 2>>$LOGFILE
