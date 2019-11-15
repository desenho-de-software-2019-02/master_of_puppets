#!/bin/bash
find . -name "*.py" | xargs perl -i -0pe 's/\n+\Z/\n/'