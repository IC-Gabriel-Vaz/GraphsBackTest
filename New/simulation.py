import pandas as pd


class Simulation:

    def __init__(self, data, parameters):

        self.portfolio_value = parameters.investment
        self.shares = dict((asset,0) for asset in data.all_assets)
        self.weights = {asset: 0 for asset in data.all_assets}


    def simulate(self,data):

        print(f'Inicial investment: {self.portfolio_value} \n')

        for date in data.out_of_Sample_dates:

            self.daily_price = data.all_prices.loc[date]

            if date in data.rebalance_dates:

                print('**** rebalancing ******* \n')
                
                rebalance_prices = self.get_rebalance_prices(data,date)

                self.rebalance(data,rebalance_prices)

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
    
    def rebalance(self, data, rebalance_prices):

        total_rows = rebalance_prices.shape[0]

        nan_counts = rebalance_prices.isna().sum()

        cols_with_many_nans = nan_counts[nan_counts > total_rows*0.5].index

        optmization_prices = rebalance_prices.drop(columns=cols_with_many_nans)

        weights_dict = self.optmize(optmization_prices)

        # print(type(self.weights))

        # for asset in self.weights.keys():

        #     self.weights = weights_dict.get(asset,0)

        # print(self.weights)

    def optmize(self,optmization_prices):

        new_weights = {}

        for asset in optmization_prices.columns:

            new_weights[asset] = 1/len(optmization_prices)

        print(new_weights)

        return new_weights