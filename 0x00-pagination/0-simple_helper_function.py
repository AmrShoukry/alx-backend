#!/usr/bin/env python3
""" 0. Simple helper function """

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return start and end index """
    start_index = 0
    end_index = page_size
    
    for i in range(1, page):
        start_index += page_size
        end_index += page_size

    return (start_index, end_index)