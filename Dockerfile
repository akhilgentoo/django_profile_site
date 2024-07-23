# init a base image 
FROM quay.apps.lz-np2.ent-ocp4-useast1.aws.internal.das/openshift-base-images/python-3.9-image-with-certs
MAINTAINER Akeel <akhilkumar8609@gmail.com>
#create and set directory
USER root
WORKDIR /pegaops

#Copy requirement files to opsadmin directory
ADD . /pegaops/
RUN chown -R root:root /pegaops/
RUN chmod +w /pegaops/db.sqlite3
#RUN chmod  666 /pegaops/
RUN pip3 install -r requirements.txt
# define the command to start the container
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]