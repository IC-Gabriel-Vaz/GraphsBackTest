import pandas as pd
import math
import sys


class Simulation:

    def __init__(self, parameters,data):
        self.shares = dict((asset,0) for asset in data.assets)
        self.shares_history = pd.DataFrame({},columns=data.assets)
        self.valuation = dict((asset,0) for asset in data.assets)
        self.valuation_history = pd.DataFrame({},columns=data.assets)
        self.portfolio_value = parameters.investment
        self.portfolio_values = pd.DataFrame(columns=['Portfolio Value'])

    def calculate_portfolio_value(self, prices):

        self.portfolio_value = 0

        for (asset,shares_per_asset), price in zip(self.shares.items(),prices):
            valuation = shares_per_asset*price
            self.portfolio_value += valuation
            self.valuation[asset] = valuation
    
        return self.portfolio_value, self.valuation
    
    def backtest_portfolio(self, weights, prices, dates):

        #print(prices)
        amount_per_asset = {}
        for asset, weight in weights.items():
            #print(weight)
            money_availble_per_asset = (self.portfolio_value)*(weight)
            #print(money_availble)
            amount_per_asset[asset] = money_availble_per_asset

        #print(amount_per_asset) 
        for asset, value in amount_per_asset.items():
            shares_per_asset = value/prices.iloc[0][asset]
            self.shares[asset] = shares_per_asset
            #shares = math.floor(shares)

        dicts = []

        for date in dates:
            print(date)
            new_dict = self.shares
            new_dict['date'] = date
            dicts.append(new_dict)

        for dictionary in dicts:
            self.shares_history = self.shares_history._append(dictionary,ignore_index = True)
             
        self.shares_history.set_index('date', inplace=True)

        valuation_dicts_list = []
        for index, row in prices.iterrows():
            #row_dict = row.to_dict()
            current_portfolio_value, valuation_dict = self.calculate_portfolio_value(row)
            print(f'{index}   {current_portfolio_value} \n')
            #self.portfolio_values.append(current_portfolio_value)
            self.portfolio_values.loc[index] = current_portfolio_value
            valuation_dict['date'] = index
            valuation_dicts_list.append(valuation_dict)

        for dictionary in valuation_dicts_list:
            self.valuation_history = self.valuation_history._append(dictionary,ignore_index = True)
        
        self.valuation_history.set_index('date', inplace=True)

        return self.portfolio_values
    
        
    

    # Considerar ações fracionárias