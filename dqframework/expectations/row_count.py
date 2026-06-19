from .base_expectation import BaseExpectation

class RowCountExpectation(BaseExpectation):

    def validate(self, df):

        min_value = self.config["min_value"]
        max_value = self.config["max_value"]

        row_count = len(df)

        return {
            "expectation": "expect_table_row_count_to_be_between",
            "success": bool(
                min_value <= row_count <= max_value
            ),
            "observed_value": row_count,
            "kwargs": self.config
        }