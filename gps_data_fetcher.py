import argparse
import datetime
import json

from src.clients import VehicleInfo_Client
from src.utils import decouple_data


parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help'
)

parser.add_argument('vehicle_number')
parser.add_argument('start_time')
parser.add_argument('-et', '--end_time')
parser.add_argument('-gps', '--gps_only', default=False, action='store_true')

args = parser.parse_args()

try:
    vehicleName = int(args.vehicle_number)
    start_time = datetime.datetime.fromisoformat(args.start_time)
    end_time = datetime.datetime.fromisoformat(args.end_time) \
        if args.end_time \
        else datetime.datetime.now(datetime.UTC)
except ValueError as e:
    print(str(e))
    print('Usage: python gps_data_fetcher.py '
          '\n\t[vehicle_number]:<int> '
          '\n\t[start_time]:<str>   - Start time in format "2026-01-01"'
          '\n\t-et [end_time]:<str> - End time in format "2026-01-21", OPTIONAL, if none is specified datetime.today(UTC) will be used'
          '\n\t-gps [OPTIONAL]      - Optional flag for returning GPS data only'
    )
    exit(1)


def __main__():
    data = VehicleInfo_Client().get_truck_info_for_period(
        vehicleName=vehicleName,
        startDate=start_time,
        endDate=end_time
    )
    clean_data = json.dumps(decouple_data(data, vehicleName, gps_only=args.gps_only))
    print(clean_data)
    return clean_data

__main__()

...
