from .base_expectation import BaseExpectation


class TypeExpectation(BaseExpectation):

    TYPE_MAP = {
        "int": "int",
        "float": "float",
        "string": "object"
    }

    def validate(self, df):

        column = self.config["column"]

        if column not in df.columns:
            return {
                "expectation": "expect_column_values_to_be_of_type",
                "success": False,
                "observed_value": "COLUMN_NOT_FOUND",
                "kwargs": self.config
            }

        expected_type = self.config["dtype"]

        observed_type = str(df[column].dtype)

        success = (
            self.TYPE_MAP.get(
                expected_type,
                expected_type
            )
            in observed_type
        )

        return {
            "expectation": "expect_column_values_to_be_of_type",
            "success": bool(success),
            "observed_value": observed_type,
            "kwargs": self.config
        }