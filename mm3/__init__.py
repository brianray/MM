#!/usr/bin/env python

__version__ = "0.1.3"
__author__ = [
    "Brian Ray <brianhray@gmail.com>",
]
__license__ = "TBD"

from .document_base import *
from . import config_base
from . import model_base
import logging
logging.basicConfig()


Date = model_base.DateFieldType
URL = model_base.URLFieldType
Image = model_base.ImageFieldType
Formula = model_base.FormulaFieldType

Config = config_base.ConfigBase
