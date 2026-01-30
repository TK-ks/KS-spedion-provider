# Spedion GPS / Status data fetcher

## Usage:
```
python gps_data_fetcher.py 
  [vehicle_number]:<int>
  [start_time]:<str>            - Start time in format "2026-01-01"'
  -et [end_time OPTIONAL]:<str> - End time in format "2026-01-21", OPTIONAL, if none is specified datetime.today(UTC) will be used'
  -d [add_driver_data]          - include driver`s info, default=True'
  -p [add_position_extra]       - include extra positional data (like coutry, city and street), default=True'
  -ts [add_timestamp]           - include time, default=True'
  -tm [add_telematics]          - include telematics data (fuel %, speed, etc.), default=True'
```