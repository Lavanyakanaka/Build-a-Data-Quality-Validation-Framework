import pandas as pd
from dqframework.expectations.between import (
    BetweenExpectation
)


def test_between_failure():

    df = pd.DataFrame({
        "age": [10, 200]
    })

    exp = BetweenExpectation({
        "column": "age",
        "min_value": 18,
        "max_value": 100
    })

    result = exp.validate(df)

    assert result["success"] is False