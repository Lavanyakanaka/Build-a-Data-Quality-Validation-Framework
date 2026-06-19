from dqframework.utils.config_loader import load_config
from dqframework.datasource.datasource_factory import DataSourceFactory
from dqframework.engine.expectation_factory import ExpectationFactory
from dqframework.reporting.report_generator import ReportGenerator


class Validator:

    def run(self, config_path):

        config = load_config(config_path)

        dataset_name = config["dataset_name"]

        source_config = config["data_source"]

        datasource = DataSourceFactory.create(
            source_config["type"]
        )

        df = datasource.load(
            source_config["path"]
        )

        results = []

        for expectation_config in config["expectations"]:

            expectation = ExpectationFactory.create(
                expectation_config
            )

            result = expectation.validate(df)

            results.append(result)

        report = ReportGenerator.generate(
            dataset_name,
            results
        )

        ReportGenerator.save(
            report,
            "reports/validation_report.json"
        )

        return report