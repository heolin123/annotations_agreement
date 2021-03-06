import numpy as np
import pytest
from agreement.utils.transform import pivot_table_frequency


@pytest.fixture
def dataset_gwet():
    """
    Rating data from 4 raters and 12 subjects.

    This dataset comes from Handbook of Inter-Rater ReLiability, Kilem Li. Gwet, 2014, p. 120

    Columns description:
    """
    return np.array([
        [1, 1, 'a'],
        [2, 1, 'b'],
        [3, 1, 'c'],
        [4, 1, 'c'],
        [5, 1, 'b'],
        [6, 1, 'a'],
        [7, 1, 'd'],
        [8, 1, 'a'],
        [9, 1, 'b'],
        [1, 2, 'a'],
        [2, 2, 'b'],
        [3, 2, 'c'],
        [4, 2, 'c'],
        [5, 2, 'b'],
        [6, 2, 'b'],
        [7, 2, 'd'],
        [8, 2, 'a'],
        [9, 2, 'b'],
        [10, 2, 'e'],
        [2, 3, 'c'],
        [3, 3, 'c'],
        [4, 3, 'c'],
        [5, 3, 'b'],
        [6, 3, 'c'],
        [7, 3, 'd'],
        [8, 3, 'b'],
        [9, 3, 'b'],
        [10, 3, 'e'],
        [11, 3, 'a'],
        [12, 3, 'c'],
        [1, 4, 'a'],
        [2, 4, 'b'],
        [3, 4, 'c'],
        [4, 4, 'c'],
        [5, 4, 'b'],
        [6, 4, 'd'],
        [7, 4, 'd'],
        [8, 4, 'a'],
        [9, 4, 'b'],
        [10, 4, 'e'],
        [11, 4, 'a']
    ], dtype=object)


@pytest.fixture
def dataset_gwet_transformed(dataset_gwet):
    dataset = dataset_gwet
    questions_answers_table = pivot_table_frequency(dataset[:, 0], dataset[:, 2])
    users_answers_table = pivot_table_frequency(dataset[:, 1], dataset[:, 2])
    return questions_answers_table, users_answers_table


@pytest.fixture
def dataset_unused_values():
    return np.array([
        [0,  1,  3],
        [0,  2,  3],
        [1,  1,  3],
        [1,  2,  3],
        [2,  1,  3],
        [2,  2,  3],
        [3,  1,  2],
        [3,  2,  3],
        [4,  1,  2],
        [4,  2,  2],
        [5,  1,  3],
        [5,  2,  3]
    ])


@pytest.fixture
def dataset_unused_values_transformed(dataset_unused_values):
    dataset = dataset_unused_values
    questions_answers_table = pivot_table_frequency(dataset[:, 0], dataset[:, 2])
    users_answers_table = pivot_table_frequency(dataset[:, 1], dataset[:, 2])
    return questions_answers_table, users_answers_table
