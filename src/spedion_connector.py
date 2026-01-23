from src.spedion_client_soap import SpedionSoapClient

TEST_VEHICLES_IDS = [
    1111,
    1112
]

TOUR_NR = 130514


# def get_tours_by_():
# tours = SpedionSoapClient().get_tour(tour_nr=TOUR_NR)
tour = SpedionSoapClient().get_tour_single(tour_nr=TOUR_NR)
v_data = SpedionSoapClient().get_vehicle_info()

...
