
from subprocess import run, PIPE, STDOUT
from enum import IntEnum
from json import loads

class Status(IntEnum):
    OK = 0
    FATAL = 1
    ERROR = 2
    WARNING = 4
    REFACTOR = 8
    CONVENTION = 16
    USAGE = 32

def test_valid_fixture(message_id):
    cmd = f"pylint -f json fixtures/{message_id}/valid.py"
    res = run(cmd.split(), stdout=PIPE, stderr=STDOUT, text=True)
    assert res.returncode == 0

def test_invalid_fixture(message_id, code):
    cmd = f"pylint -f json fixtures/{message_id}/invalid.py"
    res = run(cmd.split(), stdout=PIPE, stderr=STDOUT, text=True)
    assert res.returncode == code
    for it in loads(res.stdout):
        assert it["message-id"] == message_id

if __name__ == "__main__":
    for message_id in ["E0101", "E1123"]:
        test_valid_fixture(message_id)
        test_invalid_fixture(message_id, Status.ERROR)
    for message_id in ["W0311", "W0702"]:
        test_valid_fixture(message_id)
        test_invalid_fixture(message_id, Status.WARNING)
    for message_id in ["R0123", "R0201"]:
        test_valid_fixture(message_id)
        test_invalid_fixture(message_id, Status.REFACTOR)
    for message_id in ["C0301", "C0328"]:
        test_valid_fixture(message_id)
        test_invalid_fixture(message_id, Status.CONVENTION)
