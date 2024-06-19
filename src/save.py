import csv
import json
from datetime import datetime, timedelta, timezone
import os

def save_results_to_json(results):
    results_dir = "speedtest_results"
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    
    now = datetime.now().strftime("%Y-%m-%d_at_%H-%M-%S")
    filename = os.path.join(results_dir, f"{now}.json")
    with open(filename, 'w') as json_file:
        json.dump(results, json_file, indent=4)
    return filename

def convert_timestamp(timestamp_str):
    timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
    gmt3 = timestamp - timedelta(hours=3)
    return gmt3.strftime('%Y-%m-%d %H:%M:%S')

def save_results_to_csv(results, filename='speedtest_results.csv'):
    headers = [
        'timestamp', 'downloadMbps', 'uploadMbps', 'ping', 'url',
        'server.name', 'server.latency', 'client.ip', 'client.isp',
        'download', 'upload', 'bytes_sent', 'bytes_received', 'server.url',
        'server.lat', 'server.lon', 'server.country', 'server.cc',
        'server.sponsor', 'server.id', 'server.host', 'server.d',
        'client.lat', 'client.lon', 'client.isprating', 'client.rating',
        'client.ispdlavg', 'client.ispulavg', 'client.loggedin',
        'client.country'
    ]

    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        if not file_exists:
            writer.writeheader()
        
        results['timestamp'] = convert_timestamp(results['timestamp'])
        
        writer.writerow({
            'timestamp': results['timestamp'],
            'downloadMbps': results['downloadMbps'],
            'uploadMbps': results['uploadMbps'],
            'ping': results['ping'],
            'url': results['url'],
            'server.name': results['server']['name'],
            'server.latency': results['server']['latency'],
            'client.ip': results['client']['ip'],
            'client.isp': results['client']['isp'],
            'download': results['download'],
            'upload': results['upload'],
            'bytes_sent': results['bytes_sent'],
            'bytes_received': results['bytes_received'],
            'server.url': results['server']['url'],
            'server.lat': results['server']['lat'],
            'server.lon': results['server']['lon'],
            'server.country': results['server']['country'],
            'server.cc': results['server']['cc'],
            'server.sponsor': results['server']['sponsor'],
            'server.id': results['server']['id'],
            'server.host': results['server']['host'],
            'server.d': results['server']['d'],
            'client.lat': results['client']['lat'],
            'client.lon': results['client']['lon'],
            'client.isprating': results['client']['isprating'],
            'client.rating': results['client']['rating'],
            'client.ispdlavg': results['client']['ispdlavg'],
            'client.ispulavg': results['client']['ispulavg'],
            'client.loggedin': results['client']['loggedin'],
            'client.country': results['client']['country']
        })
