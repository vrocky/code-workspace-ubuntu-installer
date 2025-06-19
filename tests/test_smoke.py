import subprocess
import sys
import tempfile
from pathlib import Path
import unittest
from installer.utils import state

class SmokeTest(unittest.TestCase):
    def test_cli_smoke(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / 'status.json'
            orig = state.STATE_PATH
            state.STATE_PATH = path
            try:
                result = subprocess.run(
                    [sys.executable, '-m', 'installer.cli', 'install', '--profile', 'test'],
                    capture_output=True,
                    text=True,
                    check=True,
                )
                self.assertIn('Installing profile test', result.stdout)
            finally:
                state.STATE_PATH = orig

if __name__ == '__main__':
    unittest.main()
