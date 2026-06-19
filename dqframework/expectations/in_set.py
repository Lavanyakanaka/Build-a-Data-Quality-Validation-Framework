from .base_expectation import BaseExpectation

class InSetExpectation(BaseExpectation):

    def validate(self, df):
        column = self.config["column"]
        allowed_values = self.config["values"]

        invalid_count = (~df[column].isin(allowed_values)).sum()

        return {
            "expectation": "expect_column_values_to_be_in_set",
            "success": bool(invalid_count == 0),
            "observed_value": int(invalid_count),
            "kwargs": self.config
        }