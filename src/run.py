from loguru import logger

from join_data.join_frames import join_frames
from create_data import create_frame_a, create_frame_b


def main():
    a = create_frame_a.create_frame_a()
    logger.info(f">> dataframe a is : {a}")

    b = create_frame_b.create_frame_b()
    logger.info(f">> dataframe b is : {b}")

    z = join_frames(a, b)
    logger.info(f"dataframe after join : {z}")


if __name__ == "__main__":
    main()