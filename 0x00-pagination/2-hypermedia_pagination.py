#!/usr/bin/env python3
""" 2. Hypermedia pagination """

from typing import Tuple, List
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return start and end index """
    start_index = 0
    end_index = page_size

    for i in range(1, page):
        start_index += page_size
        end_index += page_size

    return (start_index, end_index)


class Server:
    """ Server class to paginate a database of popular baby names. """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """ Init of the class """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Cached dataset """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ takes 2 integer page default 1 and page_size default 10. """
        assert type(page) is int and type(page_size) is int and\
            page > 0 and page_size > 0

        data = self.dataset()
        max_index = len(data)

        start_index, end_index = index_range(page, page_size)

        if start_index > max_index:
            return []

        if end_index > max_index:
            end_index = max_index

        paged_data = []
        for i in range(start_index, end_index):
            paged_data.append(data[i])

        return paged_data

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """ returns a dictionary containing the following key-value pairs """
        data = self.dataset()
        paged_data = self.get_page(page, page_size)
        current_page_size = len(paged_data)
        total_pages = math.ceil(len(data) / page_size)

        if (page < 2):
            prev_page = None
        else:
            prev_page = page - 1

        if (page >= total_pages):
            next_page = None
        else:
            next_page = page + 1

        return {
            "page_size": current_page_size,
            "page": page,
            "data": paged_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
