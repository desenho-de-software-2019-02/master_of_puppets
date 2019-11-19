#!/bin/bash
find . -name "*.py" | xargs sed -i 'N;/^\n$/D;P;D;'