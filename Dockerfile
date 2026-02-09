FROM python:3.14.3
LABEL maintainer="Luca Bacchi <bacchilu@gmail.com> (https://github.com/bacchilu)"

ARG USER_ID
ARG GROUP_ID
ARG USERNAME=appuser

RUN groupadd -g ${GROUP_ID} ${USERNAME}
RUN useradd -m -u ${USER_ID} -g ${USERNAME} ${USERNAME}

WORKDIR /app

RUN chown -R ${USERNAME}:${USERNAME} /app
USER ${USERNAME}

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY app /app/app

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]
