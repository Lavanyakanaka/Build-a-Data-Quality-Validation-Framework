from .csv_source import CSVSource
from .dataframe_source import DataFrameSource


class DataSourceFactory:

    @staticmethod
    def create(source_type):

        if source_type.lower() == "csv":
            return CSVSource()

        if source_type.lower() == "dataframe":
            return DataFrameSource()

        raise ValueError(f"Unsupported datasource: {source_type}")