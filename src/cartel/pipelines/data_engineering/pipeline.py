from kedro.pipeline import node, Pipeline
from cartel.pipelines.data_engineering.nodes import (
    preprocess_location,
)

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_location,
                inputs='sf_location',
                outputs='preprocessed_location_sf',
                name='preprocessing_location_sf',
            ),
            node(
                func=preprocess_location,
                inputs='rome_location',
                outputs='preprocessed_location_rome',
                name='preprocessing_location_rome',
            ),
        ]
    )