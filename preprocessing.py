import pandas as pd

class Preprocessor:

    def __init__(self, data=None):
        self.data = pd.DataFrame()

    def get_pink_morsels_data(self):
        df = self.data
        for i in range(3):
            new = pd.read_csv(f"./data/daily_sales_data_{i}.csv")
            df = pd.concat([df, new], ignore_index=True)

        df = df[df['product'] == 'pink morsel']

        df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

        df['sales'] = df['quantity'] * df['price']

        cols_to_drop = ["quantity", "price"]
        df = df.drop(cols_to_drop, axis=1)

        self.data = df.reset_index()
        return self.data


if __name__ == "__main__":
    preprocessor = Preprocessor()

    pm_data = preprocessor.get_pink_morsels_data()
    print(pm_data)
    pm_data.to_csv("data/preprocessed.csv")

