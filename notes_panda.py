from pandas.core import groupby
from pandas.core.reshape.concat import concat
from pandas.core.reshape.merge import merge_ordered
from pydataset import data
import numpy as np
import pandas as pd
from env import host, user, password

def get_db_url(url='employees'):
    url = f'mysql+pymysql://{user}:{password}@{host}/{url}'
    return url

