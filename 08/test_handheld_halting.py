import pytest
from handheld_halting import execute_boot_code


@pytest.fixture
def boot_code():
    return ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99',
            'acc +1', 'jmp -4', 'acc +6']


def test_execute_boot_code(boot_code):
    assert execute_boot_code(boot_code) == 5
