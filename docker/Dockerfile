FROM demisto/boto3py3:1.0.0.20350

# Install awcli so that we can communicate to the AWS services
RUN pip3 install --upgrade awscli

# Copy our python script to docker
# Create Vol points for our docker-compose

COPY list.py /project/
VOLUME /root/.aws
VOLUME /project

# Make our list.py executable
RUN chmod -R 765 "/project/list.py"

# Run the Py to /project vol and exit docker. 
CMD [ "python3", "./project/list.py"]
