"""
Flatland is a country with a number of cities, some of which have train stations. Cities are 
numbered consecutively and each has a road of 1km length connecting it to the next city. 
It is not a circular route, so the first city doesn't connect with the last city. Determine 
the maximum distance from any city to its nearest train station.

Notes:
- Cities are indexed from 0.
- Number of cities is between 1 and 10000.
- Number of cities with train station is between 1 and number of cities.
- No city has more than one train station.

Example:

number_of_cities == 3
cities_with_train_station == [1]

There are 3 cities and city #1 has a train station. They occur consecutively along a route. 
City #0 is 1km away, city #1 is 0km away and city #2 is 1km away from its nearest train station.
The maximum distance is 1.

"""

from typing import List


def find_maximum_distance(
    number_of_cities: int, cities_with_train_station: List[int]
) -> int:
    if number_of_cities < 1 or number_of_cities > 10000:
        raise ValueError("Number of cities should be between 1 and 10000")
    if max(cities_with_train_station) >= number_of_cities:
        raise ValueError(f"City {max(cities_with_train_station)} is out of range")

    city_with_train_station_passed = False
    distance = 0
    max_dist = 0
    for i in range(number_of_cities):
        if i in cities_with_train_station:
            if city_with_train_station_passed:
                distance += 1
                distance_to_city_between_stations = int(distance // 2)
                if max_dist < distance_to_city_between_stations:
                    max_dist = distance_to_city_between_stations
                distance = 0
            else:
                max_dist = distance
                distance = 0
                city_with_train_station_passed = True
        # Last city without train station
        elif i + 1 == number_of_cities:
            distance += 1
            if max_dist < distance:
                max_dist = distance
        # City without train station
        else:
            distance += 1

    return max_dist


if __name__ == "__main__":
    # These are some of test cases. When evaluating the task, more will be added:
    assert find_maximum_distance(number_of_cities=3, cities_with_train_station=[1]) == 1
    assert find_maximum_distance(number_of_cities=4, cities_with_train_station=[3]) == 3
    assert (
        find_maximum_distance(number_of_cities=5, cities_with_train_station=[0, 4]) == 2
    )
    print("ALL TESTS PASSED")
