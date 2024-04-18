import pandas as pd
import sys

sys.path.append("../classes")
sys.path.append('../dbUtils')

from data import Data

import get_assets_prices as gp
import get_assets as ga

def get_data(adm,parameters):

    data = Data()

    data.date = parameters.in_sample_initial_date

    data.prices = gp.get_prices(parameters.app , adm)

    data.returns = data.prices.pct_change().dropna()

    data.official_dates = data.get_official_dates(parameters.app)

    return data