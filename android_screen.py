import scrcpy
import cv2

client = scrcpy.Client(device="123f07fc")


def on_frame(frame):
    if frame is not None:
        # frame is an bgr numpy ndarray (cv2' default format)
        cv2.imshow("viz", frame)
    cv2.waitKey(10)


client.add_listener(scrcpy.EVENT_FRAME, on_frame)


def on_init():
    # Print device name
    print(client.device_name)


client.add_listener(scrcpy.EVENT_INIT, on_init)


client.start()