import pandas as pd
from sdv.tabular import CTGAN

def generate_synthetic_data(obesity_data: pd.DataFrame, num_rows: int) -> pd.DataFrame:
    model = CTGAN()
    model.fit(obesity_data)
    synthetic_data = model.sample(num_rows)
    return synthetic_data
