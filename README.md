# Switch: Enable/Disable Hardware Devices

Switch is a simple tool to control hardware devices.

## Installation

Install the package using the following command:

```bash
$ sudo add-apt-repository ppa:sugarcoat/ppa
$ sudo apt update
$ sudo apt install switch
```

## Usage

To get the names of hardware devices, run:
```bash
$ xinput
```

Create a `config` file and include the names of the devices you want to enable or disable.
```python
[ENABLE]
devices = ["SynPS/2 Synaptics TouchPad", "Virtual core XTEST pointer"]

[DISABLE]
devices = ["ELAN Touchscreen"]
```

Execute the command for the changes to take effect:
```bash
$ switch /path/to/config
```
