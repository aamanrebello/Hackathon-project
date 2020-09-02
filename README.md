# Hackathon-project
----

**1. The Project**
--
In the actual hackathon, we used an [Arduino](https://www.arduino.cc/) to process sensor readings. The data was formatted and "dumped" into a text file in the computer communicating with the Arduino (data format will be discussed later). After fixed intervals of time, the prepared data file was sent to an [AWS S3](https://aws.amazon.com/s3/) bucket where it was stored. Many such files can be stored in such a bucket. Hence the computer sending the file acts as a kind of edge computing client.

We also had a server laptop that ran a web app. The server downloaded file(s) from the S3 bucket, and performed analyses of the data. Based on this, it could obtain metrics on energy usage over the day (as we implemented in the hackathon) or, as files accumulate in the bucket, over weeks. Based on these metrics the web app displays diagrams and stats. There was also functionality to remotely switch off appliances, which was accomplished by the server sending emails and the edge device regularly monitoring for new emails.

Here, the web app and the communication via S3 is implemented. The Arduino code, Arduino serial data processing program, and remote switching off programs are not implemented here because:
  1. The author currently has no access to Arduinos or sensors, so it is not possible to verify that these programs would perform as required.
  2. Sending via email is quite costly - it involves the usage of personal passwords/ setting up a completely new alternative email account - maybe RPC is a better option (TODO perhaps).
  3. These functions are relatively easy to implement with the correct libraries (e.g. to process Arduino serial output on the connected laptop, Pyserial library can be used).
  
  
**2. Choice of Technology**
--
  - The web app was implemented using the Python Flask framework, with the front end in JavaScript, HTML and CSS.
  - Matplotlib and pyplot libraries were used to generate output graphs
  - Communication and download of the text file via S3 bucket was done via the AWS software development kit (SDK) for Python called [Boto3](https://github.com/boto/boto3).
  - An AWS S3 bucket needs to be set up beforehand and needs to be allowed programmatic access on both client and server laptops 
  - Wifi needs to be available on both sides.
  
  
**3. How to run**
--
  To send from client side to cloud, run the sender program from within the *edge* directory. A text file called *readings.txt* needs to be available within the directory (example provided).
  ```
  cd edge
  python send.py
  ```
  
  To download new text file on server side and generate new graphs, run the *plotgen.py* file from within the *app* directory.
  ```
  cd app
  python plotgen.py
  ```
  
  To run the web app, run:
  ```
  python details.py
  ```
  and go to the URL.
  
  
  **4. Additional Information**
  --
   1. Format of the text file
      - Each row represents a set of sensor readings taken at regular intervals (we set it to be once every 5 seconds).
      - Column 1 represents whether the user was in the room or not. 1 indicates presence of user, 0 indicates absence.
      - Column 2 represents whether the first appliance - a light bulb - is on, which is measured by light sensors in the room. 1 = on, 0 = off.
      - Column 3 represents whether the second appliance - the heater - is 1 = on/0 = off, which is measured by temperature sensors next to the heater.
      - Column 4 represents whwther the third appliance - the AC - is on/off, which is measured by humidity sensors in the room.
     Only three appliances are used in this implementation.
     
   2. Future developments
      - To develop this in the future, one of the first things needed would be to ensure that there is an ability to scale to many users - this would need databases,                     management of storage and development of a better underlying architecture.
      - The current method of client server communication is probably not the most elegant/secure, because of the permissions problems involved in providing access to bucket(s)         from various devices. Maybe it might be a better idea to use RPC or HTTPS POST?
      - The format of sending data in a text file is also rather inelegant.
      - In the best systems, data is updated live, which is not the case here. Something like RPC or a persistent TCP connection may be able to provide this.
      - A sleek, more attractive and fluid front end.
      
   Developments to this project are planned but nothing is likely to happen in the near future.
    
  
