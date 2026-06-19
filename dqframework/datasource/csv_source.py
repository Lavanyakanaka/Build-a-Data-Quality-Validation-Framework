import pandas as pd
from dqframework.utils.exceptions import DataSourceError


class CSVSource:

    def load(self, path):

        try:
            return pd.read_csv(path)

        except FileNotFoundError:
            raise DataSourceError(
                f"CSV file not found: {path}"
            )

        except Exception as e:
            raise DataSourceError(
                f"Failed to load CSV: {str(e)}"
            )