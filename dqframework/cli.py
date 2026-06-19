import sys

from dqframework.engine.validator import Validator


def main():

    if len(sys.argv) != 2:

        print(
            "Usage: python -m dqframework.cli <config_file>"
        )

        return

    config_path = sys.argv[1]

    validator = Validator()

    report = validator.run(config_path)

    print("\nValidation Completed\n")

    print(
        f"Overall Success: "
        f"{report['metadata']['overall_success']}"
    )

    print(
        f"Passed: "
        f"{report['summary']['passed']}"
    )

    print(
        f"Failed: "
        f"{report['summary']['failed']}"
    )


if __name__ == "__main__":
    main()