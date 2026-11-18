#!/usr/bin/env python3

import sys
import time
import requests

REQUEST_COUNT = 10


def format_size(bytes_count):
    for unit in ['B', 'KiB', 'MiB', 'GiB']:
        if bytes_count < 1024:
            return f"{bytes_count:.2f} {unit}"
        bytes_count /= 1024
    return f"{bytes_count:.2f} TiB"


def format_speed(bytes_per_second):
    for unit in ['B/s', 'KiB/s', 'MiB/s', 'GiB/s']:
        if bytes_per_second < 1024:
            return f"{bytes_per_second:.2f} {unit}"
        bytes_per_second /= 1024
    return f"{bytes_per_second:.2f} TiB/s"


def measure_speed(url):
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    print(f"Testing URL: {url}")
    print(f"Making {REQUEST_COUNT} sequential requests...\n")
    
    request_times = []
    total_bytes = 0
    
    for i in range(REQUEST_COUNT):
        try:
            start_time = time.perf_counter()
            content_size = 0
            with requests.get(url, stream=True, timeout=30) as response:
                response.raise_for_status()
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        content_size += len(chunk)
            end_time = time.perf_counter()
            
            request_time = end_time - start_time
            
            request_times.append(request_time)
            total_bytes += content_size
            
            print(f"Request {i + 1}: {request_time:.3f}s ({format_size(content_size)})")
            
        except requests.RequestException as e:
            print(f"Request {i + 1} failed: {e}")
            return None
    
    print()
    
    average_time = sum(request_times) / REQUEST_COUNT
    total_time = sum(request_times)
    average_bytes = total_bytes / REQUEST_COUNT
    download_speed = total_bytes / total_time if total_time > 0 else 0
    
    results = {
        'url': url,
        'num_requests': REQUEST_COUNT,
        'total_bytes': total_bytes,
        'total_time': total_time,
        'average_time': average_time,
        'average_bytes': average_bytes,
        'download_speed': download_speed,
    }
    
    return results


def print_results(results):
    if results is None:
        print("Failed to measure speed.")
        return
    
    print("=" * 60)
    print("SPEED TEST RESULTS")
    print("=" * 60)
    print(f"URL: {results['url']}")
    print(f"Number of requests: {results['num_requests']}")
    print(f"Total data downloaded: {format_size(results['total_bytes'])}")
    print(f"Total time: {results['total_time']:.3f} seconds")
    print(f"Average request time: {results['average_time']:.3f} seconds")
    print(f"Average download size: {format_size(results['average_bytes'])}")
    print("-" * 60)
    print(f"Download speed: {format_speed(results['download_speed'])}")
    print("=" * 60)


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <url>")
        print("Example: python main.py https://example.com/largefile.jpg")
        print("Example: python main.py example.com/image.png")
        sys.exit(1)
    
    url = sys.argv[1]
    results = measure_speed(url)
    print_results(results)
    if results is None:
        sys.exit(1)


if __name__ == '__main__':
    main()
