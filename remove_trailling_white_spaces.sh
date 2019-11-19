#!/bin/bash
ack --print0 -l '[ \t]+$' --type=python | xargs -0 -n1 perl -pi -e 's/[ \t]+$//'