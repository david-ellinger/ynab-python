#!/bin/sh
pytest    # individual lines don't need to end with ;
err=$?

if [ "$err" -ne 5 ] && [ "$err" -ne 0 ]; then
  exit "$err"
fi
flake8
