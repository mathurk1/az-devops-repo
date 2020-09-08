import pandas as pd


def create_frame_b():
    """This function will create 
    dataframe b

    Returns:
        df: dataframe b
    """

    d = {"col1": [1, 8], "col2": [7, 6]}
    df = pd.DataFrame(data=d)

    return df
