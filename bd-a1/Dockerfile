FROM ubuntu

RUN apt-get update -y && apt-get install -y \
    python3 \
    python3-pip

RUN pip3 install pandas numpy matplotlib seaborn scikit-learn scipy
WORKDIR /home/doc-bd-a1/
RUN mkdir -p /home/doc-bd-a1

COPY Dataset.csv /home/doc-bd-a1
COPY load.py  /home/doc-bd-a1
COPY dpre.py  /home/doc-bd-a1
COPY eda.py  /home/doc-bd-a1
COPY vis.py  /home/doc-bd-a1
COPY model.py /home/doc-bd-a1
CMD [ "bash" ]
EXPOSE 8080
