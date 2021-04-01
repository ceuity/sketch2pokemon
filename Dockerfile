FROM tensorflow/tensorflow:latest-gpu

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev

RUN pip install keras numpy pillow flask

COPY . .

RUN wget model http://e-ver.wo.tc:8080/pix2pix_model.h5

EXPOSE 80
ENTRYPOINT ["python"]
CMD ["app.py"]
