import cv2
from mtcnn.mtcnn import MTCNN

def process_img(input, output):
    detector = MTCNN()

    image = cv2.imread(input)
    result = detector.detect_faces(image)

    for item in result:
        bounding_box = item['box']
        keypoints = item['keypoints']

        cv2.rectangle(image,
                      (bounding_box[0], bounding_box[1]),
                      (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
                      (0,155,255),
                      2)

        cv2.circle(image,(keypoints['left_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['right_eye']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['nose']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_left']), 2, (0,155,255), 2)
        cv2.circle(image,(keypoints['mouth_right']), 2, (0,155,255), 2)

    cv2.imwrite(output, image)


for i in range(1,11):
    input = "imgs/img{index}.jpg".format(index=i)
    output = "result/img{index}.jpg".format(index=i)
    process_img(input, output);
