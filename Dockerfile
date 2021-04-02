FROM tensorflow/tensorflow:latest-gpu

RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev wget vim

RUN pip install keras numpy pillow flask

COPY . .

RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1v1t2AXEb94rvw32Zj24_9dmQj2_58vB2' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1v1t2AXEb94rvw32Zj24_9dmQj2_58vB2" -O pix2pix_model.h5 && rm -rf /tmp/cookies.txt
RUN mkdir model
RUN mv pix2pix_model.h5 model/

EXPOSE 80
ENTRYPOINT ["python"]
CMD ["app.py"]
