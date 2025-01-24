# Pyarmor 9.0.6 (trial), 000000, 2024-12-06T12:19:52.804699
import sys
import os

# Add the path to the directory containing pyarmor_runtime_000000 to sys.path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'pyarmor_runtime_000000'))

from .pyarmor_runtime import __pyarmor__
