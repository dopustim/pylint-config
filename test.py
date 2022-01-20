
import subprocess
import json

def test_valid_fixtures():
    res = subprocess.run("pylint -f json fixtures/*/valid.py",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=False)
    assert res.returncode == 0

def test_invalid_fixtures():
    res = subprocess.run("pylint -f json fixtures/*/invalid.py",
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, check=False)
    assert res.returncode != 0
    for it in json.loads(res.stdout):
        assert it["message-id"] in it["path"]

if __name__ == "__main__":
    test_valid_fixtures()
    test_invalid_fixtures()
