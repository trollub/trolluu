FROM python:3.10-slim-buster as main
ENV DOCKER=true
ENV TROLL=true
ENV GIT_PYTHON_REFRESH=quiet
ENV PIP_NO_CACHE_DIR=1
RUN apt-get update && apt-get install apt-utils libcairo2 git curl ffmpeg libavcodec-dev libavutil-dev libavformat-dev libtool liblz4-dev libunwind-dev libswscale-dev libavdevice-dev -y --no-install-recommends
RUN apt-get install gcc python3-dev flac wkhtmltopdf neofetch -y --no-install-recommends
RUN rm -rf /var/lib/apt/lists /var/cache/apt/archives /tmp/*
RUN git clone https://github.com/trollub/troll/ /troll
WORKDIR /troll
RUN git fetch && git checkout main
RUN pip install --no-warn-script-location --no-cache-dir -r requirements.txt
RUN pip install tgcrypto werkzeug moviepy psutil pytube pillow websockets pydub python-dateutil SpeechRecognition requests-toolbelt emoji 
EXPOSE 8080
RUN mkdir /data
CMD ["python3", "-m", "friendly-telegram"]

