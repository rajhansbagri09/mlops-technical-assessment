import logging


def setup_logger(log_file):
    """
    Configure application logger.
    """

    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode="w"
    )

    return logging.getLogger(__name__)