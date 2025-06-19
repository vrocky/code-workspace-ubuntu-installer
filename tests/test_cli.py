import unittest
import tempfile
from pathlib import Path
from installer import cli
from installer.utils import state
import io
from contextlib import redirect_stdout

class CLITest(unittest.TestCase):
    def test_install_and_status(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / 'status.json'
            orig = state.STATE_PATH
            state.STATE_PATH = path
            try:
                out = io.StringIO()
                with redirect_stdout(out):
                    cli.main(['install', '--profile', 'full'])
                self.assertIn('Installing profile full', out.getvalue())
                status = state.load_state()
                self.assertEqual(status.get('last_profile'), 'full')

                out = io.StringIO()
                with redirect_stdout(out):
                    cli.main(['status'])
                self.assertIn('last_profile', out.getvalue())
            finally:
                state.STATE_PATH = orig

if __name__ == '__main__':
    unittest.main()
