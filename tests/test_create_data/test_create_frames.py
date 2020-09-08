from src.create_data.create_frame_a import create_frame_a
from src.create_data.create_frame_b import create_frame_b

import pandas as pd


def test_create_frame_a():
    """test frame a"""

    d = {"col1": [1, 2], "col2": [3, 4]}
    expected_df = pd.DataFrame(data=d)

    actual_df = create_frame_a()

    pd._testing.assert_frame_equal(expected_df, actual_df)


def test_create_frame_b():
    """test frame b"""

    d = {"col1": [1, 8], "col2": [7, 6]}
    expected_df = pd.DataFrame(data=d)

    actual_df = create_frame_b()

    pd._testing.assert_frame_equal(expected_df, actual_df)