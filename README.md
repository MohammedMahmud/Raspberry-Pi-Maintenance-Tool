# RaspberryPi-Maintenance- Terminal Tool (Linux)

This script basically updates & upgrades the existing packages in your Raspberry Pi and auto remove old packages and also auto clean it.

## Getting Started
Clone the directory to your PI desktop or any folder.
to clone this directory copy & paste in this your Terminal
```
git clone
```

### Installing
**** Make sure you already have Python 3.7.0 or above **** 
(cd == change directory)
cd to your directory.

* This will Immediately start updating and upgrading your packages
```
python3 PI_Maintenance.py -now
```

For HELP Type:
```
python3 PI_Maintenance.py --help
```
![Screenshot - Help](help.png)

## Built With -- Module

* [Python](https://www.python.org) - A high-level programming language
* [Datetime](https://docs.python.org/3.7/library/datetime.html) - This Module for Basic date and time.
* [Argparse](https://docs.python.org/3/library/argparse.html) - This Module for Parser for command-line options, arguments and sub-commands
* [Subprocess](https://docs.python.org/3/library/subprocess.html) - This Module for Subprocess management.
* [os](https://docs.python.org/3/library/os.html) - This module provides a portable way of using operating system dependent functionality.


## Authors

* **Mohammed Mahmud** - *Initial work* - [Mohammed Mahmud](https://github.com/MohammedMahmud)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
