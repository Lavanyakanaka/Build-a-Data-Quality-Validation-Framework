import pandas as pd
from dqframework.expectations.unique import (
    UniqueExpectation
)


def test_unique_failure():

    df = pd.DataFrame({
        "id": [1, 1, 2]
    })

    exp = UniqueExpectation({
        "column": "id"
    })

    result = exp.validate(df)

    assert result["success"] is False