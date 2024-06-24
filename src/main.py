import speedtest
from datetime import datetime
import time
import argparse
from save import save_results_to_csv, save_results_to_json
from thread_execution_state_controller import create_system_activity_controller

config = None

def getSpeedTest():
    global config
    try:
        s = speedtest.Speedtest()
        config = s.get_config()
        return s
    except:
        return speedtest.Speedtest(config=config)

def run_speedtest():
    s = getSpeedTest()
    s.get_best_server()
    s.download(threads=None)
    s.upload(threads=None)
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
    system_activity_controller = create_system_activity_controller()
    while True:
        system_activity_controller.keep_system_active()
        try:
            execute()
            time.sleep(interval)
        except KeyboardInterrupt:
            print("Execution interrupted by user.")
            break
        except Exception as e:
            time.sleep(10)
            print(f"An error occurred: {e}")


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
