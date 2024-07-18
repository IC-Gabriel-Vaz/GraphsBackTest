import pandas as pd

class TCSimulation:

    def __init__(self, data, parameters):

        self.portfolioValue = parameters.investment


        self.start_day = data.out_of_Sample_dates[0]



    def simulate(self, data, parameters):

        prices = data.all_prices

        print(f'Inicial investment: {self.portfolioValue} \n')

        prices.ffill(inplace=True)
        
        prices.bfill(inplace=True)

        for date in data.out_of_Sample_dates:




    

    def calculate_potfolioValue(self,prices,date):

        if date == self.start_day:
            print('')