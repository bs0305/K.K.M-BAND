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

# 손 모양 분류기 클래스
class HandShapeClassifier:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.notes = {
            "주먹": 0,                 # FX_piano01.mp3
            "엄지": 1,                 # FX_piano02.mp3
            "검지": 2,                 # FX_piano03.mp3
            "중지": 3,                 # FX_piano04.mp3
            "약지": 4,                 # FX_piano05.mp3
            "새끼": 5,                 # FX_piano06.mp3
            "엄지와 검지": 6,          # FX_piano07.mp3
            "엄지와 중지": 7,          # FX_piano08.mp3
            "엄지와 약지": 8,          # FX_piano09.mp3
            "엄지와 새끼": 9,          # FX_piano10.mp3
            "엄지와 검지와 중지": 10,   # FX_piano11.mp3
            "엄지와 중지와 약지": 11,   # FX_piano12.mp3
            "엄지와 약지와 새끼": 12    # FX_piano13.mp3
        }
    
    def detect_hand_shape(self, frame):
        # 손 감지
        results = self.hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 손가락의 랜드마크 인덱스
                finger_tip_indices = [4, 8, 12, 16, 20]
                
                # 손가락 상태 분석
                finger_states = [1 if hand_landmarks.landmark[i].y <
                                 hand_landmarks.landmark[i - 1].y else 0 for i in finger_tip_indices]
                
                # 손 모양 분류
                hand_shape = self.classify_hand_shape(finger_states)
                
                # 손 모양에 해당하는 음정 반환
                note_index = self.notes.get(hand_shape, None)
                
                return hand_shape, note_index
        else:
            return None, None
    
    def classify_hand_shape(self, finger_states):
        # 손 모양 분류 로직
        # 여기서는 단순히 손가락 개수를 기반으로 모양을 식별합니다.
        finger_count = sum(finger_states)
        
        if finger_count == 0:
            print("도")
            return "주먹"
        elif finger_count == 1:
            if finger_states == [1, 0, 0, 0, 0]:
                print("도#")
                return "엄지"
            elif finger_states == [0, 1, 0, 0, 0]:
                print("레")
                return "검지"
            elif finger_states == [0, 0, 1, 0, 0]:
                print("레#")
                return "중지"
            elif finger_states == [0, 0, 0, 1, 0]:
                print("미")
                return "약지"
            else:
                print("파")
                return "새끼"
        elif finger_count == 2:
            if finger_states == [1, 1, 0, 0, 0]:
                print("파#")
                return "엄지와 검지"
            elif finger_states == [1, 0, 1, 0, 0]:
                print("솔")
                return "엄지와 중지"
            elif finger_states == [1, 0, 0, 1, 0]:
                print("솔#")
                return "엄지와 약지"
            elif finger_states == [1, 0, 0, 0, 1]:
                print("라")
                return "엄지와 새끼"
        elif finger_count == 3:
            if finger_states == [1, 1, 1, 0, 0]:
                print("라#")
                return "엄지와 검지와 중지"
            elif finger_states == [1, 0, 1, 1, 0]:
                print("시")
                return "엄지와 중지와 약지"
            elif finger_states == [1, 0, 0, 1, 1]:
                print("도")
                return "엄지와 약지와 새끼"
        elif finger_count == 4:
            return "4 손가락 펴기"
        elif finger_count == 5:
            return "손 모두 펴기"
        else:
            return "알 수 없는 모양"

# 메인 함수
def main():
    cap = cv2.VideoCapture(0)
    classifier = HandShapeClassifier()
    last_play_time = 0
    pitch_offset = 0  # 피치 오프셋 초기화
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # 현재 시간 가져오기
        current_time = time.time()
        frame = cv2.flip(frame, 1)
        
        # 손 모양 감지
        hand_shape, note_index = classifier.detect_hand_shape(frame)
        
        # 소리 출력
        if note_index is not None and current_time - last_play_time > 0.3:
            last_play_time = current_time
            
            # 피치 조절
            pitch_adjusted_index = (note_index + pitch_offset) % len(sound_files)
            sound_path = os.path.join(sound_dir, sound_files[pitch_adjusted_index])
            
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play()
        
        
       
        
        # 화면에 손 모양 표시
        if hand_shape:
            cv2.putText(frame, f"{hand_shape}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow('Hand Shape Detection', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()