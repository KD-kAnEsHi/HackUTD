# Plant Smarter
- uses light and temperature sensor data to help plants grow better
- Uses ML to process data and use Samba Nova's API to suggest plant growth'

https://www.youtube.com/watch?v=0gDY958_tsA&ab_channel=AadeshSenthilkumar

## Inspiration
We were inspired by the idea of using technology to help plants grow better while making farming and gardening more efficient and environmentally friendly. Many people struggle with maintaining the right conditions for plants, and we wanted to create a solution that could provide precise recommendations. By combining machine learning and sensors, we saw an opportunity to support sustainable agriculture and make plant care easier for everyone.

## What it does
Our project predicts the best conditions for plant growth using a machine-learning model. It identifies the ideal temperature, sunlight hours, and humidity for a plant and sends this information to sensors in the field. The sensors then check real-time conditions and compare them to the ideal ones. If the conditions are not suitable, the system suggests ways to adjust. The data collected by the sensors is sent back to the machine learning model to improve its predictions. The new data is also added to the original dataset to make the model smarter and more accurate over time.

## How we built it
We started with a dataset containing information on plant growth conditions like temperature, sunlight hours, and humidity. Using this data, we trained a gradient-boosting machine learning model to predict whether conditions are good or bad for a plant. We built hardware sensors to monitor real-time temperature, humidity, and sunlight. These sensors send their data to the system, which uses the machine learning model to classify conditions. Finally, we created a pipeline to add sensor data back into the dataset and retrain the model, ensuring it continuously improves.

## Challenges we ran into
We faced several challenges while working on this project. First, it was tricky to ensure the sensors gave accurate measurements because even small errors could affect the model's predictions. Integrating the sensors with the software was another hurdle, as we had to ensure smooth communication between the two. Training the machine learning model to make reliable predictions for different types of plants took a lot of trial and error. Finally, setting up real-time feedback from the sensors to the AI system required careful planning and debugging.

## Accomplishments that we're proud of
We are proud of successfully combining machine learning with real-world hardware. Building a system that adapts and learns from real data was a major achievement for us. It feels great to know that our project not only predicts optimal plant growth conditions but also continuously improves over time. We are also proud that our solution could help make agriculture more sustainable and efficient, making a positive impact on the environment.

## What we learned
This project taught us a lot about machine learning and how to apply it to real-world problems. We gained experience in integrating hardware sensors with software systems, which was new and exciting for us. We also learned about the importance of sustainability in agriculture and how technology can support eco-friendly practices. Perhaps most importantly, we saw the value of continuously improving a system by feeding it real-world data, making it smarter and more reliable over time.

## What's next for Plant Smarter
In the future, we plan to add more advanced sensors to track other factors like soil moisture and air quality. We want to create a mobile app that gives users real-time updates and advice about their plants. Our goal is to make the system even smarter by customizing it for specific plant types. We also want to scale this project to larger farms and greenhouses to help more people. Lastly, we’re exploring how to power the sensors with renewable energy, like solar panels, to make the system even more sustainable.

## Contributors
Aadesh Senthilkumar - Iot Device (Created an Iot Device which gathers data such as Temperature, Humidity, and Sunlight, and stores it in a database)

Shivani Elitem - Machine Learning Model (Created a Gradient Boosting Model with a 75% accuracy using a dataset from Kaggle and the data from the IoT Device)

Karl Demanou - Backend (Integrated Iot Device Data and ML Model Predictions with SambaNova AI)

Ammar Mohammed - Frontend (Created the front-end interface for the project, displaying the data from the database such as tables and charts, and trying to integrate the SambaNova AI onto the front end)
