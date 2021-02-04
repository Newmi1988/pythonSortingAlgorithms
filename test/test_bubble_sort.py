import pytest
from sortingalgorithms.bubble_sort import bubbleSort
import random


@pytest.fixture()
def random_list():
    return random.sample(list(range(100)),50)

def test_merge_sort(random_list):
    """Test bubble sort with a sampled list"""

    sorted_list = bubbleSort(random_list)

    next_is_bigger = [sorted_list[i]<sorted_list[i+1] for i in range(len(sorted_list)-1)]

    assert all(next_is_bigger) == True