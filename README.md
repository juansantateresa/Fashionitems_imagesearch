# Fashion Items Image Search

This repo contains code and documentation for the development of an image search service of Fashion Items. The aim of this project is create a visual search tool for Fashion/Apparel relying on Deep Learning development for building a Classifier able to predict labels of new images using the following [workflow](https://ibb.co/wzxcdt3).


## Repo structure and envirorment

Repo contains 2 main folders. First of all, development folder includes notebooks with the development of the models, utils and preprocess workflows and production folder contains the notebooks prepared to launch the App

All the code is intended to be open in [Google Colab](colab.research.google.com/) and all the files, model weights, variables etc. created in the process are stored in runtime envirorment or google drive, in order to avoid open any files or notebooks in local. Also is a good solution for pip install packages on the go in Colab virtual envirorment.


## Data

I've used imageset from [Zalando MNIST](https://github.com/zalandoresearch/fashion-mnist) which is a dataset of 60,000 train images and 10,000 test images released in 2017 to provide an alternative MNIST dataset for benchmarking Machine Learning Models.

For this project Data is stored raw in free google drive links and its access is detailed in [first notebook](https://github.com/juansantateresa/Fashionitems_imagesearch/blob/2d9f275e9e4721adedaee5e0d28c9e95be4830eb/Development/01_Data_Adquisition_and_Preprocessing.ipynb) of development folder. 

## Tools used

Python Stack was used for data processing, plotting and building functions and Keras API for creating Deep Learning model from scratch. For image processing project switched between common libraries as PIL or CV2.

From Deep Learning model building I have done iterations around layer stacking and model structure, balancing computer processing under the Google Colab Envirorment.

## Deployment

In this project there is a Streamlit App for uploading images and search similar items. As mentioned above, all the project is developed in Colab, [Ngrok](www.ngrok.com) is needed in order to create a public url connected to your local host. 

You can run the App it easily following this instructions.

1. Sign in free in www.ngrok.com and get your [authtoken](https://ngrok.com/docs)
2. Open [01_Production.ipynb](https://github.com/juansantateresa/Fashionitems_imagesearch/blob/main/Production/Notebooks/01_Production.ipynb)
3. Upload to runtime session content folder of Colab these utils files: app.py, img_search.py, model_4.h5, test_pickle (model_4.h5 is a +300mb file so it maybe takes some time)
4. Introduce your authoken in !ngrok authoken xxxx cell.
5. Execute all Cells
6. Click on ngrok url generated 




