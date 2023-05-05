# Object Detection Model

This repository contains the example and sample files to deploy an Object Detection Model on Katonic Platform.

## Prerequisites for Deployment:


- `launch.py`: This file consists of `loadmodel`, `preprocessing` and `predict` functions.
 The first function helps to fetch the model. The second function is optional,if you are performing any kind of preprocessing on the data before prediction please add all the necessary steps into it and return the formatted input, else you can just return `False` if no processing is required. In the third function write down the code for prediction and return the results in the data structure supported by API response.   

- `schema.py`: Define your schema on how you should pass your input data in predict function.

- `requirements.txt`: Define the required packages along with specific versions this file.

## Sample Input Data for Prediction API

```python
{
  "data": "https://images.pexels.com/photos/2083866/pexels-photo-2083866.jpeg?auto=compress&cs=tinysrgb&h=750&w=1260\"
}
```

## Sample Input Data for Feedback API

This model can be deployed by choosing `Others` option in `Model Type`field of the model deployement section. With this options any type of model can be deployed but under monitoring section they will be able to capture only resource level information.
