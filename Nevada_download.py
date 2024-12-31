"""
File Name: Nevada_download.py
Author: Qifeng He
Time: 2024/12/25 15:31
"""
import requests
import os
import argparse


def download_station_data(station_name, ref_base):
    url = f"http://geodesy.unr.edu/gps_timeseries/tenv3/plates/{ref_base}/" + f"{station_name}.{ref_base}.tenv3"
    print(url)
    response = requests.get(url)
    
    if response.status_code == 200:
        # 确保 data 文件夹存在
        if not os.path.exists("data"):
            os.makedirs("data")
        
        file_path = os.path.join("data", f"{station_name}.{ref_base}.tenv3")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {station_name}.tenv3 to {file_path}")
    else:
        print(f"Failed to download {station_name}.tenv3, status code {response.status_code}")


def download_all_station_data(file_path, ref_base):
    with open(file_path, "r") as f:
        stations = f.readlines()
        stations = [station.strip() for station in stations]
        for station in stations:
            download_station_data(station, ref_base)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download station data from Nevada Geodetic Laboratory")
    parser.add_argument("file_path", type=str, help="Path to the file containing station names")
    parser.add_argument("ref_base", type=str, help="Reference frame base")
    args = parser.parse_args()
    
    download_all_station_data(args.file_path, args.ref_base)
