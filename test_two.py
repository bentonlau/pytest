import pytest

@pytest.mark.golden_suite

class Node():
    def __init__(self,val=None):
        self.val = val
        self.nextnode = None

def test_node():
    new_node = Node()
    assert (new_node.val) == (None)