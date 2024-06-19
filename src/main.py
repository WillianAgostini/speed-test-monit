import speedtest
from datetime import datetime
import time
import argparse
import threading
from save import save_results_to_csv, save_results_to_json


def run_speedtest():
    threads = None
    s = speedtest.Speedtest()
    s.get_servers()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()
    results = s.results.dict()
    
    if 'share' in results:
        results['url'] = results['share'].replace('.png', '')
        
    results['downloadMbps'] = round(results['download'] / 1_000_000, 2)
    results['uploadMbps'] = round(results['upload'] / 1_000_000, 2)
    return results

def execute():
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Execution started at {now}")

    results = run_speedtest()
    save_results_to_csv(results)
    filename = save_results_to_json(results)
    
    print(f"url: {results.get('url')}")
    print(f"downloadMbps: {results.get('downloadMbps')}")
    print(f"uploadMbps: {results.get('uploadMbps')}")
    print(f"Results saved to {filename}")
    print("-" * 10)

def main(interval):
    while True:
        try:
            thread = threading.Thread(target=execute)
            thread.start()
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run speedtest at regular intervals.")
    parser.add_argument(
        "-t", "--time", 
        type=int, 
        default=60, 
        help="Time in minutes between each speedtest execution"
    )
    args = parser.parse_args()
    interval = args.time * 60  # Convert minutes to seconds
    print(f"Loop interval set to {args.time} minutes.")
    main(interval)
