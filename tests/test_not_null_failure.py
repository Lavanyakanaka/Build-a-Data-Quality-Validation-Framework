import pandas as pd
from dqframework.expectations.not_null import (
    NotNullExpectation
)


def test_not_null_failure():

    df = pd.DataFrame({
        "id": [1, None, 3]
    })

    exp = NotNullExpectation({
        "column": "id"
    })

    result = exp.validate(df)

    assert result["success"] is False