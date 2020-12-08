import pytest
from handheld_halting import (execute_boot_code, fix_boot_code,
                              does_boot_code_complete)


@pytest.fixture
def boot_code():
    return ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99',
            'acc +1', 'jmp -4', 'acc +6']


def test_execute_boot_code(boot_code):
    assert execute_boot_code(boot_code) == 5


def test_does_boot_code_complete(boot_code):
    assert does_boot_code_complete(boot_code) == (False, 5)


def test_fix_boot_code(boot_code):
    assert fix_boot_code(boot_code) == 8
