# Sign Language Gesture Recognition using Deep Learning
<p align="center">
<img src="https://1.bp.blogspot.com/-8SxmsK5VoJ0/XVrTpMrJDFI/AAAAAAAAEiM/nAa3vuj8a2sjgEPAeMKXD4m09yKUgjVIQCLcBGAs/s640/Screenshot%2B2019-08-19%2Bat%2B9.51.25%2BAM.png" width="1060" height="450">
</p>

## Overview

This repository contains the code and resources for a project that I've developed to recognize sign language gestures using deep learning and computer vision techniques. The project aims to provide a powerful tool for real-time sign language communication and bridge the communication gap for individuals who use sign language.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Data Collection](#data-collection)
- [Data Preprocessing](#data-preprocessing)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Validation and Testing](#validation-and-testing)
- [Inference and Deployment](#inference-and-deployment)
- [Contributing](#contributing)
- [Real Time Testing Examples](#examples)

## Introduction

In this project, I've developed a deep learning model capable of recognizing sign language gestures captured through computer vision. The model has been trained on a dataset of hand gesture images representing different sign language alphabet characters.

## Data Collection

Data collection involved capturing images or videos of sign language gestures. In the following repo I have included a file 'collect_imgs.py' , using this code you will be able to take pictures to generate your own dataset. I have used 100 images for every alphabet.

## Data Preprocessing

Prior to training, I conducted data preprocessing tasks. This includes resizing, normalizing, and augmenting the data to ensure consistency and improve model performance.

## Model Architecture

The deep learning model architecture is a crucial component of the project. I've chosen an ANN architechture network, capable of learning hierarchical features from hand gesture images.

## Training

Training the model involved feeding the preprocessed data into the network, computing the loss, and optimizing the model's weights using suitable optimization algorithms. The model learned to recognize patterns in hand gestures from the dataset.

## Validation and Testing

To ensure model performance, I split the dataset into training, validation, and testing sets. This allowed me to assess the model's accuracy, precision, recall, and other relevant metrics. The validation set helped in tuning hyperparameters, while the test set provided an unbiased evaluation of model performance.

## Inference and Deployment

Once the model was trained and validated, I used my webcam to see real time classification of the hand Gestures. The deployed model can recognize hand gestures in real-world scenarios, making sign language communication more accessible.

## Contributing

Contributions and suggestions are welcome! Feel free to open issues and submit pull requests to help improve this project.

## Examples
![Sign Language Gesture Recognition](https://drive.google.com/uc?export=view&id=1lLTMVOr5dRnbWF6rHboZmTGNgQ5CaNvz)


