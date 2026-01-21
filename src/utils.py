from typing import List, OrderedDict, Any
import sys
from types import ModuleType, FunctionType
from gc import get_referents


def decouple_data(
        vehicle_messages_data: List[OrderedDict],
        vehicleName: int,
        gps_only: bool
) -> dict[str, list[Any] | dict[str, int | Any]] | None:
    """

    :param gps_only:
    :param vehicle_messages_data:
    :param vehicleName:
    :param gps_only:
    :return:
    """
    if not vehicle_messages_data:
        return None

    clean_data = []
    for d in vehicle_messages_data:
        data_dict = {
            'Time': str(d['Time']),
            'Position': dict(d['Position'])
        }
        if not gps_only:
            data_dict = {
                **data_dict,
                'TelematicData': dict(d['TelematicData']),
                'Form': d['Form'],
                'FormDescription': d['FormDescription']
            }
        clean_data.append(data_dict)

    if gps_only:
        return {'gps_data': clean_data}

    return {
        'messages_data': clean_data,
        'driver_data': {
            'VehicleName': vehicleName,
            'Id': vehicle_messages_data[0]['Id'],
            'DriverId': vehicle_messages_data[0]['DriverId'],
            'DriverExternal': vehicle_messages_data[0]['DriverExternal']
        }
    }


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
