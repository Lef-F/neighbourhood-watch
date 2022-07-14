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

## System design

As we are focusing on keeping the processing on the device light, we designed this system to depend on AWS Lambdas and S3 for most of the processing instead.
The data flow looks as follows:

1. From the Raspberry Pi 4 we upload new video streams to AWS S3
2. The `video -> image sequence` AWS Lambda runs once new video streams have reached our S3 bucket (`video-streams`)
    - The resulting image sequences are dropped into another S3 bucket (`image-sequences`)
3. The `image object recognition` AWS Lambda runs once new image sequences are available on our S3 bucket (`image-sequences`)
    - The object recognition results with cropped image sections are dropped in another S3 bucket (`recognized-segments`)
    - The object recognition result metadata are dropped in a separate subfolder to be queried by e.g. AWS Athena
    - There is potential for data augmentation at this step e.g. license plate recognition, color, car make/type etc
4. The resulting data are made available for querying from some frontend e.g. Grafana.
