# Humidity Cart Validation Program

## Contents
 1. [Summary](#summary)
 2. [Project Motivation](#motiv)
 3. [Hardware Requirements](#hard)
 4. [Software Requirements](#install)
 5. [Quick Start Guide](#use)
    - [Program Launch](#launch)
    - [Device Setup](#dsetup)
    - [Recording Setup](#ssetup)
    - [Set Airstream Conditions](#setac)
    - [Scan Systems](#scan)
    - [Data Recording](#rec)
 6. [Future Capabilities](#future)
 7. [Acknowledgements](#kudos)

## Summary <a name="summary"></a>
This program was generated for specific use at the NASA Glenn Research Center to allow for a direct comparison of humidity measurements between the SpectraSensors WVSS-II and LiCor Dew Point Generator (LI-610).

## Project Motivation <a name="motiv"></a>
The motivation for this project stems from the different data types transmitted from each unit. The WVSS-II streams an RS-232 serial connection with ppmV (parts per million by volume) native units while the LI-610 streams an analog 0-5 Volt signal directly corresponding to dew point temperature (°C). There was no direct means of data recording from the WVSS-II software and no software available for data collection with the LI-610 unit.

Additionally, the concept of allowing for side-by-side comparison of data as well as a scrolling data visualization limits the amount of data waste by making setup issues more noticeable during runtime. These features improve the overall experience and allow for a streamlined transition from one engineer to another.

## Hardware Requirements <a name="hard"></a>
This program utilizes very specific hardware in order to properly run. The following hardware must be utilized:
 - [SpectraSensors WVSS-II Atmospheric Water Vapor Sensing System](https://www.spectrasensors.com/wvss/)
 - [LI-COR LI-610 Portable Dew Point Generator](https://www.licor.com/env/products/gas_analysis/LI-610/)
 - [DataQ Instruments DI-145 Data Acquisition Analog to Digital USB Kit](https://www.dataq.com/resources/obsolete/products/di-145/) (may also work with the [DI-1100](https://www.dataq.com/products/di-1100/) but NOT tested)

## Software Requirements <a name="install"></a>
Required for use of this program:
 - [Python](https://www.python.org/downloads/) (>=3.4)
 - [pyserial](https://pypi.org/project/pyserial/)
 - [CoolProp](https://pypi.org/project/CoolProp/)
 - [Numpy](https://pypi.org/project/numpy/)
 - [Pandas](https://pypi.org/project/pandas/)

If modification is necessary:
 - [PyQt5](https://pypi.org/project/PyQt5/)
 - [PyQt5-tools](https://pypi.org/project/pyqt5-tools/)

## Quick Start Guide <a name="use"></a>
Before launching into the program, be sure the WVSS-II and LI-610 units are properly powered up and connected to the data acquisition terminal.  To connect each system, perform the following:<br><br>
**WVSS-II**: Connect the RS-232 cable from the WVSS-II unit to the computer and note the COM port.<br>
**LI-610**: Attach one end of the analog cable to the BNC connector on the LiCor unit, the other end into Ch1 of the DataQ A/D. Plug the USB into the PC and note the COM port.

For help determining which COM port is connected check out this [link](https://answers.microsoft.com/en-us/windows/forum/windows_10-hardware/how-to-identify-com-ports-in-windows10/2591ed8b-805e-4e66-9513-836cdd49ed80).

#### Program Launch<a name="launch"></a>
From the main directory of this project enter in the command line to access the program via a GUI

```
>> python RUN_THIS.py
```
GUI will launch:<br>

![launch](/images/gui_launch.PNG)

#### Device Setup<a name="dsetup"></a>
Click the "Setup" menubar item and select "Device Setup" (or keyboard shortcut CTRL+D) to configure the devices.  The following screen should appear:<br>

![device setup](/images/device_setup.PNG)

Type the ports that correspond to the DataQ device and Water Vapor Monitor System. A future capability of this program will allow for a thermocouple connection to the DataQ device for enhanced temperature compensation. Check the "Use Pressure" checkbox if a local atmospheric pressure is unavailable. Click on Apply to accept the changes.

If a connection to one or more systems failed, an error message will appear and you will not be able to interact with the system(s).  If connections were established the Scan and Stop buttons of each system will turn active.

#### Recording Setup<a name="ssetup"></a>
Click the "Setup" menubar item and select "Recording Setup" (or keyboard shortcut CTRL+R) to enter the data recording configuration.

![recording setup](/images/recording_setup.PNG)

Customize the recording setup based on your needs then click Apply.  The Record button is now active.

#### Set Airstream Conditions<a name="setac"></a>
From the main GUI, click the "Set Airstream Conditions" to access the following screen:

![airstream conditions](/images/as_conditions.PNG)

Check the box from whichever variable you want to remain constant and type in the numerical value in any of the units within the dropdown box.  Select OK to accept changes.

#### Scan Systems<a name="scan"></a>
Click the "Scan" button on one or both systems to activate the streaming data process.  Numeric data should appear green and be active.

#### Data Recording<a name="rec"></a>
Press the "Record" button to initiate a recording. The LED will turn green while data is being collected and once the recording is complete, the LED will turn back to yellow and Rdg Number will increment by 1.

## Future Capabilities <a name="future"></a>
 - Implement a method of connecting thermocouples to the DataQ A/D for improved temperature and humidity accuracy.
 - Allow for connection of a transducer into the DataQ A/D for improvement of pressure compensation.
 - Generate an interactive, scrolling plot with measured and/or calculated variables for realtime viewing of live data (utilize these resources for help: [1](http://www.pyqtgraph.org/downloads/0.10.0/pyqtgraph-0.10.0-deb/pyqtgraph-0.10.0/examples/scrollingPlots.py ), [2](https://stackoverflow.com/questions/54198278/graph-scrolling-using-pyqt5-and-malplotlib), [3](https://www.learnpyqt.com/courses/graphics-plotting/plotting-pyqtgraph/))

## Acknowledgements <a name="kudos"></a>
Thanks must be given to the rest of the ERB Turbo engineers for help in procuring and developing necessary components for the "Humidity Cart". 
