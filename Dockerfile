# Base 이미지로 Python 3.9를 사용합니다.
FROM python:3.9
# 작업 디렉토리를 설정합니다.
WORKDIR /app
# 가상 환경 생성
RUN python -m venv myenv
# 가상 환경 활성화
RUN /bin/bash -c "source myenv/bin/activate"
# 필요한 종속성 파일들을 복사합니다.
COPY requirements.txt ./
# 종속성을 설치합니다.
RUN pip install --no-cache-dir -r requirements.txt
# 소스 코드를 복사합니다.
COPY . .
# 컨테이너 내에서 실행할 명령을 지정합니다.
CMD python manage.py runserver 0.0.0.0:8000