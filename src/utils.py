from typing import List, OrderedDict
import sys
from types import ModuleType, FunctionType
from gc import get_referents


def decouple_data(
        vehicle_messages_data: List[OrderedDict],
        vehicle_name: int,
        no_driver_data: bool = False,
        no_position_extra: bool = False,
        no_timestamp: bool = False,
        no_telematics: bool = False
):

    if not vehicle_messages_data:
        return None
    if no_driver_data and no_position_extra and no_telematics and no_timestamp:
        return None

    result = {}
    clean_data = []
    driver_data = {}

    if no_driver_data:
        # If we filter out driver's data from each message - we store it on a 0-depth layer
        driver_data = {
            'VehicleName': vehicle_name,
            'Id': vehicle_messages_data[0]['Id'],
            'DriverId': vehicle_messages_data[0]['DriverId'],
            'DriverExternal': vehicle_messages_data[0]['DriverExternal']
        }
        result['driver_data'] = driver_data

    for d in vehicle_messages_data:
        if not (no_timestamp or no_telematics or no_position_extra):
            all_data = dict(d)

            # Filter out repeating driver data, leaving changed data
            if no_driver_data:
                check_fields = ['DriverExternal', 'DriverId', 'Id']
                is_same = True
                for f in check_fields:
                    if all_data.get(f) != driver_data.get(f):
                        is_same = False
                        break
                if is_same:
                    del all_data['DriverExternal']
                    del all_data['DriverId']
                    del all_data['Id']
            clean_data.append(all_data)
            continue

        data = {}
        if not no_timestamp:
            data['Time'] = str(d['Time'])

        if not no_telematics:
            data['TelematicData'] = d['TelematicData']

        data['Position'] = d['Position'] \
            if not no_position_extra \
            else {
                'Latitude': d['Position']['Latitude'],
                'Longitude': d['Position']['Longitude']
            }
        clean_data.append(data)

    result['messages_data'] = clean_data
    return result


# Custom objects know their class.
# Function objects seem to know way too much, including modules.
# Exclude modules as well.
BLACKLIST = type, ModuleType, FunctionType


def getsize(obj):
    """sum size of object & members."""
    if isinstance(obj, BLACKLIST):
        raise TypeError('getsize() does not take argument of type: ' + str(type(obj)))
    seen_ids = set()
    size = 0
    objects = [obj]
    while objects:
        need_referents = []
        for obj in objects:
            if not isinstance(obj, BLACKLIST) and id(obj) not in seen_ids:
                seen_ids.add(id(obj))
                size += sys.getsizeof(obj)
                need_referents.append(obj)
        objects = get_referents(*need_referents)
    return size
