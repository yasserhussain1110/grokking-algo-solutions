def find_biggest_station(current_states, radio_stations):
    biggest_station = None
    number_of_states = 0
    for (station, states) in radio_stations.items():
        covered_states = current_states & states
        if len(covered_states) > number_of_states:
            number_of_states = len(covered_states)
            biggest_station = station
    return biggest_station


def radio_stations(states, radio_stations):
    stations = set()
    while radio_stations:
        biggest = find_biggest_station(states, radio_stations)
        stations.add(biggest)
        states = states - radio_stations[biggest]
        del radio_stations[biggest]
        if not states:
            return stations
    return None


print(radio_stations({"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}, {
    "kone": {"id", "nv", "ut"},
    "ktwo": {"wa", "id", "mt"},
    "kthree": {"or", "nv", "ca"},
    "kfour": {"nv", "ut"},
    "kfive": {"ca", "az"}
}))
