#!/bin/sh

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
PROJECT_DIR="$SCRIPT_DIR"

cd "$SCRIPT_DIR" || exit 1
test -e ssshtest || curl -fsSL https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest -o ssshtest
. ./ssshtest

DATA_FILE="$PROJECT_DIR/test_data.csv"
PRINT_FIRES="$PROJECT_DIR/print_fires.py"

run raw_values python3 "$PRINT_FIRES" -f "$DATA_FILE" -c Albania
assert_exit_code 0
assert_equal "$(cat "$STDOUT_FILE")" "[4, 8, 12]"

run mean python3 "$PRINT_FIRES" -f "$DATA_FILE" -c Albania -o mean
assert_exit_code 0
assert_equal "$(cat "$STDOUT_FILE")" "8"

run median python3 "$PRINT_FIRES" -f "$DATA_FILE" -c Albania -o median
assert_exit_code 0
assert_equal "$(cat "$STDOUT_FILE")" "8"

run standard_deviation python3 "$PRINT_FIRES" -f "$DATA_FILE" -c Albania \
	-o standard_deviation
assert_exit_code 0
assert_equal "$(cat "$STDOUT_FILE")" "3.265986323710904"

run custom_columns python3 "$PRINT_FIRES" -f "$DATA_FILE" -c Canada \
	-cc 0 -fc 3
assert_exit_code 0
assert_equal "$(cat "$STDOUT_FILE")" "[5, 15]"

run missing_required_argument python3 "$PRINT_FIRES" -f "$DATA_FILE"
assert_exit_code 2