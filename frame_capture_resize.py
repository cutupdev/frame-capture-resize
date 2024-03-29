import cv2
import os

def extract_frames(video_path, output_folder):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get frames and save them to the output folder
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame
        frame_count += 1
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")

        resized_frame = resize_and_fill_black(frame)

        # cv2.imwrite(frame_filename, resized_frame)
        cv2.imwrite(frame_filename, frame)

    # Release the video capture object
    cap.release()


def resize_and_fill_black(img):
    
    height, width, _ = img.shape

    if height > width:
        black = height - width
        img_with_border = cv2.copyMakeBorder(img, 0, 0, round(black/2), round(black/2), cv2.BORDER_CONSTANT, value=(0, 0, 0))
        resized_image = cv2.resize(img_with_border, (416, 416))
    else: 
        black = width - height
        img_with_border = cv2.copyMakeBorder(img, round(black/2), round(black/2), 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        resized_image = cv2.resize(img_with_border, (416, 416))

    return resized_image


if __name__ == "__main__":
    video_path = "V10.mp4"
    output_folder = "frames"

    extract_frames(video_path, output_folder)