# Data Quality Validation Framework

## Overview

This project is a reusable and extensible Data Quality Validation Framework inspired by Great Expectations. It enables users to define data quality rules declaratively using YAML configuration files and validate datasets programmatically.

The framework supports validation of CSV files and in-memory Pandas DataFrames. Validation results are generated as structured JSON reports containing detailed information about each expectation and overall dataset health.

---

## Features

* Declarative YAML-based expectation suites
* CSV and Pandas DataFrame support
* Modular and extensible architecture
* JSON validation reporting
* Command Line Interface (CLI)
* Comprehensive automated tests
* Easy addition of custom expectations

---

## Architecture

```text
CLI
 |
Validator Engine
 |
Expectation Factory
 |
Expectations
 |
Datasource Connectors
 |
Report Generator
```

### Components

* **Datasource Layer**: Loads data from CSV files or Pandas DataFrames.
* **Expectation Layer**: Contains reusable expectation classes.
* **Expectation Factory**: Dynamically creates expectation objects from configuration.
* **Validator Engine**: Executes validations and collects results.
* **Report Generator**: Produces structured JSON reports.
* **CLI**: Runs validations from the command line.

---

## Supported Expectations

### 1. expect_column_to_not_be_null

Validates that a column contains no null values.

### 2. expect_column_values_to_be_unique

Validates that all values in a column are unique.

### 3. expect_column_values_to_be_of_type

Validates that a column has the expected data type.

### 4. expect_column_values_to_be_in_set

Validates that column values belong to a predefined set.

### 5. expect_column_values_to_be_between

Validates that numeric values fall within a specified range.

### 6. expect_column_mean_to_be_between

Validates that the mean of a numeric column falls within a specified range.

### 7. expect_table_row_count_to_be_between

Validates that the dataset row count is within a specified range.

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running the Framework

Validate a dataset using:

```bash
python -m dqframework.cli configs/customer_suite.yaml
```

Validate a dataset containing known quality issues:

```bash
python -m dqframework.cli configs/bad_data_suite.yaml
```

---

## Example Configuration

```yaml
dataset_name: customers

data_source:
  type: csv
  path: data/customers.csv

expectations:
  - type: expect_column_to_not_be_null
    column: customer_id
```

---

## Example Validation Report

```json
{
  "metadata": {
    "dataset_name": "customers",
    "overall_success": true
  },
  "summary": {
    "total_expectations": 7,
    "passed": 7,
    "failed": 0
  }
}
```

---

## Extending the Framework

New expectations can be added by creating a class that inherits from `BaseExpectation`.

Example:

```python
class RegexExpectation(BaseExpectation):

    def validate(self, df):
        pass
```

Register the new expectation in `ExpectationFactory`:

```python
EXPECTATIONS = {
    "expect_column_values_to_match_regex": RegexExpectation
}
```

No changes to the validation engine are required.

---

## Testing

Run all tests using:

```bash
pytest
```

---

## Project Structure

```text
dqframework/
├── datasource/
├── engine/
├── expectations/
├── reporting/
├── utils/
└── cli.py
```

---

## Future Enhancements

* Apache Spark support
* Polars support
* Regex-based expectations
* Data profiling reports
* HTML reporting
* Cloud storage connectors
