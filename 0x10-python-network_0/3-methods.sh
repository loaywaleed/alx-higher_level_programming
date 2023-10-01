#!/bin/bash
# Script that displays all http methods server can accept
curl -sI "$1" | grep 'Allow' | cut -d' ' -f2-
