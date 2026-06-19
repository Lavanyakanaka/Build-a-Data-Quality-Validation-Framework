import json
from datetime import datetime


class ReportGenerator:

    @staticmethod
    def generate(dataset_name, results):

        total = len(results)

        passed = sum(
            1 for result in results
            if result["success"]
        )

        failed = total - passed

        report = {
            "metadata": {
                "dataset_name": dataset_name,
                "timestamp": datetime.now().isoformat(),
                "overall_success": failed == 0
            },

            "summary": {
                "total_expectations": total,
                "passed": passed,
                "failed": failed
            },

            "results": results
        }

        return report

    @staticmethod
    def save(report, output_path):

        with open(output_path, "w") as file:
            json.dump(
                report,
                file,
                indent=4
            )