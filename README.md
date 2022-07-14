# Monitor strange behavior in your neighbourhood

Have you heard rumours that a strange car is passing by your neighbourhood, snooping around?

With `neighbourhood-watch` you will be able to keep track of what vehicles pass by your street and you can then use that data to identify any suspicious actors.
For example:

- How frequently certain vehicles come through?
- What time of the day do they usually come through?
- Which days of the week?
- The details of the vehicles e.g. color, license plate etc

## Requirements

This solution aims to be lightweight since I will be running it on a Raspberry Pi 4.
Thus we aim for the least amount of processing to take place on the device and we offload the rest to the cloud™ using `serverless`.

You will need:

- Python >=3.8
- An AWS account

## Setup

Install using `poetry install`.
Alternatively you can do `pip install -r requirements.txt`.
