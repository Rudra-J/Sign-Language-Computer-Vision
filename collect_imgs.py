import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)
dataset_size = 100
alphabets = [chr(i) for i in range(65+14, 91)]
alphabets.append(' ')

cap = cv2.VideoCapture(0)
for j in range(len(alphabets)):
    if not os.path.exists(os.path.join(DATA_DIR, str(j+14))):
        os.makedirs(os.path.join(DATA_DIR, str(j+14)))

    print('Collecting data for class {}'.format(alphabets[j]))

    done = False
    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "R" ! :)', (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3,
                    cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('r'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)  
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, str(j+14), '{}.jpg'.format(counter)), frame)

        counter += 1

cap.release()
cv2.destroyAllWindows()
