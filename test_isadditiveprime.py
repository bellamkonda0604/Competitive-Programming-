import os,sys
sys.path.append(os.getcwd())
from isadditiveprime import isadditiveprime
import pytest


@pytest.mark.parametrize('m, result',[
	(2, True), (3, True),
	(5, True), (13, False),
	(23, True), (29, True),
	(41, True), (98, False),
    (198, False), (290, False),
    (67, True), (97, False)
])
def test_ishappynumber(m, result):
    assert isadditiveprime(m) == result