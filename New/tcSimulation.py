import pandas as pd

class TCSimulation:

    def __init__(self, data, parameters):

        self.portfolioValue = parameters.investment

        self.shares = dict((asset,0) for asset in data.all_assets)
        self.rebalance_weights = {asset: 0 for asset in data.all_assets}

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

                weights  = self.rebalance(data,rebalance_prices)
                
                rebalance_proportion = {asset: 0 for asset in data.all_assets}

                if date == self.start_day:

                    print('Initializing portfolio \n ')
                    print('First trades will be executed')

                    for stock in data.all_assets:
                
                        # print(f'Value avaiable to be invested in {stock} is {weights[stock]*self.portfolioValue} \n')
                        # print(f'Transaction costs for {stock} will be {parameters.transactionCosts * weights[stock]*self.portfolioValue} \n ')
                        # print(f'Value to be spent in {stock} stocks is {weights[stock]*self.portfolioValue/(1+parameters.transactionCosts)} \n')
                        rebalance_proportion[stock] = weights[stock]*self.portfolioValue/(1+parameters.transactionCosts)
                    
                    shares_before = dict((asset,0) for asset in data.all_assets)

                    for asset in data.all_assets:
                        shares_before[asset] = self.shares[asset]
                        self.shares[asset] = rebalance_proportion[asset]/prices[asset].loc[date]
                        print(f'{asset}: Had {shares_before[asset]} bought {self.shares[asset]:.2f} at {prices[asset].loc[date]:.2f}')

                else:

                    print('Today is a Rebalance day, some trades will be executed')


    def calculate_potfolioValue(self,prices,date):

        if date == self.start_day:
            self.portfolioValue = self.portfolioValue

        return self.portfolioValue
            


    def get_rebalance_prices(self,data, date, parameters):

        start_date = date - pd.Timedelta(days=parameters.inSample)

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
    