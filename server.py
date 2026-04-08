#!/usr/bin/env python3
import os
import subprocess
import sys

port = os.environ.get('PORT', '8080')
subprocess.run([sys.executable, '-m', 'http.server', port])
