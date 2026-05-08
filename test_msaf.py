# Simple MSAF example
from __future__ import print_function
from pathlib import Path
import sys
PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from src import msaf

# 1. Select audio file
audio_file = r"outputs\66CCFF\66CCFF.inst.mp3"

# 2. Segment the file using the default MSAF parameters (this might take a few seconds)
boundaries, labels = msaf.process(audio_file)
print('Estimated boundaries:', boundaries)

# 3. Save segments using the MIREX format
out_file = 'segments.txt'
print('Saving output to %s' % out_file)
msaf.io.write_mirex(boundaries, labels, out_file)
