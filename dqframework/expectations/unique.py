from .base_expectation import BaseExpectation

class UniqueExpectation(BaseExpectation):

    def validate(self, df):
        column = self.config["column"]

        duplicate_count = df[column].duplicated().sum()

        return {
            "expectation": "expect_column_values_to_be_unique",
            "success": bool(duplicate_count == 0),
            "observed_value": int(duplicate_count),
            "kwargs": self.config
        }