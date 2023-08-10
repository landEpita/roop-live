# Face-Swap Live Webcam Project

This project allows users to perform real-time face swapping on a webcam feed. It is built upon the base of the ROOP project.

## Prerequisites

Ensure you have the required dependencies and your system meets the necessary requirements.
Download model.
    wget https://civitai.com/api/download/models/85159 -O inswapper_128.onnx

### Virtual Webcam Setup

This project requires setting up a virtual webcam. Here's how you can achieve this:

1. Load the v4l2loopback module:
    sudo modprobe v4l2loopback

2. To configure the virtual device, you can run:
    sudo modprobe -r v4l2loopback && sudo modprobe v4l2loopback devices=1 video_nr=10 card_label="Overlay" exclusive_caps=1 max_buffers=2

3. To verify the virtual device has been correctly set up, run:
    ls -la -1 /sys/devices/virtual/video4linux

If everything is set up correctly, you should see your virtual device listed.

## Running the Face-Swap

To run the face-swap on your live webcam feed:

1. Navigate to the project directory.

2. Execute the main script:
    python main.py

This will initiate the face-swapping process on your webcam. Ensure your virtual webcam device is selected as the source in any application you're using.
q
## Notes

- The virtual webcam device can be used in software such as video conferencing tools, allowing you to use the face-swap feature in real-time communications.
- Ensure the v4l2loopback module is correctly set up before attempting to run the main script.

## Acknowledgments

This project is based on the ROOP project. A big thank you to all contributors of the original project.
