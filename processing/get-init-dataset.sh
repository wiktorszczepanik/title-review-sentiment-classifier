#!/bin/bash

curl -L -o ../datasets/can/amazon-product-reviews.zip \
  https://www.kaggle.com/api/v1/datasets/download/arhamrumi/amazon-product-reviews

unzip ../datasets/can/amazon-product-reviews.zip -d ../datasets/init/
