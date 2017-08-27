# Connect Raspberry Pi online simulator to Azure IoT Hub (Node.js)

_Captured: 2017-08-18 at 09:05 from [docs.microsoft.com](https://docs.microsoft.com/en-gb/azure/iot-hub/iot-hub-raspberry-pi-web-simulator-get-started)_

In this tutorial, you begin by learning the basics of working with Raspberry Pi online simulator. You then learn how to seamlessly connect the Pi simulator to the cloud by using [Azure IoT Hub](https://docs.microsoft.com/en-gb/azure/iot-hub/iot-hub-what-is-iot-hub).

If you have physical devices, visit [Connect Raspberry Pi to Azure IoT Hub](https://docs.microsoft.com/en-gb/azure/iot-hub/iot-hub-raspberry-pi-kit-node-get-started) to get started.

![Connect Raspberry Pi web simulator to Azure IoT Hub](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-raspberry-pi-web-simulator/3_banner.png)

## What you do

  * Learn the basics of Raspberry Pi online simulator.
  * Create an IoT hub.
  * Register a device for Pi in your IoT hub.
  * Run a sample application on Pi to send simulated sensor data to your IoT hub.

Connect simulated Raspberry Pi to an IoT hub that you create. Then you run a sample application with the simulator to generate sensor data. Finally, you send the sensor data to your IoT hub.

## What you learn

  * How to create an Azure IoT hub and get your new device connection string. If you don't have an Azure account, [create a free Azure trial account](https://azure.microsoft.com/free/) in just a few minutes.
  * How to work with Raspberry Pi online simulator.
  * How to send sensor data to your IoT hub.

## Overview of Raspberry Pi web simulator

Click the button to launch Raspberry Pi online simulator.

There are three areas in the web simulator.

  1. Assembly area - The default circuit is that a Pi connects with a BME280 sensor and an LED. The area is locked in preview version so currently you cannot do customization.
  2. Coding area - An online code editor for you to code with Raspberry Pi. The default sample application helps to collect sensor data from BME280 sensor and sends to your Azure IoT Hub. The application is fully compatible with real Pi devices. 
  3. Integrated console window - It shows the output of your code. At the top of this window, there are three buttons.
    * **Run** \- Run the application in the coding area.
    * **Reset** \- Reset the coding area to the default sample application.
    * **Fold/Expand** \- On the right side there is a button for you to fold/expand the console window.
![Overview of Pi online simulator](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-raspberry-pi-web-simulator/0_overview.png)

## Create an IoT hub

  1. In the [Azure portal](https://portal.azure.com/), click **New** > **Internet of Things** > **IoT Hub**.

![Create an IoT hub in the Azure portal](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-create-hub-and-device/1_create-azure-iot-hub-portal.png)

  2. In the **IoT hub** pane, enter the following information for your IoT hub:

**Name**: Enter the name of your IoT hub. If the name you enter is valid, a green check mark appears.

**Pricing and scale tier**: Select the **F1 - Free** tier. This option is sufficient for this demo. For more information, see the [Pricing and scale tier](https://azure.microsoft.com/pricing/details/iot-hub/).

**Resource group**: Create a resource group to host the IoT hub or use an existing one. For more information, see [Use resource groups to manage your Azure resources](https://docs.microsoft.com/en-gb/azure/azure-resource-manager/resource-group-portal).

**Location**: Select the closest location to you where the IoT hub is created.

**Pin to dashboard**: Select this option for easy access to your IoT hub from the dashboard.

![Enter information to create your IoT hub](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-create-hub-and-device/2_fill-in-fields-for-azure-iot-hub-portal.png)

The IoT hub will be publicly discoverable as a DNS endpoint, so make sure to avoid any sensitive information while naming it.

  3. Click **Create**. Your IoT hub might take a few minutes to create. You can see progress in the **Notifications** pane.

![See progress notifications for your IoT hub](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-create-hub-and-device/3_notification-azure-iot-hub-creation-progress-portal.png)

  4. After your IoT hub is created, click it on the dashboard. Make a note of the **Hostname**, and then click **Shared access policies**.

![Get the hostname of your IoT hub](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-create-hub-and-device/4_get-azure-iot-hub-hostname-portal.png)

  5. In the **Shared access policies** pane, click the **iothubowner** policy, and then copy and make a note of the **Connection string** of your IoT hub. For more information, see [Control access to IoT Hub](https://docs.microsoft.com/en-gb/azure/iot-hub/iot-hub-devguide-security).

![Get your IoT hub connection string](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-create-hub-and-device/5_get-azure-iot-hub-connection-string-portal.png)

## Register a device in the IoT hub for your device

  1. In the [Azure portal](https://portal.azure.com/), open your IoT hub.

  2. Click **Device Explorer**.

  3. In the Device Explorer pane, click **Add** to add a device to your IoT hub. Then do the following:

**Device ID**: Enter the ID of the new device. Device IDs are case sensitive.

**Authentication Type**: Select **Symmetric Key**.

**Auto Generate Keys**: Select this check box.

**Connect device to IoT Hub**: Click **Enable**.

![Add a device in the Device Explorer of your IoT hub](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-create-hub-and-device/6_add-device-in-azure-iot-hub-device-explorer-portal.png)

The device ID may be visible in the logs collected for customer support and troubleshooting, so make sure to avoid any sensitive information while naming it.

  4. Click **Save**.

  5. After the device is created, open the device in the **Device Explorer** pane.
  6. Make a note of the primary key of the connection string.

![Get the device connection string](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-create-hub-and-device/7_get-device-connection-string-in-device-explorer-portal.png)

## Run a sample application on Pi web simulator

  1. In coding area, make sure you are working on the default sample application. Replace the placeholder in Line 15 with the Azure IoT hub device connection string. 

  2. Click **Run** or type `npm start` to run the application.

You should see the following output that shows the sensor data and the messages that are sent to your IoT hub

![Output - sensor data sent from Raspberry Pi to your IoT hub](https://docs.microsoft.com/en-gb/azure/iot-hub/media/iot-hub-raspberry-pi-web-simulator/2_run_application.png)

## Next steps

You've run a sample application to collect sensor data and send it to your IoT hub.

To continue to get started with Azure IoT Hub and to explore other IoT scenarios, see the following:
