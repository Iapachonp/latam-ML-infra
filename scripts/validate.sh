#!/bin/bash
set -e
echo 'running black...'
black $CI_PROJECT_DIR --check
