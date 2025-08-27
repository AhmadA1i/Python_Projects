# Importing Necessary Libraries
import pyautogui, cv2, numpy as np

# specifying resolution
resolution = (1920, 1080)

# sepcify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# sepcifying name of output file
filename = "recording.avi"

# specifying frame per second (fps)
fps = 60.0

# creating a videowrite object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# create an empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 480, 270)

while True:

    # Taking the screenshot using pyautogui
    img = pyautogui.screenshot()

    # convert the screenshot into a numpy array
    frame = np.array(img)

    # convert it from (Blue, Green, Red) RGB to (Red, Green, Blue) RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # write it to the output file  
    out.write(frame)

    # optional: Display the recording screen
    cv2.imshow("Live", frame)

    # stop recording when we press 'q'
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video Editor
out.release()

# Destroy all windows
cv2.destroyAllWindows()
