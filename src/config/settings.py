# settings.py
import json
import os
from collections import namedtuple
from typing import Dict, Type

from dotenv import load_dotenv
from pathlib import Path  # python3 only
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
env_path = Path('..') / '.env'
load_dotenv(dotenv_path=env_path)


class CBEFFConfig:
    """ cbeff related config"""
    version_major = os.getenv("atk.cbeff.version.major")  # default 1
    version_minor = os.getenv("atk.cbeff.version.minor")  # default 1
    cbeff_version_major = os.getenv("atk.cbeff.cbeff_version.major")  # default 1
    cbeff_version_minor = os.getenv("atk.cbeff.cbeff_version.minor")  # default 1
    format_organization = os.getenv("atk.cbeff.format.organization")  # default Mosip
    format_type = os.getenv("atk.cbeff.format.type")  # default 257
    level = os.getenv("atk.cbeff.level")  # default Raw
    purpose = os.getenv("atk.cbeff.purpose")  # default Enroll
    quality_algorithm_organization = os.getenv("atk.cbeff.quality.algorithm.organisation")  # default HMAC
    quality_algorithm_type = os.getenv("atk.cbeff.quality.algorithm.type")  # default SHA-256
    quality_score = os.getenv("atk.cbeff.quality.score")  # default 100
    bir_info_integrity = os.getenv("atk.cbeff.birinfo.integrity")  # default false


class QueueConfig:
    """ Queue related config """
    host = os.getenv("atk.queue.host")  # default 'http://localhost'
    port = os.getenv("atk.queue.port")  # default '8161'
    user = os.getenv("atk.queue.user")  # default 'admin'
    password = os.getenv("atk.queue.password")  # 'admin'
    send_address = os.getenv("atk.queue.send_address")  # 'm2a'
    consume_address = os.getenv("atk.queue.consume_address")  # 'a2m'
    client_id = os.getenv("atk.queue.client_id")  # 'any string'


class AppConfig:
    """ App config """
    callback_url = os.getenv("atk.app.callback_url")  # default 'http://localhost:8000/'
    abis_max_results = os.getenv("atk.app.abis_max_results")  # default 30
    abis_target_fpir = os.getenv("atk.app.abis_target_fpir")  # default 30
    abis_response_timeout = os.getenv("atk.app.abis_response_timeout")
    abis_threshold = os.getenv("atk.app.abis_threshold")

