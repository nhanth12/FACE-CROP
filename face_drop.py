import cv2
from mtcnn.mtcnn import MTCNN

index = 0
def process_img(input):
    detector = MTCNN()

    image = cv2.imread(input)
    result = detector.detect_faces(image)

    for item in result:
        global index
        index += 1
        bounding_box = item['box']
        keypoints = item['keypoints']
        imgDroped = image[bounding_box[1]:bounding_box[1] + bounding_box[3], bounding_box[0]:bounding_box[0]+bounding_box[2]]
        op = "face_drop_result/face_{index}.jpg".format(index=index)
        cv2.imwrite(op, imgDroped)


for i in range(1,11):
    input = "imgs/img{index}.jpg".format(index=i)
    process_img(input);
