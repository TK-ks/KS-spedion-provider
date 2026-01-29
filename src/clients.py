import datetime

from src.spedion_client_soap import SpedionSoapClient


class VehicleInfo_Client(SpedionSoapClient):
    WSDL_URL = (
        'https://services.spedion.de/CustomerVehicleInfoExtern/5/'
        'CustomerVehicleInfoExtern.asmx?WSDL'
    )

    def get_truck_info_for_period(
            self,
            vehicleName: int,
            startDate: datetime.datetime | str,
            endDate: datetime.datetime | str = datetime.datetime.now(datetime.UTC)
    ):
        """
        Calls the Spedion SOAP API to fetch all the messages for the period for a given vehicle.
        Info contains Telemetry, Time, MessageType (Form), Truck's position, and Driver Info.
        Example call {
            vehicleName=1013,
            startDate=datetime.date.today() - datetime.timedelta(minutes=55),
            endDate=datetime.datetime(2026, 01, 10, 16, 30, 01)
        }

        :type startDate: datetime.datetime | str
        :type endDate: optional - datetime.datetime | str
        :return: List of JSON objects. Contains all Spedion messages for the period.
        """
        data = self._do_request(self.service.GetVehicleMessagesByVehicleName,
            vehicleName=vehicleName,
            startDate=startDate,
            endDate=endDate
        )
        return data
