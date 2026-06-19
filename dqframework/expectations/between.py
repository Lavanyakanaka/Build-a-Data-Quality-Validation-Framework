from .base_expectation import BaseExpectation

class BetweenExpectation(BaseExpectation):

    def validate(self, df):
        column = self.config["column"]
        min_value = self.config["min_value"]
        max_value = self.config["max_value"]

        out_of_range = (
            ((df[column] < min_value) |
             (df[column] > max_value))
        ).sum()

        return {
            "expectation": "expect_column_values_to_be_between",
            "success": bool(out_of_range == 0),
            "observed_value": int(out_of_range),
            "kwargs": self.config
        }