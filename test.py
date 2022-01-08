
from subprocess import run, PIPE, STDOUT
from json import loads

def test_valid_fixtures():
    cmd = f"python -m pylint -f json fixtures/*/valid.py"
    res = run(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    assert res.returncode == 0

def test_invalid_fixtures():
    cmd = f"pylint -f json fixtures/*/invalid.py"
    res = run(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    assert res.returncode != 0
    for it in loads(res.stdout):
        assert it["message-id"] in it["path"]

if __name__ == "__main__":
    test_valid_fixtures()
    test_invalid_fixtures()
