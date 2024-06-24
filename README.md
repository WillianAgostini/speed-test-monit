
# Speed Test Monitor

Speed Test Monitor is a Python-based application designed to monitor internet speed by periodically running speed tests and logging the results.

## Features

- Runs periodic internet speed tests.
- Logs download, upload speeds, and ping times.
- Generates reports for internet speed over time.

## Requirements

- Python 3.x
- Required packages listed in `requirements.txt`

## Installation

### Local Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/WillianAgostini/speed-test-monit.git
    ```
2. Navigate to the project directory:
    ```sh
    cd speed-test-monit
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Docker Installation

1. Build the Docker image:
    ```sh
    docker build -t speed-test-monit .
    ```

2. Run the Docker container with a custom time interval (e.g., every 30 minutes):
    ```sh
    docker run -v $(pwd)/speedtest_results:/app/speedtest_results speed-test-monit python src/main.py -t 30
    ```

## Usage

To start monitoring the internet speed with a local installation, run the main script:
```sh
python src/main.py -t 60  # Default is 60 minutes if no -t parameter is provided
```

## Releases

Releases for Windows and Linux can be found in the [Releases](https://github.com/WillianAgostini/speed-test-monit/releases) section.

## Speedtest CLI

This project utilizes [SPEEDTEST® CLI](https://www.speedtest.net/apps/cli) to execute the speed tests. For more information, visit the [Speedtest website](https://www.speedtest.net/).

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Contact

For questions or suggestions, please open an issue in this repository.
