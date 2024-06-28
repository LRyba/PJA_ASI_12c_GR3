import pandas as pd
from sdv.lite import SingleTablePreset
from sdv.metadata import SingleTableMetadata

def generate_synthetic_data(obesity_data: pd.DataFrame, num_rows: int) -> pd.DataFrame:
    # Generate metadata from the DataFrame automatically and adjust types
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data=obesity_data)

    # Create the synthesizer with the 'FAST_ML' preset
    synthesizer = SingleTablePreset(
        metadata=metadata,
        name='FAST_ML'
    )

    # Fit the model
    synthesizer.fit(obesity_data)
    
    # Generate synthetic data
    synthetic_data = synthesizer.sample(num_rows=num_rows)
    return synthetic_data
