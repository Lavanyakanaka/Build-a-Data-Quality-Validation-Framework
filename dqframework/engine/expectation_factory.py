@classmethod
def create(cls, config):

    expectation_type = config.get("type")

    if expectation_type not in cls.EXPECTATIONS:
        raise ValueError(
            f"Unsupported expectation: {expectation_type}"
        )

    return cls.EXPECTATIONS[
        expectation_type
    ](config)