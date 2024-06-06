from inference import InferencePipeline
from inference.core.interfaces.camera.entities import VideoFrame
import csv
from datetime import datetime
from datetime import timedelta
# import Roboflow as rf

# rf = Roboflow(api_key="pjZtbsAzjhkBsKvruel1")
# import opencv to display our annotated images
import cv2
# import supervision to help visualize our predictions
import supervision as sv

# create a simple box annotator to use in our custom sink
annotator = sv.BoxAnnotator()

# num_lists = 5
timestamps_0=[]  # Change this number as needed
timestamps_1=[]
timestamps_2=[]
timestamps_3=[]
timestamps_4=[]
timestamps_5=[]
# for i in range(1, num_lists + 1):
#     exec(f"timestamps_{i} = []")
# timestamps=[]

# def timestampdata(timestampdt):
def timestampdata(timestamps):
    prev_second = None
    count = 0
    print_count = 0
    for timestamp in timestamps:
        second = timestamp.second
        if second != prev_second:
            if prev_second is not None and count != 1:
                print(f"Count for second {prev_second}: {count}")
                print_count += 1
            prev_second = second
            count = 1
        else:
            count += 1
    if prev_second is not None and count != 1:
        print(f"Count for second {prev_second}: {count}")
        print_count += 1
    return print_count

# print("Number of print statements:", count_seconds(timestamps))

def my_custom_sink(predictions: dict, video_frame: VideoFrame):
    # get the text labels for each prediction
    labels = [p["class"] for p in predictions["predictions"]]
    # load our predictions into the Supervision Detections api
    detections = sv.Detections.from_inference(predictions)
    # annotate the frame using our supervision annotator, the video_frame, the predictions (as supervision Detections), and the prediction labels
    # print(predictions)
    # print(detections)
    image = annotator.annotate(
        scene=video_frame.image.copy(), detections=detections, labels=labels
    )
    for prediction in predictions["predictions"]:
        detected_class = prediction["class"]
        class_names=["0","1","2","3","4","5"]
        # print(class_names[0])
        if detected_class == class_names[0]:
            # timestamp_str = video_frame.frame_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
            timestamps_0.append(video_frame.frame_timestamp)
            # print(video_frame.frame_timestamp)
        if detected_class == class_names[1]:
            # timestamp_str = video_frame.frame_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
            timestamps_1.append(video_frame.frame_timestamp)
            # print(video_frame.frame_timestamp)
        if detected_class == class_names[2]:
            # timestamp_str = video_frame.frame_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
            timestamps_2.append(video_frame.frame_timestamp)
            # print(video_frame.frame_timestamp)
        if detected_class == class_names[3]:
            # timestamp_str = video_frame.frame_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
            timestamps_3.append(video_frame.frame_timestamp)
            # print(video_frame.frame_timestamp)
        if detected_class == class_names[4]:
            # timestamp_str = video_frame.frame_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
            timestamps_4.append(video_frame.frame_timestamp)
        if detected_class == class_names[5]:
            # timestamp_str = video_frame.frame_timestamp.strftime("%Y-%m-%d %H:%M:%S.%f")
            timestamps_5.append(video_frame.frame_timestamp)
            # print(video_frame.frame_timestamp)
    # display the annotated image
    cv2.imshow("Predictions", image)
    cv2.waitKey(1)

def write_to_csv(dt, class_label, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['Class', 'Time Duration'])
        writer.writerow([class_label, dt])
def mainfn(modelid):
    pipeline = InferencePipeline.init(
        model_id=modelid,
        video_reference="videoplayback.mp4",
        on_prediction=my_custom_sink,
        max_fps=60,
        api_key="xmb3YIcjWsvnCIz14KMt"
    )

    pipeline.start()
    pipeline.join()


    with open('classduration.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Class', 'Time Duration in sec'])
        
        dt0 = timestampdata(timestamps_0)
        print(f"Monica: {dt0}")
        writer.writerow(['Monica', dt0])

        dt1 = timestampdata(timestamps_1)
        print(f"Chandler: {dt1}")
        writer.writerow(['Chandler', dt1])

        dt2 = timestampdata(timestamps_2)
        print(f"Phoebe: {dt2}")
        writer.writerow(['Phoebe', dt2])

        dt3 = timestampdata(timestamps_3)
        print(f"Rachel: {dt3}")
        writer.writerow(['Rachel', dt3])

        dt4 = timestampdata(timestamps_4)
        print(f"Joey: {dt4}")
        writer.writerow(['Joey', dt4])

        dt5 = timestampdata(timestamps_5)
        print(f"Ross: {dt5}")
        writer.writerow(['Ross', dt5])
    # dt1 = timestampdata(timestamps_0)
    # print(f"class 1: {dt1}")

    # timestamps_list=[dt1,dt2,dt3,dt4,dt5]
    # Write the timestamps data to a CSV file
  
    # for i in range(5):
    #     write_to_csv(timestamps_list[i],i,'classduration.csv')
    # Use the function to write data to CSV
    # write_to_csv(timestamps_1, 'Class 1', 'class_1_duration.csv')
    # write_to_csv(timestamps_2, 'Class 2', 'class_2_duration.csv')
    # write_to_csv(timestamps_3, 'Class 3', 'class_3_duration.csv')
    # write_to_csv(timestamps_4, 'Class 4', 'class_4_duration.csv')
    # write_to_csv(timestamps_5, 'Class 5', 'class_5_duration.csv')
modelid="friends-tv-show-face-detection/1"
mainfn(modelid)