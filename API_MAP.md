## Spedion API map:

[SPEDION Interfaces](https://wiki.spedion.de/docs/en/spedion-schnittstellen):
- [SImpEx](https://simpex.spedion.de/simpex/3.1/Services/MessageService.asmx) - SPEDION Import / Export interface for bidirectional data exchange. Sending of free texts and tours. Collection of location, activity and tour status messages

    <details>
    
    <summary>WSDL 1 returns</summary>
    
    https://simpex.spedion.de/simpex/3.1/Services/MessageService.asmx?WSDL
    
  ```python
    'Tournr' = {str} '130514'
    'DriverPin' = {str} '5387'
    'State' = {int} 30
    'tours' = {OrderedDict: 16},
     'Tournr' = {str} '130514'
     'DriverPin' = {str} '5387'
     'State' = {int} 30
     'Places': {
         'Place': [
             0: {
                 'PlaceNr' = {str} 'order:130514, waypoint:83098',
                 'PlaceName' = {str} 'Dleteren',
                 'Address' = {str} 'Leuvenseeteenweg',
                 'Housenr' = {str} '639',
                 'Nation' = {str} 'BE',
                 'Zip' = {str} '3071',
                 'Location' = {str} 'Kortenberg',
                 'Orders': {
                     'Order': {
                         0: {
                             'AdditionalData' = {NoneType} None
                             'CommentToDispo' = {NoneType} None
                             'OrderNr' = {str} 'order:130514, waypoint:83098, type: loading, s_type: Load'
                             'Type' = {str} 'Load'
                             'ProductName' = {NoneType} None
                             'Amount' = {NoneType} None
                             'Amount2' = {NoneType} None
                             'Packing' = {NoneType} None
                             'Packing2' = {NoneType} None
                             'Weight' = {NoneType} None
                             'Hazard' = {NoneType} None
                             'Trailer' = {NoneType} None
                             'Container1' = {NoneType} None
                             'Container2' = {NoneType} None
                             'State' = {int} 100
                             'OrderNrExtern' = {NoneType} None
                             'DisplayAtPos' = {int} 0
                             'Name1' = {NoneType} None
                             'Name2' = {NoneType} None
                             'ArtNr' = {NoneType} None
                             'Charge' = {NoneType} None
                             'DeliveryNr' = {NoneType} None
                             'CommentFromDispo' = {NoneType} None
                             'LoadingMeter' = {NoneType} None
                             'PackingDescription' = {NoneType} None
                             'RefNr' = {NoneType} None
                             'Workflow' = {NoneType} None
                             'Attachment' = {NoneType} None
                             'AttachmentFromDispo' = {NoneType} None
                             'ExternalRefNr' = {NoneType} None
                         }
                     }
                 },
                 'CommentFromDispo' = {str} 'Leergut\nID: 45890\nскин документы от выгруски'
                 'CommentToDispo' = {NoneType} None
                 'Latitude' = {float} 0.0
                 'Longitude' = {float} 0.0
                 'DisplayAtPos' = {int} 1
                 'AdditionalData' = {
                     'Items' = {NoneType} None
                 },
                 'State' = {int} 100
                 'Workflow' = {NoneType} None
                 'PlanBeginUtc' = {datetime} datetime.datetime(2026, 1, 22, 6, 0, tzinfo=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>)
                 'PlanEndUtc' = {datetime} datetime.datetime(2026, 1, 22, 6, 10, tzinfo=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>)
                 'Attachment' = {OrderedDict: 3} OrderedDict({'UrlBased': None, 'Text': OrderedDict({'TextAttachment': [OrderedDict({'MetaData': OrderedDict({'WorkflowActionLa...o=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>)}), 'Value': 'Nein', 'Name': 'PalettentauschJaNein'})]}), 'Barcode': None})
                 'AttachmentFromDispo' = {NoneType} None
                 'ExternalRefNr' = {NoneType} None
         ]
     }                                                                                                                                                                                                                                                                             
     'PlaceNr' = {str} 'order:130514, waypoint:83098'
     'PlaceName' = {str} 'Dleteren'
     'Address' = {str} 'Leuvenseeteenweg'
     'Housenr' = {str} '639'
     'Nation' = {str} 'BE'
     'Zip' = {str} '3071'
     'Location' = {str} 'Kortenberg'
     'Orders' = {OrderedDict: 1} OrderedDict({'Order': [OrderedDict({'AdditionalData': None, 'CommentToDispo': None, 'OrderNr': 'order:130514, waypoint:83098, ...escription': None, 'RefNr': None, 'Workflow': None, 'Attachment': None, 'AttachmentFromDispo': None, 'ExternalRefNr': None})]})
     'CommentFromDispo' = {str} 'Leergut\nID: 45890\nскин документы от выгруски'
     'CommentToDispo' = {NoneType} None
     'Latitude' = {float} 0.0
     'Longitude' = {float} 0.0
     'DisplayAtPos' = {int} 1
     'AdditionalData' = {OrderedDict: 1} OrderedDict({'Items': None})
     'State' = {int} 100
     'Workflow' = {NoneType} None
     'PlanBeginUtc' = {datetime} datetime.datetime(2026, 1, 22, 6, 0, tzinfo=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>)
     'PlanEndUtc' = {datetime} datetime.datetime(2026, 1, 22, 6, 10, tzinfo=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>)
     'Attachment' = {OrderedDict: 3} OrderedDict({'UrlBased': None, 'Text': OrderedDict({'TextAttachment': [OrderedDict({'MetaData': OrderedDict({'WorkflowActionLa...o=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>)}), 'Value': 'Nein', 'Name': 'PalettentauschJaNein'})]}), 'Barcode': None})
     'AttachmentFromDispo' = {NoneType} None
     'ExternalRefNr' = {NoneType} None
     __len__ = {int} 21
         1 = {OrderedDict: 21} OrderedDict({'PlaceNr': 'order:130514, waypoint:83099', 'PlaceName': 'Volkswagen AG/ OTC 3', 'Address': 'Zwickauer Straße', 'H...fo=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>), 'Attachment': None, 'AttachmentFromDispo': None, 'ExternalRefNr': None})
     'PlaceNr' = {str} 'order:130514, waypoint:83099'
     'PlaceName' = {str} 'Volkswagen AG/ OTC 3'
     'Address' = {str} 'Zwickauer Straße'
     'Housenr' = {str} '15'
     'Nation' = {str} 'DE'
     'Zip' = {str} '34225'
     'Location' = {str} 'Baunatal'
     'Orders' = {OrderedDict: 1} OrderedDict({'Order': [OrderedDict({'AdditionalData': None, 'CommentToDispo': None, 'OrderNr': 'order:130514, waypoint:83099, ...escription': None, 'RefNr': None, 'Workflow': None, 'Attachment': None, 'AttachmentFromDispo': None, 'ExternalRefNr': None})]})
     'CommentFromDispo' = {str} 'OTC 3'
     'CommentToDispo' = {NoneType} None
     'Latitude' = {float} 0.0
     'Longitude' = {float} 0.0
     'DisplayAtPos' = {int} 2
     'AdditionalData' = {OrderedDict: 1} OrderedDict({'Items': None})
     'State' = {int} 40
     'Workflow' = {NoneType} None
     'PlanBeginUtc' = {datetime} datetime.datetime(2026, 1, 22, 7, 0, tzinfo=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>)
     'PlanEndUtc' = {datetime} datetime.datetime(2026, 1, 22, 7, 10, tzinfo=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>)
     'Attachment' = {NoneType} None
     'AttachmentFromDispo' = {NoneType} None
     'ExternalRefNr' = {NoneType} None
     __len__ = {int} 21
  
    'AdditionalData' = {
     OrderedDict: 1}
     OrderedDict(
         {
             'Items': OrderedDict({
                 'AdditionalValueItem': [
                     OrderedDict({
                         'Value': '5830.0',
                         'Key': 'AxleWeight1'
                     }),
                     OrderedDict...B'}), OrderedDict({'Value': '73629', 'Key': 'VehicleID'}), OrderedDict({'Value': '28.6', 'Key': 'VoltageExternalBattery'})]})})
    'RequiredTrailer' = {NoneType} None
    'DisplayAtPos' = {int} 0
    'VehicleName' = {str} '548'
    'Workflow' = {NoneType} None
    'CommentFromDispo' = {NoneType} None
    'CommentToDispo' = {NoneType} None
    'TourBeginUtc' = {NoneType} None
    'TourEndUtc' = {NoneType} None
    'TourDateUtc' = {datetime} datetime.datetime(2026, 1, 21, 9, 36, 42, 203000, tzinfo=<isodate.tzinfo.Utc object at 0x000001D5680EEF90>)
    'Attachment' = {NoneType} None
    'AttachmentFromDispo' = {NoneType} None
    __len__ = {int} 16
  ```
    
    </details>
  
    - AbandonSubCustomerTourByTourNr
    - AbandonTourByTourNr
    - AddMessage
    - AddOrUpdateFromDispoAttachmentTo
    - AddRegistrationMessage
    - DeleteSubCustomerTour
    - DeleteTour
    - DeleteTourObject
    - GetCustomerTourForAllSubCustomersByTourNr
    - GetMessageCount
    - GetMessageId
    - GetNewMessage
    - GetPresignedUploadUrl
    - GetSingleTourInfoByTournr
      <details>
      
      <summary>Responses (JSON + XML)</summary>
      
      ```python
       OrderedDict({
           'Result': OrderedDict({
               'Code': 'OkCode',
               'Description': 'Webservice-Operation erfolgreich',
               'ErrorCode': 0, 'ErrorDesc': 'OkCode'
           }),
           'SingleTourLogin': OrderedDict({
               'TourNr': 'T53847654',
               'Pin': '319822',
               'Url': 'https://www.spedion.de/singletour/en/?tournr=T53847654&tourpin=319822'
           })
       })
        ```
        ```xml
       <SingleTourInfoResult>
         <Result>
           <Code>OkCode</Code>
           <Description>Webservice-Operation erfolgreich</Description>
           <ErrorCode>0</ErrorCode>
           <ErrorDesc>OkCode</ErrorDesc>
         </Result>
         <SingleTourLogin>
           <TourNr>T53847654</TourNr>
           <Pin>319822</Pin>
           <Url>
           https://www.spedion.de/singletour/en/?tournr=T53847654&tourpin=319822
           </Url>
         </SingleTourLogin>
       </SingleTourInfoResult>
      ```
    
      </details>

    - GetTourByTourNr
    - GetTourByTourNrOfCustomer
    - GetToursByExample
    - GetToursByOrderNrExtern
    - GetToursByOrderNrs
    - GetToursByPlaceNrs
    - GetToursBySubCustomerVehicle
    - GetToursByVehicle
    - GetToursByVehicleAndState
    - GetUnreadMessage
    - GetVersion
    - ParseIdentifierString
    - ParseIdentifierStringSubCustomer
    - RemoveFromDispoAttachmentFrom
    - ReportError
    - SetListOfMessageAsRead
    - UpdateSubCustomerTour
    - UpdateTour 
- [SPEDION Driving and rest times](https://services.spedion.de/DriveAndRestTimesExtern/1.9/DriveAndRestTimes.asmx) - Calling up calculated remaining driving and working times as well as driver tachograph activities.
  - GetDtcoAnalysisResult
  - GetDtcoAnalysisResultByDriverRequest
  - GetDtcoAnalysisResultWithActivities
  - GetDtcoAnalysisResultWithActivitiesByDriverRequest
  - GetDtcoAnalysisResultWithActivitiesByDriverRequestExtended
  - GetDtcoAnalysisResultWithActivitiesExtended
  - MaxDriversAllowed
  - MaxSecondsAccessAllowed
  - SelectDriverByExample
  - Version
- [SPEDION tachograph data](https://services.spedion.de/DTCODownloadWebservice/6/DTCODownloadService.asmx) - Retrieval of downloaded driver card and mass data (*.DDD files)
  - GetAllDTCOFiles
  - GetAvailableAllFilesCount
  - GetAvailableDriverFilesCount
  - GetAvailableVehicleFilesCount
  - GetCompanyCardInfo
  - GetDriverDTCOFiles
  - GetRdlFileCountForVehicleId
  - GetVehicleDTCOFiles
  - GetVersion
  - SetFileStatusAsRead 
- [Master data](https://services.spedion.de/StammdatenWsExtern/2.1/StammdatenWsExtern.asmx) - Create, edit and delete customers, drivers and vehicles as well as associated groups.
  - CompanyCardGroupByExample
  - CustomerAdd
  - CustomerByExample
  - CustomerDelete
  - CustomerUpdate
  - DriverAdd
  - DriverByExample
  - DriverDelete
  - DriverGroupAdd
  - DriverGroupByExample
  - DriverGroupDelete
  - DriverGroupUpdate
  - DriverUpdate
  - GetAvailableVehicleDeviceTypes
  - GetCustomerSubCategories
  - GetDriverAvailableLanguages
  - GetDriverAvailableNationalities
  - UserAdd
  - UserByExample
  - UserDelete
  - UserUpdate
  - VehicleAdd
  - VehicleByExample
  - VehicleDelete
  - VehicleDevicesByExample
  - VehicleGroupAdd
  - VehicleGroupByExample
  - VehicleGroupDelete
  - VehicleGroupUpdate
  - VehicleUpdate
  - Version
- [SPEDION ECO](https://services.spedion.de/EcoWsExtern/3.0/EcoWsExtern.asmx) - Retrieval of calculated ECO data.
  - GetAvailableLanguages
  - GetDriverList
  - GetEcoReportForAllDrivers
  - GetEcoReportForAllDriversAsExcel
  - GetEcoReportForAllVehicles
  - GetEcoReportForAllVehiclesAsExcel
  - GetEcoReportForDriver
  - GetEcoReportForDriverAsExcel
  - GetEcoReportForVehicle
  - GetEcoReportForVehicleAsExcel
  - GetVehicleList
  - GetVersion 
- [Last Position](https://services.spedion.de/LastPosition/) **REST** - Retrieve the last current vehicle position.
  - LastPositionForVehicleId
  - LastPositionForVehicleName
  - LastPositions
  - Version
- [File Webservice](https://services.spedion.de/FileWebservice/FileWebservice.asmx) - Retrieval of SPEDION reporting files.
  - AddFile
  - GetFiles
  - GetFilesByTypeString
  - GetFilesByTypeStringAndCompanyCard
  - SetFileStatus
  - Version
- [Vehicle Info](https://services.spedion.de/CustomerVehicleInfoExtern/5/CustomerVehicleInfoExtern.asmx) - Retrieve historical vehicle data.
  - GetVehicleCluster
  - GetVehicleClusterByVehicleName
  - GetVehicleFirstAndLastData
  - GetVehicleFirstAndLastDataByVehicleName
  - GetVehicleMessages
  - GetVehicleMessagesByVehicleName
  - GetVehicleMonthlyData
  - GetVehicleMonthlyDataByVehicleName
  - SelectAllDrivers
  - SelectAllVehicles
  - SelectDriverByExample
  - SelectVehicleByExample
  - Version
- [Information Exchange](https://services.spedion.de/InformationExchangeWS/1.0) **REST** - Sending free texts and documents.
  - Driver
  - PresignedAttachmentUploadUrl
  - SendInformation
  - Status

---

