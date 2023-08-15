import logging
#You can use to add logs, failure and error information into the execution

def test_logging():
    LOGGER=logging.getLogger(__name__)
    LOGGER.info("This is information message")
    LOGGER.warning("This is wanrning message")
    LOGGER.error("This is error info")
    LOGGER.debug("This is for debug")