FROM alpine:3.5
RUN apk add --update py2-pip
RUN apk add --update bash
WORKDIR /code
ADD receive.py /code
ADD requirements.txt /code
ADD wait-for-it.sh /code
RUN pip install -r /code/requirements.txt
CMD ["/code/wait-for-it.sh", "rabbit:5672", "--", "python", "-u", "/code/receive.py"]
