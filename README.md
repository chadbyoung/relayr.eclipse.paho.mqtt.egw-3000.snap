# Paho.MQTT - Dell Edge Gateway - Relayr

My goal here is to create a snap where I can send sensor data (Temperature,
Pressure, Humidity) from a Dell Edge Gateway 3001 to the Relayr developer hub.
This program will read the ambient temperature, pressure, and humidity inside
of a Dell Edge Gateway 3001 using the onboard ST Micro HTS221 and XXX sensors, and then publish that temperature
to the Relayr developer cloud - where I can view it from dashboard.

## Authors

* **Thibaut Rouffineau** - *Initial work*  
[github](https://github.com/campbieil/mqtt-for-ubuntu-core)
* **Chad Young** - *Current Work*  
[github](https://github.com/chadyoungdell/relayr.eclipse.paho.mqtt.egw-3000.snap)

### Prerequisites

Ubuntu Snapcraft 2.33 or later (This version was built on 2.33)  
A Relayr account - Sign up for a free account here --> https://developer.relayr.io  
A Dell Edge Gateway 3001 with the Ubuntu Core 16 Operating System installed

### How to build the snap
* Make sure that you have snapcraft installed on your Ubuntu Desktop 16.04 system
* Clone this repository to your local system
* "cd" into the main directory
* Run snapcraft

### Installing the snap 
1. Copy the snap to gateway
2. Run the following command:  
    - sudo snap install egw3000-relayr-mqtt_1.0_amd64.snap --devmode

### Running the program
1. Start the program:
    - egw3000-relayr-mqtt.publish

## License
  
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
  
  
  
  
Anything below this line is boiler plate and will be up dated as available
--------------------------------------------------------------------------------



## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 


## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc


