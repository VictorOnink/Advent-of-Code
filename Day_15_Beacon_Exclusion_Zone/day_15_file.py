from typing import List, Tuple, Set
from parse import compile
from tqdm import tqdm

Coordinate = Tuple[int]
SensorBeaconCoordinates = List[List[Coordinate]]
SensorCoverage = Set[Coordinate]
SensorSearchRadii = List[int]


def load_puzzle_input(case: str) -> SensorBeaconCoordinates:
    if case == "puzzle":
        file_name = "Day_15_Beacon_Exclusion_Zone/puzzle_input.txt"
    else:
        file_name = "Day_15_Beacon_Exclusion_Zone/test_input.txt"
    with open(file_name) as f:
        lines = [x.strip() for x in f.readlines()]
    input_schema = compile("Sensor at x={}, y={}: closest beacon is at x={}, y={}")
    sensor_coordinates = []
    for line in lines:
        values = [int(x) for x in input_schema.parse(line)]
        sensor_coordinates.append([(values[0], values[1]), (values[2], values[3])])
    return sensor_coordinates


def manhattan_distance(point_a: Coordinate, point_b: Coordinate) -> int:
    return sum(abs(point_a[i] - point_b[i]) for i in range(2))


def get_search_radii(sensor_coordinates: SensorBeaconCoordinates) -> SensorSearchRadii:
    sensor_beacon_distance: SensorSearchRadii = []
    for sensor in sensor_coordinates:
        start, beacon = sensor
        sensor_beacon_distance.append(manhattan_distance(start, beacon))
    return sensor_beacon_distance


def coverage_in_target_line(
    sensor_coordinates: SensorBeaconCoordinates,
    sensor_search_radii: SensorSearchRadii,
    target_line: int,
) -> None:
    coverage_target_line: List[Coordinate] = []

    for sensor_index in range(len(sensor_coordinates)):
        start, _ = sensor_coordinates[sensor_index]
        search_radius: int = sensor_search_radii[sensor_index]

        diff_y: int = abs(target_line - start[1])

        if diff_y <= search_radius:
            span_x: int = search_radius - diff_y
            range_x = range(-span_x, span_x + 1)
            for x in range_x:
                coverage_target_line.append((start[0] + x, target_line))

    coverage_target_line: Set[Coordinate] = set(coverage_target_line)

    print(f"We have {len(coverage_target_line) - 1} points covered for {target_line=}")


def get_distress_beacon(
    sensor_coordinates: SensorBeaconCoordinates,
    sensor_search_radii: SensorSearchRadii,
    search_domain: int,
) -> Coordinate:

    for sensor_index, sensor in tqdm(enumerate(sensor_coordinates)):
        sensor_x, sensor_y = sensor[0]
        sensor_search_radius = sensor_search_radii[sensor_index]
        for point_x in range(
            max(0, sensor_x - sensor_search_radius - 1),
            min(search_domain + 1, sensor_x + sensor_search_radius + 2),
        ):
            diff_x: int = abs(point_x - sensor_x)

            possible_y_plus: int = sensor_y + (sensor_search_radius - diff_x) + 1
            possible_y_minus: int = sensor_y - (sensor_search_radius - diff_x) - 1

            for point_y in [possible_y_plus, possible_y_minus]:
                if point_y in range(0, search_domain + 1):
                    in_other_range = False
                    point: Coordinate = (point_x, point_y)

                    for other_sensor_index, other_sensor in enumerate(
                        sensor_coordinates
                    ):
                        if (
                            manhattan_distance(point, other_sensor[0])
                            <= sensor_search_radii[other_sensor_index]
                        ):
                            in_other_range = True
                            break
                    if not in_other_range:
                        return point


if __name__ == "__main__":
    case = "puzzle"
    target_line = {"test": 10, "puzzle": 2_000_000}[case]
    search_domain = {"test": 20, "puzzle": 4_000_000}[case]

    sensor_coordinates: SensorBeaconCoordinates = load_puzzle_input(case)

    sensor_search_radii: SensorSearchRadii = get_search_radii(sensor_coordinates)

    coverage_in_target_line(sensor_coordinates, sensor_search_radii, target_line)

    distress_beacon: Coordinate = get_distress_beacon(
        sensor_coordinates, sensor_search_radii, search_domain
    )

    print(
        f"The tuning frequency is {distress_beacon[0] * 4_000_000 + distress_beacon[1]}."
    )
