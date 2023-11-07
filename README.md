# README

## Overview

This repository contains a Python codebase designed to evaluate the capabilities of Large Language Models (LLM) in detecting deadlocks and resource contention issues within Python code. It offers a set of tests that challenge the LLM's ability to identify and handle potential concurrency problems.

## Features

- **Deadlock Detection:** The code includes scenarios that could potentially lead to deadlocks, allowing the LLM to demonstrate its understanding and handling of these issues.
  
- **Resource Contention Tests:** It also tests for conditions where resource contention might occur, assessing the LLM's ability to spot and mitigate race conditions.

- **Distractor Items:** The tests are conducted with and without distractor items to gauge the LLM's robustness and accuracy under varied complexity.

## How to Use

To use this testing framework, follow these simple steps:

1. Clone this repository to your local machine using your preferred method.
   
2. Navigate to the cloned directory.

3. add your openai_api into environment variable

4. Execute `main.py`:
   ```shell
   python main.py
   ```

The tests will run automatically, and the LLM's performance in identifying deadlocks and resource contentions will be evaluated.

## Requirements

- Python 3.x

Ensure you have the latest version of Python installed on your system to run the tests without any issues.

## Contributing

We welcome contributions and suggestions! If you have ideas on how to improve the tests or the detection algorithms, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

For any additional questions or feedback, feel free to open an issue in this repository.
