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

            self.portfolioValue = self.calculate_potfolioValue(prices.loc[date], date)

            if date in data.rebalance_dates:

                print('*************Rebalancing************** \n ')

                rebalance_prices = self.get_rebalance_prices(data,date,parameters)

                print(rebalance_prices)
                if date == self.start_day:
                    print('')




    

    def calculate_potfolioValue(self,prices,date):

        if date == self.start_day:
            print('Oiii')

        else:
            print('aaaaaaaaaaaaa')


    def get_rebalance_prices(self,data, date, parameters):

        start_date = date - pd.Timedelta(days=parameters.inSample)
        print(start_date)
        end_date = date - pd.Timedelta(days=1)
        print(data.all_prices)

        rebalance_prices = data.all_prices.loc[start_date:end_date]

        return rebalance_prices