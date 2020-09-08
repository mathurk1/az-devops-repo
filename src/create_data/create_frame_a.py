import pandas as pd


def create_frame_a():
    """This function will create 
    dataframe a

    Returns:
        df: dataframe a
    """

    d = {"col1": [1, 2], "col2": [3, 4]}
    df = pd.DataFrame(data=d)

    return df
