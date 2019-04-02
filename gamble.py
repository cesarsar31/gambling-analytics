# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:31:23 2019

@author: Consultor
"""

from datetime import datetime
import os
import pytz
import requests
import math
API_KEY = 'XuO9JzLhSFGNrHKo7AGnPCQF3Qa2oRCnOByzN60gTIzDqfW5CVfLIRQZEiJz'
API_URL = ('https://soccer.sportmonks.com/api/v2.0/leagues?api_token={}')

def query_api():
    data = requests.get(API_URL.format(API_KEY)).json()
    return data




