import cv2
import mediapipe as mp

# MediaPipe Hands 초기화
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 소리 파일 디렉토리와 소리 파일 목록
sound_dir = "C:/Users/User/Downloads/piano"
sound_files = ["FX_piano01.mp3", "FX_piano02.mp3", "FX_piano03.mp3", "FX_piano04.mp3",
               "FX_piano05.mp3", "FX_piano06.mp3", "FX_piano07.mp3", "FX_piano08.mp3",
               "FX_piano09.mp3", "FX_piano10.mp3", "FX_piano11.mp3", "FX_piano12.mp3",
               "FX_piano13.mp3"]

# 포즈 정의 함수들
def is_thumb_up(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (thumb_tip.y < index_finger_tip.y and
        thumb_tip.y < middle_finger_tip.y and
        thumb_tip.y < ring_finger_tip.y and
        thumb_tip.y < pinky_tip.y):
        return True
    return False

def is_index_finger_up(landmarks):
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (index_finger_tip.y < thumb_tip.y and
        index_finger_tip.y < middle_finger_tip.y and
        index_finger_tip.y < ring_finger_tip.y and
        index_finger_tip.y < pinky_tip.y):
        return True
    return False
def is_middle_finger_up(landmarks):
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (middle_finger_tip.y < thumb_tip.y and
        middle_finger_tip.y < index_finger_tip.y and
        middle_finger_tip.y < ring_finger_tip.y and
        middle_finger_tip.y < pinky_tip.y):
        return True
    return False

def is_ring_finger_up(landmarks):
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (ring_finger_tip.y < thumb_tip.y and
        ring_finger_tip.y < index_finger_tip.y and
        ring_finger_tip.y < middle_finger_tip.y and
        ring_finger_tip.y < pinky_tip.y):
        return True
    return False

def is_pinky_up(landmarks):
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]

    if (pinky_tip.y < thumb_tip.y and
        pinky_tip.y < index_finger_tip.y and
        pinky_tip.y < middle_finger_tip.y and
        pinky_tip.y < ring_finger_tip.y):
        return True
    return False

def is_thumb_and_index_up(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (thumb_tip.y < index_finger_tip.y and
        middle_finger_tip.y < thumb_tip.y and
        middle_finger_tip.y < ring_finger_tip.y and
        middle_finger_tip.y < pinky_tip.y):
        return True
    return False

def is_index_and_middle_up(landmarks):
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (index_finger_tip.y < middle_finger_tip.y and
        thumb_tip.y < index_finger_tip.y and
        ring_finger_tip.y < middle_finger_tip.y and
        ring_finger_tip.y < pinky_tip.y):
        return True
    return False

def is_middle_and_ring_up(landmarks):
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (middle_finger_tip.y < ring_finger_tip.y and
        index_finger_tip.y < middle_finger_tip.y and
        thumb_tip.y < index_finger_tip.y and
        pinky_tip.y < ring_finger_tip.y):
        return True
    return False

def is_ring_and_pinky_up(landmarks):
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]

    if (ring_finger_tip.y < pinky_tip.y and
        middle_finger_tip.y < ring_finger_tip.y and
        thumb_tip.y < index_finger_tip.y and
        thumb_tip.y < pinky_tip.y):
        return True
    return False

def is_thumb_and_index_and_middle_up(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (thumb_tip.y < index_finger_tip.y and
        middle_finger_tip.y < thumb_tip.y and
        ring_finger_tip.y < middle_finger_tip.y and
        ring_finger_tip.y < pinky_tip.y):
        return True
    return False

def is_index_and_middle_and_ring_up(landmarks):
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (index_finger_tip.y < middle_finger_tip.y and
        middle_finger_tip.y < ring_finger_tip.y and
        thumb_tip.y < index_finger_tip.y and
        pinky_tip.y < ring_finger_tip.y):
        return True
    return False

def is_middle_and_ring_and_pinky_up(landmarks):
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]

    if (middle_finger_tip.y < ring_finger_tip.y and
        ring_finger_tip.y < pinky_tip.y and
        thumb_tip.y < index_finger_tip.y and
        thumb_tip.y < pinky_tip.y):
        return True
    return False

def is_thumb_and_index_and_middle_and_ring_up(landmarks):
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

    if (thumb_tip.y < index_finger_tip.y and
        middle_finger_tip.y < thumb_tip.y and
        ring_finger_tip.y < middle_finger_tip.y and
        pinky_tip.y < ring_finger_tip.y):
        return True
    return False

def is_index_and_middle_and_ring_and_pinky_up(landmarks):
    index_finger_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_finger_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_finger_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]
    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]

    if (index_finger_tip.y < middle_finger_tip.y and
        middle_finger_tip.y < ring_finger_tip.y and
        ring_finger_tip.y < pinky_tip.y and
        thumb_tip.y < index_finger_tip.y):
        return True
    return False
# 이하 생략 (나머지 손가락 감지 함수들 추가 필요)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # BGR 이미지를 RGB로 변환
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # 손 랜드마크 감지
    results = hands.process(image)

    # 이미지를 다시 BGR로 변환
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # 랜드마크 그리기 및 제스처 인식 추가
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            if is_thumb_up(landmarks):
                cv2.putText(image, 'Thumb Up', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            elif is_index_finger_up(landmarks):
                cv2.putText(image, 'Index Finger Up', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
            # 나머지 손가락 감지 함수들에 대한 분기 추가
            

    # 화면에 출력
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
