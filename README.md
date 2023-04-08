# Email-validator

This is a Python script that checks email addresses using the email_validator library and multithreading.

## Usage

To use this script, you will need to install the email_validator and tqdm libraries:
```
pip install email_validator tqdm
```
The script will read a CSV file containing email addresses and validate each address using the email_validator library. It will output the results to a new CSV file.

## Multithreading

The script uses multithreading to speed up the validation process. It creates a process pool with a number of workers equal to the number of logical processors on your system. Each worker validates a subset of the email addresses in parallel.
