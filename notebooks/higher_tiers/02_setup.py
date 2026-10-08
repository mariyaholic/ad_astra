# Mount and execute only the reviewed, pinned repository. Typical setup: a few minutes.
import os
import shutil
import subprocess
import sys
from pathlib import Path
if (shutil.which('nvidia-smi') and subprocess.run(['nvidia-smi'], capture_output=True).returncode == 0) or os.environ.get('COLAB_TPU_ADDR'):
    raise RuntimeError('Switch to a CPU runtime; this workload does not need a GPU/TPU')
try:
    from google.colab import drive
except ImportError as exc:
    raise RuntimeError('This setup cell requires Google Colab; local fixture tests use the embedded workflow cell') from exc
print('Mounting Drive; authorize through Colab, not through notebook source.', flush=True)
drive.mount('/content/drive')
CYGNUS_ROOT = Path('/content/drive/MyDrive/Cygnus')
if not CYGNUS_ROOT.is_dir():
    raise FileNotFoundError('BLOCK: Cygnus/ is not visible in the mounted Drive. Fix the mount; nothing outside it is read.')
REPO_DIR = Path('/content/cygnus_stage_two')
if not (REPO_DIR / '.git').is_dir():
    subprocess.run(['git', 'clone', '--quiet', 'https://github.com/mariyaholic/ad_astra', str(REPO_DIR)], check=True)
else:
    subprocess.run(['git', '-C', str(REPO_DIR), 'fetch', '--quiet', 'origin'], check=True)
subprocess.run(['git', '-C', str(REPO_DIR), 'checkout', '--quiet', '--detach', PINNED_COMMIT], check=True)
ACTUAL_HEAD = subprocess.run(['git', '-C', str(REPO_DIR), 'rev-parse', 'HEAD'], capture_output=True, text=True, check=True).stdout.strip()
if ACTUAL_HEAD != PINNED_COMMIT:
    raise RuntimeError('Pinned checkout mismatch')
print('Installing the pinned science tools, then running their targeted offline gate.', flush=True)
subprocess.run([sys.executable, '-m', 'pip', 'install', '--quiet', '-e', str(REPO_DIR) + '[test,campaign]'], check=True)
sys.path.insert(0, str(REPO_DIR / 'src'))
subprocess.run([sys.executable, '-m', 'pytest', '-q', 'tests/test_native_lead_tools.py', 'tests/test_skyrecord.py', 'tests/test_campaign.py'], cwd=str(REPO_DIR), check=True)
SCRATCH = Path('/content/cygnus_stage_two_scratch')
SCRATCH.mkdir(exist_ok=True)
os.environ['CYGNUS_SCRATCH'] = str(SCRATCH)
os.environ['CYGNUS_RATE_S'] = '0.5'
print('Pinned tools ready:', ACTUAL_HEAD, '| scratch is on the VM, never the Drive mount')
