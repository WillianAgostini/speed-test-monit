import json
import speedtest
from datetime import datetime
import os
import time
import argparse
import threading

def run_speedtest():
    threads = None
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download(threads=threads)
    s.upload(threads=threads)
    s.results.share()
    results = s.results.dict()
    
    if 'share' in results:
        results['url'] = results['share'].replace('.png', '')
        
    results['downloadMbps'] = round(results['download'] / 1_000_000, 2)
    results['uploadMbps'] = round(results['upload'] / 1_000_000, 2)
    return results

def save_results_to_json(results):
    results_dir = "speedtest_results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    now = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
    filename = os.path.join(results_dir, f"{now}.json")
    with open(filename, 'w') as json_file:
        json.dump(results, json_file, indent=4)
    return filename

def execute():
    now = datetime.now().strftime("%H:%M:%S")
    print(f"Execution started at {now}")

    results = run_speedtest()
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
