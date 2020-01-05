# -*- coding: utf-8 -*-
"""Module to test out logging to kafka."""

import json
import logging

from utils.kafka_handler import KafkaHandler
from kafka import KafkaProducer


def run_it(logger=None):
    """Run the actual connections."""

    logger = logging.getLogger(__name__)
    # enable the debug logger if you want to see ALL of the lines
    #logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)

    kh = KafkaHandler(['kafka1:9092', 'kafka2:9093', 'kafka3:9094'], 'python_logging')
    logger.addHandler(kh)

    logger.info("I'm a little logger, short and stout")
    logger.debug("Don't tase me bro!")


if __name__ == "__main__":
    run_it()