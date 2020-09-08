from loguru import logger


def join_frames(a, b):
    """join the two frames"""

    c = a.merge(b, on=["col1"], how="outer")
    logger.info(f"after join : {c}")

    return c
