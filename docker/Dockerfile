FROM demisto/boto3py3:1.0.0.20350

RUN pip3 install --upgrade awscli

COPY list.py /project/
VOLUME /root/.aws
VOLUME /project

RUN chmod -R 765 "/project/list.py"

#ENTRYPOINT ["./project/list.py"]
CMD [ "python3", "./project/list.py"]
