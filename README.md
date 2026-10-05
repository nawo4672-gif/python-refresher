---

# Fire Data Query Tool

A lightweight Python command-line utility that queries CSV datasets to extract and parse specific numerical data (such as fire statistics) associated with a given country.

## Features

* **Command-Line Interface (CLI):** Easily run queries from your terminal using flexible arguments.
* **Robust Error Handling:** Gracefully catches missing files and handles malformed data rows.
* **Flexible Parsing:** Automatically converts string and float values (e.g., `'14.227'`) into clean integers, alerting you if any conversion errors occur.

---

## File Structure

Ensure your project directory contains the following two files:

1. `print_fires.py` (The main execution script with `argparse`)
2. `my_utils.py` (Contains the `get_column` helper function)

## Continuous Integration

The GitHub Actions workflow in `.github/workflows/test.yml` runs on every push,
on pull requests targeting `main`, and can also be started manually. It runs
these checks on Ubuntu:

* **Unit tests:** `python3 -m unittest test_my_utils.py`
* **Functional tests:** `bash test_print_fires.sh`
* **Style check:** `pycodestyle` on tracked Python files, using Python 3.14

All three checks must pass for the workflow to succeed.

---

## Usage

Run the script from your terminal using the required arguments for the file and the country name.

### Basic Syntax

```bash
python3 print_fires.py -f <path_to_csv> -c "<Country_Name>"

```

### Command-Line Arguments

| Flag / Short Flag | Long Flag | Description | Default |
| --- | --- | --- | --- |
| `-f` | `--file` | **Required.** The path to the CSV data file. | *None* |
| `-c` | `--country` | **Required.** The country name you want to query. | *None* |
| `-cc` | `--country_column` | The column index where country names are located. | `0` |
| `-fc` | `--fires_column` | The column index where fire/numeric data is located. | `3` |
| `-o` | `--operation` | An optional operation: `mean`, `median`, or `standard_deviation`. | *None* |

---

## Example

To search for fire data for **Albania** inside a file named `fire_data.csv`:

```bash
python3 print_fires.py -f fire_data.csv -c 'Albania'

```

If your dataset uses different column positions (for instance, if the country is in column `1` and fires are in column `4`), you can specify them like this:

```bash
python3 print_fires.py -f fire_data.csv -c 'Albania' -cc 1 -fc 4

```

To calculate a statistic instead of printing the returned values, use the
`--operation` argument:

```bash
python3 print_fires.py -f fire_data.csv -c 'Albania' --operation mean
```