import pandas as pd
import sys
from datetime import datetime , timedelta
import New.argParse as argParse

sys.path.append("../classes")
sys.path.append('../dbUtils')


############ Classes ##############
from admin import Admin
from simulation import Simulation
from data import Data
from parameters import Parameters
###################################

########### Functions #############
import New.read_txt as read_txt
import get_sim_prices as gp
import get_assets as ga
import New.argParse as argParse

###################################



if __name__ == '__main__':

    txt = argParse.argParse()

    parameters = Parameters(txt)

    adm = Admin(parameters.db_path)
    adm.connect()

    print('Loading Data ... \n')

    gp.get_simulation_prices(parameters, adm)

