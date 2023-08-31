import numpy


def main(array: list):
    data = numpy.array(array)

    num_dict = {num: array.count(num) for num in data}
    max_value = max(num_dict.values())
    if max_value > 1:
        mode = [key for key, value in num_dict.items() if value == max_value]
    else:
        mode = "There is no mode in array"

    print(f"Mean: {data.mean()}")
    print(f"Median: {numpy.median(data)}")
    print(f"Mode: {mode}")
    print(f"Standard deviation: {numpy.std(data)}")


if __name__ == '__main__':
    data_set = [364, 373, 358, 394, 378, 379, 357, 364, 350, 363, 392, 368, 359, 375, 399, 365, 379, 357, 380]
    main(data_set)
