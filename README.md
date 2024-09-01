# IoT Project: Temperature and Humidity Monitoring with Raspberry Pi and MongoDB

This project involves setting up a Raspberry Pi with a DHT11/DHT22 sensor to monitor temperature and humidity. The data is sent to a PubNub channel and stored in a MongoDB database. The project also includes a simple web server to display the data in real-time.

## Table of Contents
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Software Requirements](#software-requirements)
- [Installation](#installation)
- [Setting Up EC2 Using Terminal](#ec2_terminal_setup)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [License](#license)

## Features
- Real-time temperature and humidity monitoring using a DHT11/DHT22 sensor.
- Data is published to a PubNub channel and stored in a MongoDB database.
- A web interface for displaying the data in real-time.

## Hardware Requirements
- Raspberry Pi (any model)
- DHT11 or DHT22 Temperature and Humidity Sensor
- Breadboard and Jumper Wires
- Internet Connection

## Software Requirements
- Python 3.x
- Raspbian OS (for Raspberry Pi)
- MongoDB (local or cloud, such as MongoDB Atlas)
- Virtual Environment for Python

## Installation

### Step 1: Set Up Raspberry Pi
1. Install Raspbian OS on your Raspberry Pi.
2. Ensure your Raspberry Pi is connected to the internet.
3. Update your Raspberry Pi's package list:

    ```bash
    sudo apt-get update
    sudo apt-get upgrade
    ```

4. Install the required libraries:

    ```bash
    sudo apt-get install python3-pip python3-dev python3-venv
    ```

### Step 2: Clone the Repository
1. Clone the repository to your Raspberry Pi:

    ```bash
    git clone https://github.com/Martinz7z/IoTProject.git
    cd IoTProject
    ```

### Step 3: Create and Activate a Virtual Environment
1. Create a virtual environment:

    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

### Step 4: Install Python Dependencies and Running 
1. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```
2. Activate Pubnub Server fot Listening
   
      ```bash
    python grant_access_pubnub.py
    ```

3. Running the Program for Pi
   ```bash
    python DHT_publisher_pi.py
    ```
### Step 5: Set Up MongoDB
1. If using MongoDB Atlas, create a cluster and get the connection string.
2. Whitelist your Raspberry Pi's IP address in the MongoDB Atlas dashboard.
3. Update the connection string in your Python script.

### Step 6: Configure PubNub
1. Sign up for a PubNub account and obtain your publish and subscribe keys.
2. Replace the placeholder keys in the Python script with your actual PubNub keys.

## Setting Up EC2 Using Terminal

### Step 1: Launch an EC2 Instance
1. Log in to the [AWS Management Console](https://aws.amazon.com/console/).
2. Go to the **EC2 Dashboard**.
3. Click **Launch Instance** and follow the prompts to select an AMI (Amazon Machine Image), instance type, and configure instance details.

### Step 2: Connect to Your EC2 Instance
1. Obtain your instance's public DNS or IP address.
2. Connect to your EC2 instance using SSH:

    ```bash
    ssh -i /path/to/your-key.pem ec2-user@your-ec2-instance-public-dns
    ```

    Replace `/path/to/your-key.pem` with the path to your private key file and `your-ec2-instance-public-dns` with your instance's public DNS or IP address.

### Step 3: Set Up the Environment on EC2
1. Update the package list and install Python:

    ```bash
    sudo yum update -y
    sudo yum install python3 python3-pip -y
    ```

2. Install `virtualenv`:

    ```bash
    pip3 install virtualenv
    ```

3. Clone your project repository:

    ```bash
    git clone https://github.com/Martinz7z/IoTProject.git
    cd IoTProject
    ```

4. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

5. Install the Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. Make sure your virtual environment is activated:

    ```bash
    source venv/bin/activate
    ```
    Install required Libraries
        ```bash
    pip3 install flask pymongo pubnub
    ```

2. Run the Python script to start monitoring:

    ```bash
    cd EC2_MDB_Webserver && sudo python3 app.py
    ```

3. The script will start reading data from the DHT11/DHT22 sensor, publish it to the PubNub channel, and store it in MongoDB.

4. To view the data in real-time, start the web server:

    ```bash
    python web_server.py
    ```

5. Open your browser and navigate to `http://<your-ec2-instance-ip>:5000` to view the data.

## Project Structure
