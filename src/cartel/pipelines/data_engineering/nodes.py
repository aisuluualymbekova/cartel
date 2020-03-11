import pandas as pd


def _parse_time(x):
    return pd.to_datetime(x, unit='ms')


def preprocess_location(location: pd.DataFrame) -> pd.DataFrame:
    """Preprocess the data for locations.

        Args:
            location: Source data.
        Returns:
            Preprocessed data.
    """

    location['time'] = location['time'].apply(_parse_time)

    return location
