import pandas as pd
import get_assets_prices

def official_dates(app):

    prices_df = get_assets_prices.get_prices(app)

    official_dates = prices_df.dropna(subset=['BOVA11']).index.to_list()

    print(official_dates)

    return official_dates


if __name__ == '__main__':

    official_dates('IBOV')