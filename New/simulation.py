import pandas



class Simulation:

    def __init__(self, data, parameters):

        self.weights = self.get_first_weights(data)
        self.portfolio_value = parameters.investment
        self.shares = dict((asset,0) for asset in data.out_of_Sample_assets
)

    
    def get_first_weights(self,data):

        # Aqui a ideia é que a regra de escolha fique a cargo do usuário
        #equal weights de exemplo inicial

        weights = {}

        assets = data.all_prices.columns

        for asset in assets:
            weights[asset] = (1/len(assets))

        return weights

    def simulate(self,data):

        print(f'Inicial investment: {self.portfolio_value} \n')

        for date in data.out_of_Sample_dates:

            self.daily_price = data.all_prices.loc[date]

            if date in data.rebalance_dates:

                print('**** rebalancing ******* \n')

                amount_per_asset = {}
                
                for asset, weight in self.weights.items():
                 
                    money_availble_per_asset = (self.portfolio_value)*(weight)
                  
                    amount_per_asset[asset] = money_availble_per_asset
    
                for asset, value in amount_per_asset.items():
                    shares_per_asset = value/data.all_prices.iloc[0][asset]
                    self.shares[asset] = shares_per_asset

            self.portfolio_value = self.calculate_portfolio_value(self.daily_price)

            print(f'{date}   {self.portfolio_value} \n')

    def calculate_portfolio_value(self, prices):

        portfolio_value = 0

        for (asset,shares_per_asset), price in zip(self.shares.items(),prices):
            valuation = shares_per_asset*price
            portfolio_value += valuation
        
    
        return portfolio_value