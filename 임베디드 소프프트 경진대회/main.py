import cv2
from pyzbar.pyzbar import decode
import to_arduino
# 카메라 캡처 객체 생성
cap = cv2.VideoCapture(0) #웹캠으로 설정하면 1

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    # 프레임이 없으면 종료
    if not ret:
        break
    # 프레임에서 바코드/QR 코드 검출 및 디코딩 
    codes = decode(frame)

    for code in codes:
        x, y, w, h = code.rect  # 바운딩 박스 좌표와 너비/높이
        if x < frame.shape[1] / 3:  # 화면의 왼쪽 1/3 영역에 있을 경우
            print('left')
            to_arduino.move('left')
        elif x + w > frame.shape[1] * 2 / 3:  # 화면의 오른쪽 1/3 영역에 있을 경우
            print('right')
            to_arduino.move('right')
        else:   # 그 외 중간 영역에 있을 경우 
            to_arduino.move('go')
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)   # 바운딩 박스 그리기

    line_color = (255,0,0)
    line_left = int(frame.shape[1]/3)
    line_right = int(frame.shape[1]*2/3)

    cv2.line(frame,(line_left,0),(line_left,frame.shape[0]),line_color,thickness=2)
    cv2.line(frame,(line_right,0),(line_right,frame.shape[0]),line_color,thickness=2)
    cv2.imshow("frame", frame)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):   # 'q' 키가 눌리면 종료
        break

cap.release()
cv2.destroyAllWindows()
