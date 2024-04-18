import pandas as pd
import sys
from datetime import datetime , timedelta
import argParse

sys.path.append("../classes")
sys.path.append('../dbUtils')


############ Classes ##############
from admin import Admin
from parameters import Parameters
###################################

########### Functions #############
import read_txt
import get_assets_prices as gp
import get_assets as ga
###################################

def gettxt(txt):

    parameters = Parameters()

    parameters.app = txt['app']

    parameters.db_path = txt['databasePath']

    in_sample_initial_date = txt['in_sample_initial_date']

    in_sample_end_date = txt['in_sample_end_date']

    out_of_sample_initial_date = txt['out_of_sample_initial_date']

    out_of_sample_end_date = txt['out_of_sample_end_date']

    parameters.rebalance_frequency = int(txt['rebalance'])

    parameters.investiment = int(txt['investiment'])

    parameters.in_sample_initial_date = datetime.strptime(in_sample_initial_date, "%Y-%m-%d")
    parameters.in_sample_end_date = datetime.strptime(in_sample_end_date, "%Y-%m-%d")
    parameters.out_of_sample_initial_date = datetime.strptime(out_of_sample_initial_date, "%Y-%m-%d")
    parameters.out_of_sample_end_date = datetime.strptime(out_of_sample_end_date, "%Y-%m-%d")

    # parameters.date = in_sample_initial_date

    # parameters.prices = gp.get_prices(parameters.app , parameters.adm)

    # parameters.returns = parameters.prices.pct_change().dropna()

    # parameters.simulation = Simulation(parameters.investiment)

    # parameters.official_dates = parameters.get_offcial_dates()

    return parameters


