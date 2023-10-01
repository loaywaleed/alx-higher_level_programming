#!/bin/bash
# Script that that sends a get request with a header variable
curl -sH "X-School-User-Id: 98" GET "$1"
