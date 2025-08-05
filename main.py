import pytesseract
from PIL import Image

# 이미지 파일 경로 (이미지 파일이 있는 경로로 변경)
image_path = "image.png"

try:
    # 이미지 열기
    image = Image.open(image_path)

    # OCR 실행 (한국어 텍스트 추출)
    text = pytesseract.image_to_string(
        image, lang="eng"
    )  # lang='kor'는 한국어 인식 옵션

    # 추출된 텍스트 출력
    print(text)

except FileNotFoundError:
    print(f"Error: 파일 '{image_path}'를 찾을 수 없습니다.")
except Exception as e:
    print(f"OCR 처리 중 오류 발생: {e}")
