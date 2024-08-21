# pip install pyserial
import serial.tools.list_ports
import sys

ports = serial.tools.list_ports.comports()

portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))
# Prompt user to select COM port
com = input("Select Com Port fo Arduino #: ")

use = None

for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(f"Using {use}")
        break

if use is None:
    print("Error: Selected Com Port not found.")
    sys.exit()

serialInst = serial.Serial()

serialInst.baudrate = 9600
serialInst.port = use


try:
    serialInst.open()
except Exception as e:
    print(f"Error: Could not open {use}. {e}")
    sys.exit()



while True:
    command = input("Arduino Command (ON/OFF/exit): ")

    if command.lower() == "exit":
        print("Existing...")
        serialInst.close()
        sys.exit()

    try:
        serialInst.write(command.encode('utf-8'))
    except Exception as e:
        print(f"Error: Could not write {command}. {e}")
