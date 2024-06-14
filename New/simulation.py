import pandas as pd


class Simulation:

    def __init__(self, data, parameters):

        self.portfolio_value = parameters.investment
        self.shares = dict((asset,0) for asset in data.all_assets)
        self.weights = {asset: 0 for asset in data.all_assets}
        self.valuation = {asset: 0 for asset in data.all_assets}
        self.proportion = {asset: 0 for asset in data.all_assets}


    def simulate(self,data):

        prices = data.all_prices

        print(f'Inicial investment: {self.portfolio_value} \n')

        prices.ffill(inplace=True)
        
        prices.bfill(inplace=True)

        for date in data.out_of_Sample_dates:

            if date in data.rebalance_dates:

                print('**** rebalancing ******* \n')
                
                rebalance_prices = self.get_rebalance_prices(data,date)

                weights  = self.rebalance(data,rebalance_prices)

                rebalance_proportion = {asset: 0 for asset in data.all_assets}

                for asset in data.all_assets:
                    rebalance_proportion[asset] = self.portfolio_value*weights[asset]
                
                for asset in data.all_assets:
                    self.shares[asset] = rebalance_proportion[asset]/prices[asset].loc[date]
            
            self.portfolio_value = self.calculate_portfolio_value(prices.loc[date])

            print(f'{date}  {self.portfolio_value} \n')

        

    def calculate_portfolio_value(self, prices):

        for (asset,shares_per_asset), price in zip(self.shares.items(),prices):
            self.valuation[asset] = shares_per_asset*price
            self.portfolio_value = sum(self.valuation.values())
        
        return self.portfolio_value

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

        removed_cols = []

        for col in optmization_prices.columns:
            if pd.isna(optmization_prices[col].iloc[0]):
                removed_cols.append(col)
                optmization_prices.drop(columns=[col], inplace=True)

        optmization_prices.ffill()
        optmization_prices.bfill()

        weights_dict = self.optmize(optmization_prices)

        for asset in self.weights.keys():

            if asset in weights_dict.keys():

                self.weights[asset] = weights_dict[asset]
            else:

                self.weights[asset] = 0

        return self.weights

    def optmize(self,optmization_prices):

        new_weights = {}

        for asset in optmization_prices.columns:

            new_weights[asset] = (1/len(optmization_prices.columns))

        return new_weights