#!/bin/bash

# https://ringzer0team.com/challenges/49
openssl rsautl -decrypt -in flag.enc -inkey private.pem
