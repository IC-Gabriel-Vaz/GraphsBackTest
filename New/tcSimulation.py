import pandas as pd

class TCSimulation:

    def __init__(self, data, parameters):

        self.portfolio_value = parameters.investment
        self.shares = dict((asset,0) for asset in data.all_assets)
        self.rebalance_weights = {asset: 0 for asset in data.all_assets}
        self.valuation = {asset: 0 for asset in data.all_assets}
        self.proportion = {asset: 0 for asset in data.all_assets}
        self.portfolio_weights = {asset: 0 for asset in data.all_assets}

        self.weights_history = pd.DataFrame()
        self.shares_history = pd.DataFrame()
        self.valuation_history = pd.DataFrame()

        self.start_day = data.out_of_Sample_dates[0]


    def simulate(self,data,parameters):

        prices = data.all_prices

        print(f'Inicial investment: {self.portfolio_value} \n')

        prices.ffill(inplace=True)
        
        prices.bfill(inplace=True)

        for date in data.out_of_Sample_dates:

            self.portfolio_value = self.calculate_portfolio_value(prices.loc[date] , date,parameters)

            if date in data.rebalance_dates:

                print('************ rebalancing ************ \n')
                
                rebalance_prices = self.get_rebalance_prices(data,date)

                weights  = self.rebalance(data,rebalance_prices)

                rebalance_proportion = {asset: 0 for asset in data.all_assets}

                for asset in data.all_assets:
                    rebalance_proportion[asset] = self.portfolio_value*weights[asset] - self.portfolio_value*weights[asset]*parameters.transactionCosts
                
                for asset in data.all_assets:
                    self.shares[asset] = rebalance_proportion[asset]/prices[asset].loc[date]

            self.portfolio_value = self.calculate_portfolio_value(prices.loc[date], date, parameters)
            self.portfolio_weights = self.calculate_portfolio_weights(prices.loc[date])
            self.weights_history = self.weights_history._append(pd.DataFrame(self.portfolio_weights , index=[date]))
            self.shares_history = self.shares_history._append(pd.DataFrame(self.shares , index=[date]))
            self.valuation_history = self.valuation_history._append(pd.DataFrame(self.valuation, index=[date]))
            print(f'{date}  {self.portfolio_value:.2f} \n')

        # print(self.valuation_history)
        # print(self.weights_history)
        # print(self.shares_history)

    def calculate_portfolio_value(self, prices, date,parameters):

        if date == self.start_day:
            self.portfolio_value = parameters.investment - self.portfolio_value*parameters.transactionCosts

        else:
            for (asset,shares_per_asset), price in zip(self.shares.items(),prices):
                self.valuation[asset] = shares_per_asset*price
                self.portfolio_value = sum(self.valuation.values())
                # if shares_per_asset != 0:
                #     print(f'{asset} : {shares_per_asset :.3f} shares  at {price :.2f}')
        
        return self.portfolio_value

    def get_rebalance_prices(self,data, date):

        start_date = date - pd.Timedelta(days=100)
        end_date = date - pd.Timedelta(days=1)

        rebalance_prices = data.all_prices.loc[start_date:end_date]

        return rebalance_prices
    
    def rebalance(self, data, rebalance_prices):

        total_rows = rebalance_prices.shape[0]

        nan_counts = rebalance_prices.isna().sum()

        cols_with_many_nans = nan_counts[nan_counts > total_rows*0.2].index

        optmization_prices = rebalance_prices.drop(columns=cols_with_many_nans)

        removed_cols = []

        for col in optmization_prices.columns:
            if pd.isna(optmization_prices[col].iloc[0]):
                removed_cols.append(col)
                optmization_prices.drop(columns=[col], inplace=True)


        optmization_prices.ffill()
        optmization_prices.bfill()

        weights_dict = self.optmize(optmization_prices)

        for asset in self.rebalance_weights.keys():

            if asset in weights_dict.keys():

                self.rebalance_weights[asset] = weights_dict[asset]
            else:

                self.rebalance_weights[asset] = 0

        return self.rebalance_weights

    def optmize(self,optmization_prices):

        returns = optmization_prices.pct_change().dropna()
        #print(returns)

        new_weights = {}


        for asset in optmization_prices.columns:

            new_weights[asset] = (1/len(optmization_prices.columns))

        return new_weights
    
    def calculate_portfolio_weights(self, prices):

        portfolio_weights = {}

        for asset in self.valuation.keys():
            self.valuation[asset]/self.portfolio_value

        return portfolio_weights
    