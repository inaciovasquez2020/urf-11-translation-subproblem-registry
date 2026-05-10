import subprocess
import sys

def test_urf11_source_of_truth_and_overclaim_verifier():
    subprocess.run(
        [sys.executable, "tools/verify_urf11_source_of_truth_and_overclaims.py"],
        check=True,
    )
