from kedro.pipeline import Pipeline, node
from .nodes import generate_synthetic_data

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=generate_synthetic_data,
                inputs=["obesity_data", "params:syn_num_rows"],
                outputs="synthetic_data",
                name="generate_synthetic_data_node",
            )
        ]
    )
