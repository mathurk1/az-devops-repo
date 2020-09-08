from src.join_data.join_frames import join_frames
from loguru import logger

import pandas as pd
import numpy as np


def test_join_frames():
    """test join frames"""

    d1 = {"col1": [1, 2], "col2": [3, 4]}
    inp_a_df = pd.DataFrame(data=d1)

    print("hello there")

    d2 = {"col1": [1, 8], "col2": [7, 6]}
    inp_b_df = pd.DataFrame(data=d2)

    expected_data = {"col1": [1,2,8],
                     "col2_x": [3.0, 4.0, np.nan],
                     "col2_y": [7.0, np.nan, 6.0]}
    expected_df = pd.DataFrame(data=expected_data)

    result_df = join_frames(inp_a_df, inp_b_df)

    pd._testing.assert_frame_equal(expected_df, result_df)




