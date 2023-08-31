import time
import serial
import random

COM_PORT = None  # You should write your port
BAUD_RATE = 9600  # You should write appropriate baud_rate
input_range = [0, 3.3]


def measure_voltage(nplc: int):
    voltages = []
    for _ in range(nplc):
        """Here we need to send commands to our measuring device via the COM port.
        For example:
        ser.write(b"VOLT:RANG 3.3\n")
        voltage = ser.write(b"READ?\n").readline().strip()
        However, since we don't know which specific device is being used,
        I've taken random values from our input_range."""
        voltage = random.uniform(input_range[0], input_range[1])
        voltages.append(voltage)
        time.sleep(1)
    return sum(voltages) / nplc


def main_script(nplc_settings: list[int]):
    try:
        ser = serial.Serial(COM_PORT, BAUD_RATE)  # Opening of the serial port

        for nplc in nplc_settings:
            res_voltage = measure_voltage(nplc)
            print(f"Measured voltage(NPLC={nplc}): {res_voltage}V")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        ser.close()  # Closing of the serial port


if __name__ == "__main__":
    NPLC = [1, 5, 10]
    main_script(NPLC)
