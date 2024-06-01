import cv2
import mediapipe as mp
import pygame
import os
import time

# 소리 파일 디렉토리
sound_dir = "C:/Users/User/Downloads/piano"

# 소리 파일 목록
sound_files = ["FX_piano01.mp3", "FX_piano02.mp3", "FX_piano03.mp3", "FX_piano04.mp3",
               "FX_piano05.mp3", "FX_piano06.mp3", "FX_piano07.mp3", "FX_piano08.mp3",
               "FX_piano09.mp3", "FX_piano10.mp3", "FX_piano11.mp3", "FX_piano12.mp3",
               "FX_piano13.mp3"]

# 소리 파일 로드
pygame.mixer.init()

# 웹캠 캡처 초기화
cap = cv2.VideoCapture(0)

# 화면 크기 가져오기
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
half_height = height // 2

# 화면 좌우 반전 플래그
flip_flag = True

# Mediapipe 손가락 감지 모델 로드
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# 이전 소리 재생 시간 초기화
last_play_time = time.time()

# 소리 재생 간격 설정 (최소 0.1초)
min_play_interval = 0.3

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 화면 좌우 반전
    if flip_flag:
        frame = cv2.flip(frame, 1)
    
    # 프레임을 BGR에서 RGB로 변환
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Mediapipe로 손 감지
    results = hands.process(rgb_frame)
    
    # 손 감지되지 않은 경우 빈 리스트 반환
    if results.multi_hand_landmarks is not None:
        for hand_landmarks in results.multi_hand_landmarks:
            for point in hand_landmarks.landmark:
                # 손가락의 x, y 좌표
                finger_x = int(point.x * width)
                finger_y = int(point.y * height)
                
                # 현재 시간
                current_time = time.time()
                
                # 소리 재생 간격 확인 후 재생
                if current_time - last_play_time > min_play_interval:
                    for i in range(13):
                        x_start = i * (width // 13)
                        x_end = (i + 1) * (width // 13)
                        if x_start < finger_x < x_end and finger_y < half_height:
                            sound_path = os.path.join(sound_dir, sound_files[i])
                            pygame.mixer.music.load(sound_path)
                            pygame.mixer.music.play()
                            last_play_time = current_time  # 이전 소리 재생 시간 업데이트
                            break  # 한 번의 손가락 이벤트에 대해서만 소리 재생하도록 처리
                
                # x 범위 표시
                cv2.rectangle(frame, (x_start, 0), (x_end, height), (0, 255, 0), 2)
    
    # y 범위 표시
    cv2.line(frame, (0, half_height), (width, half_height), (255, 0, 0), 2)
    
    # 전체 x 범위 표시
    for i in range(1, 13):
        x_pos = i * (width // 13)
        cv2.line(frame, (x_pos, 0), (x_pos, height), (0, 0, 255), 1)
    
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
