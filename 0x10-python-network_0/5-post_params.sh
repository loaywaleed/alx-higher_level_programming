#!/bin/bash
# Script that that posts two parameters
curl -sXd POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
