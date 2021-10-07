#!/bin/sh
pytest --cov=app
err=$?

if [ "$err" -ne 5 ] && [ "$err" -ne 0 ]; then
  exit "$err"
fi
isort .
black .
# stop the build if there are Python syntax errors or undefined names
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
