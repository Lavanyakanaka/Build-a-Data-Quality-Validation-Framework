from dqframework.expectations.not_null import NotNullExpectation
from dqframework.expectations.unique import UniqueExpectation
from dqframework.expectations.between import BetweenExpectation
from dqframework.expectations.in_set import InSetExpectation
from dqframework.expectations.mean_between import MeanBetweenExpectation
from dqframework.expectations.row_count import RowCountExpectation
from dqframework.expectations.type_check import TypeExpectation


class ExpectationFactory:

    EXPECTATIONS = {
        "expect_column_to_not_be_null": NotNullExpectation,
        "expect_column_values_to_be_unique": UniqueExpectation,
        "expect_column_values_to_be_between": BetweenExpectation,
        "expect_column_values_to_be_in_set": InSetExpectation,
        "expect_column_mean_to_be_between": MeanBetweenExpectation,
        "expect_table_row_count_to_be_between": RowCountExpectation,
        "expect_column_values_to_be_of_type": TypeExpectation
    }

    @classmethod
    def create(cls, config):

        expectation_type = config.get("type")

        if expectation_type not in cls.EXPECTATIONS:
            raise ValueError(
                f"Unsupported expectation: {expectation_type}"
            )

        return cls.EXPECTATIONS[expectation_type](config)