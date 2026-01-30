import argparse
import datetime
import json
import sys

from src.clients import VehicleInfo_Client
from src.utils import decouple_data

parser = argparse.ArgumentParser(
    prog='ProgramName',
    description='What the program does',
    epilog='Text at the bottom of help'
)

parser.add_argument('vehicle_number',    required=True,  help='Vehicle number')
parser.add_argument('start_time',        required=True,  help='Starting datetime of the selection')
parser.add_argument('-et', '--end_time', required=False, help='End datetime of the selection')
# Mutators
parser.add_argument('-dd',   '--no_driver_data',    default=False, action='store_true')
parser.add_argument('-pos',  '--no_position_extra', default=False, action='store_true')
parser.add_argument('-time', '--no_timestamp',      default=False, action='store_true')
parser.add_argument('-tele', '--no_telematics',     default=False, action='store_true')

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
          '\n\t[start_time]:<str>       - Start time in format "2026-01-01"'
          '\n\t-et [end_time]:<str>     - End time in format "2026-01-21", OPTIONAL, if none is specified datetime.today(UTC) will be used'
          '\n\t-dd [no_driver_data]     - exclude driver`s info, default=True'
          '\n\t-pos [no_position_extra] - exclude extra positional data (like coutry, city and street), default=True'
          '\n\t-time [no_timestamp]     - exclude time, default=True'
          '\n\t-tele [no_telematics]    - exclude telematics data (fuel %, speed, etc.), default=True'
    )
    sys.exit(1)


def __main__():
    data = VehicleInfo_Client().get_truck_info_for_period(
        vehicleName=vehicleName,
        startDate=start_time,
        endDate=end_time
    )

    data = decouple_data(
        data,
        vehicleName,
        no_driver_data=args.no_driver_data,
        no_position_extra=args.no_position_extra,
        no_telematics=args.no_telematics,
        no_timestamp=args.no_timestamp
    )
    try:
        clean_data = json.dumps(data)
        print(clean_data)
        return clean_data
    except Exception as e:
        print(str(e))
        sys.exit(2)




__main__()

...
