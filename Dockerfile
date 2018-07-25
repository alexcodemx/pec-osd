FROM jenkins/jenkins
USER root
RUN apt-get update
RUN apt install -y python-pandas
USER jenkins
