# Spedion GPS / Status data fetcher

## Usage:
```
python gps_data_fetcher.py 
  [vehicle_number]:<int>
  [start_time]:<str>            - Start time in format "2026-01-01"'
  -et [end_time OPTIONAL]:<str> - End time in format "2026-01-21", OPTIONAL, if none is specified datetime.today(UTC) will be used'
  -gps [OPTIONAL]               - Optional flag for returning GPS data only'`
```