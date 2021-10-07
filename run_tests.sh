#!/bin/sh
pytest --cov=app --cov-report=xml    # individu al lines don't need to end with ;
err=$?

if [ "$err" -ne 5 ] && [ "$err" -ne 0 ]; then
  exit "$err"
fi
flake8
