import get_assets_prices

def get_returns(app):

    prices = get_assets_prices.get_prices(app)

    returns = prices.pct_change()
    print(returns)

    return returns

if __name__ == '__main__':

    app = 'IBOV'

    get_returns(app)

