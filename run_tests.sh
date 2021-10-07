#!/bin/sh
pytest --cov=app
err=$?

if [ "$err" -ne 5 ] && [ "$err" -ne 0 ]; then
  exit "$err"
fi
flake8
