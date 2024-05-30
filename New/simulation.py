import pandas as pd


class Simulation:

    def __init__(self, data, parameters):

        self.portfolio_value = parameters.investment
        self.shares = dict((asset,0) for asset in data.all_assets)

    def simulate(self,data):

        print(f'Inicial investment: {self.portfolio_value} \n')

        for date in data.out_of_Sample_dates:

            self.daily_price = data.all_prices.loc[date]

            if date in data.rebalance_dates:

                print('**** rebalancing ******* \n')
                print(self.get_rebalance_prices(data,date))

            # print(f'{date}   {self.portfolio_value} \n')

    def calculate_portfolio_value(self, prices):

        portfolio_value = 0

        for (asset,shares_per_asset), price in zip(self.shares.items(),prices):
            valuation = shares_per_asset*price
            portfolio_value += valuation

    def get_rebalance_prices(self,data, date):

        start_date = date - pd.Timedelta(days=100)
        end_date = date - pd.Timedelta(days=1)

        rebalance_prices = data.all_prices.loc[start_date:end_date]
        return rebalance_prices
        
    
        return portfolio_value