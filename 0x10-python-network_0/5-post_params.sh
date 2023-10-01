#!/bin/bash
# Script that that posts two parameters
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
