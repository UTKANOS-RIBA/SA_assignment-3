# Real-Time Video Processing using Filters

## Project Overview

This project demonstrates a real-time video processing pipeline that applies multiple filters to each frame of a video stream. The filters include converting the video to black-and-white, mirroring the video, resizing the frame, and applying a blur effect.

The pipeline follows the Pipes and Filters architectural pattern, where each frame is passed through a series of filters (components) that process it step-by-step. Each filter performs a specific transformation, and the result is displayed in real time.

## Filters Implemented

1. Black and White Filter: Converts the frame to grayscale.
2. Mirror Filter: Flips the frame horizontally.
3. Resize Filter: Resizes the frame to a specific width and height.
4. Blur Filter: Applies a Gaussian blur to the frame.

## How the Pipeline Works

The pipeline chains the filters together. For each frame captured from the video stream, it is processed sequentially by each filter in the pipeline. The order of filters in the pipeline matters, as each filter modifies the frame before passing it to the next one.

## Requirements

- Python 3.x
- OpenCV (`cv2` library)

To install OpenCV, run:


pip install opencv-python


## Running the Application

### 1. Using a Video File
You can run the script with a video file as the source by passing the file path to process_video:


python main.py


The default example uses a video file named IMG_7030.mp4 located in the same directory.

### 2. Using a Webcam
To use a webcam as the video source, set video_source=0 in process_video. The webcam feed will be processed through the filters:


process_video(0)


### 3. Exiting the Application
Press 'q' to quit the video stream and close all OpenCV windows.

## Code Structure

- Filter: Abstract base class defining the process() method. Every filter must implement this method.
- BlackAndWhiteFilter: Converts the frame to black and white.
- MirrorFilter: Flips the frame horizontally.
- ResizeFilter: Resizes the frame to specific dimensions.
- BlurFilter: Applies a Gaussian blur to the frame.
- Pipeline: Class that holds and executes the chain of filters on each video frame.
- process_video: Function that opens a video stream, processes each frame using the filter pipeline, and displays the processed frames.
