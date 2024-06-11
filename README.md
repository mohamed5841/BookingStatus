# Project 1: Booking Status Prediction

## Objective
Predict the booking status for hotel reservations.

## Technologies Used
- **Flask**: Used for deploying the model as a web application.

## Description
This project aims to predict whether a hotel booking will be canceled or not based on various features. The analysis includes the following parameters:
- **Number of Adults**: The total count of adults per reservation.
- **Number of Children**: The total count of children per reservation.
- **Weekend Nights**: The number of weekend nights included in the booking.
- **Weekday Nights**: The number of weekday nights included in the booking.
- **Meal Plans**: Different meal plan options chosen by the guests.
- **Car Parking**: Availability and usage of car parking facilities.
- **Room Types**: Types of rooms booked.
- **Lead Time**: The number of days between booking and arrival.
- **Market Segment Types**: Various market segments such as corporate, leisure, etc.

Using these features, a predictive model was built to determine the likelihood of a booking being canceled. The model is deployed using Flask, allowing for easy web-based interactions and predictions.
