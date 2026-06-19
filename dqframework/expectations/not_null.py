from .base_expectation import BaseExpectation


class NotNullExpectation(BaseExpectation):

    def validate(self, df):

        column = self.config["column"]

        if column not in df.columns:
            return {
                "expectation": "expect_column_to_not_be_null",
                "success": False,
                "observed_value": "COLUMN_NOT_FOUND",
                "kwargs": self.config
            }

        null_count = df[column].isnull().sum()

        return {
            "expectation": "expect_column_to_not_be_null",
            "success": bool(null_count == 0),
            "observed_value": int(null_count),
            "kwargs": self.config
        }