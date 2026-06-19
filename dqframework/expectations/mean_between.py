from .base_expectation import BaseExpectation

class MeanBetweenExpectation(BaseExpectation):

    def validate(self, df):
        column = self.config["column"]

        min_value = self.config["min_value"]
        max_value = self.config["max_value"]

        mean_value = float(df[column].mean())

        return {
            "expectation": "expect_column_mean_to_be_between",
            "success": bool(
                min_value <= mean_value <= max_value
        ),
            "observed_value": mean_value,
            "kwargs": self.config
        }