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
  - The web app was implemented using the Python Flask framework, with the front end in JavaScript, HTML and CSS.
  - matplotlib and pyplot libraries were used to generate output graphs
  - communication and download of the text file via S3 bucket was done via the AWS software development kit (SDK) for Python called [Boto3](https://github.com/boto/boto3).
