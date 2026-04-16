#!/usr/bin/env python3

import argparse
import sys
import pandas as pd

def transpose_qacct(input_data: str) -> pd.DataFrame:
    """
    Transpose qacct log into a DataFrame.

    Parameters:
    input_data (str): The raw input data as a string.

    Returns:
    pd.DataFrame: A DataFrame containing the transposed qacct log.
    """
    qacct_log_big_dict = dict()
    qacct_log_small_dict = dict()

    list_of_entries = input_data.split("==============================================================")
    for entry in list_of_entries:
        if entry.strip(): # makes sure entry isnt empty
            for line in entry.split("\n"):
                if line.strip(): # makes sure line isn't empty
                    formatted_line = ",".join(line.strip().replace(",", ";").split(maxsplit=1))
                    key, value = formatted_line.split(",")[0].strip(), formatted_line.split(",")[1].strip()
                    qacct_log_small_dict[key] = value
            qacct_log_big_dict[qacct_log_small_dict["jobnumber"]] = qacct_log_small_dict
            qacct_log_small_dict = dict()
            
    # Convert the big dictionary to a pandas DataFrame
    df = pd.DataFrame.from_dict(qacct_log_big_dict, orient="index")
    
    # Prepend a single quote to datetime columns
    df['qsub_time'] = "'" + df['qsub_time'].astype(str)
    df['start_time'] = "'" + df['start_time'].astype(str)
    df['end_time'] = "'" + df['end_time'].astype(str)
    
    return df

def run(input_file: str, output_file: str) -> None:
    """
    Main function to execute the script.

    Parameters:
    input_file (str): Path to the input file.
    output_file (str): Path to the output file (if provided).
    """
    # Read input from file or stdin
    if input_file:
        try:
            with open(input_file, 'r') as file:
                input_data = file.read()
        except IOError as e:
            print(f"Error reading input file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        input_data = sys.stdin.read()

    # Call the function to transpose qacct log
    df = transpose_qacct(input_data)

    # Write to output file or print to stdout
    if output_file:
        try:
            df.to_csv(output_file, index_label="ID")
        except IOError as e:
            print(f"Error writing to output file: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        df.to_csv(sys.stdout, index_label="ID")

if __name__ == "__main__":
    # Argument parser
    parser = argparse.ArgumentParser(description="Transpose qacct logs into a CSV format.")

    # Input file argument
    parser.add_argument("--input", help="Input file path")

    # Output file argument
    parser.add_argument("--output", help="Output file path (optional)")

    # Parse arguments
    args = parser.parse_args()

    # Ensure that at least an input file or stdin is provided
    if not args.input and not sys.stdin.isatty():
        print("No input file specified. Reading from stdin.", file=sys.stderr)
    
    # Run the main function
    run(args.input, args.output)
