#州的集合
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

#散列表表示广播台覆盖的州的集合
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

#最终选择的广播台
final_stations = set()

while states_needed:
    #选择好的广播台和它覆盖的州
    best_station = None
    states_covered = set()

    for station,states_for_station in stations.items():
        covered = states_needed & states_for_station

        if len(covered) > len(states_covered):
            best_station = station
            states_covered = states_for_station
            
    final_stations.add(best_station)

    states_needed -= states_covered

print(final_stations)
