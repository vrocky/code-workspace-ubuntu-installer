import unittest
import tempfile
from pathlib import Path
from installer.utils import state

class StateModuleTest(unittest.TestCase):
    def test_save_and_load_state(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / 'status.json'
            orig = state.STATE_PATH
            state.STATE_PATH = path
            try:
                data = {'python': 'done'}
                state.save_state(data)
                self.assertTrue(path.exists())
                loaded = state.load_state()
                self.assertEqual(loaded, data)
            finally:
                state.STATE_PATH = orig

if __name__ == '__main__':
    unittest.main()
