#!/bin/bash
# Script that that posts two parameters
curl -sX "email: test@gmail.com&subject=I will always be here for PLD" POST "$1"
