from app import hcf_lcm
import pytest
def test_hcf_lcm():
    expected_output = {
        "Hcf": 10,
        "lcm": 20
    }
    assert hcf_lcm(10, 20) == expected_output
def test_lcm():
    except_output={
        "Hcf":10,
        "lcm":60
    }
    assert hcf_lcm(20,30) ==except_output