# Hanacaraka-AI
This project is our final project for Google Bangkit Academy.

In these projects, we build a handwritten character recognition model that recognizes the ancient javanese alphabet (***Aksara Jawa***), based on a public dataset available on [Kaggle](https://www.kaggle.com/phiard/aksara-jawa). Thanks to [Phiard](https://www.kaggle.com/phiard) the author of the dataset. The dataset contains twenty ancient javanese alphabet characters which are, _ha_, _na_, _ca_, _ra_, _ka_, _da_, _ta_, _sa_, _wa_, _la_, _pa_, _dha_, _ja_, _ya_, _nya_, _ma_, _ga_, _ba_, _tha_, _nga_. The characters are shown in the picture below.

<img align="center" src="/misc/img/javanese_alphabet.jpg"></img>

<p align="center">Figure 1. Ancient Javanese Alphabet</p>

We build our baseline model based on basic Convolutional Neural Network architecture (see Figure 2.) with an additional 128 fully connected neurons layer. Our baseline model produces 98% training accuracy and 88% validation accuracy.

![Figure 2. Baseline Model Architecture](/misc/img/Baseline_model_architecture.jpg)
<p align="center">Figure 2. Baseline Model Architecture</p>

In order to develop a good model, we have searched several research papers and open-source projects on Handwritten Character Recognition topics as our references. Of the many we got, we chose the [Arabic Character Recognition](https://github.com/AmrHendy/Arabic-Handwritten-Images-Recognition) project as our model reference, it is publicly available as an open-source project on GitHub. 

To the best of our knowledge, our baseline CNN model tends to overfit. In our experiment, the accuracy on the training set keeps increasing, while the accuracy on the validation set stays around 80%. Hence, we aim to create an improved model that can reduce the overfitting issue. We use batch normalization, dropout, and global average pooling to reduce overfitting.  However, we find the model still has trouble maintaining the validation accuracy, so we use L2 kernel regularizer on each convolution layer, and use additional callbacks to reduce the learning rate when validation accuracy gets plateaued. 

As a result, we have got more stable validation accuracy. Finally, we successfully developed a model that produces 92% training accuracy and 89% validation accuracy. Our model architecture shown in Figure 3.

![Figure 2. Improved Model Architecture](/misc/img/Improve_model_architecture.jpg)
<p align="center">Figure 2. Improved Model Architecture</p>

During the improved model development, there was a new update on the origin dataset. Hence, we decided to change our current version of the dataset with the new version, and then re-train our improved model architecture on it. We successfully developed an impressive model that omits the overfitting issue and produces 97% training accuracy and 96% validation accuracy.

# Prerequisites
1. Jupyter Notebook or Google Colab
2. Kaggle API Token
3. Python version 3.6 or above
4. Latest version of Tensorflow 2

# How to use
1. Go to your Kaggle profile then download your Kaggle API.
    - My Account --> Look for API section --> Create New API Token
2. You can use it from the original source and modify our code then set the dataset to the original one,
    - or, you can downloaded it from our drive. 
    - In this script we downloaded it and reupload it to [Google Drive](https://drive.google.com/file/d/1CvBaHE6bbLP1bpEHTYxnLM0Lio22LlB4/view?usp=sharing).
    - The origin source are containing many folders for each version of the dataset. We already combined all version of the dataset into single training, validation, and testing folder.
3. Run our [**baseline model**](https://colab.research.google.com/github/IqbalLx/Hanacaraka-AI/blob/master/Hanacaraka%20AI%20-%20notebook.ipynb) on Google Colab.
4. Next, run our [**improved model**](https://colab.research.google.com/github/IqbalLx/Hanacaraka-AI/blob/master/Hanacaraka%20AI%20-%20notebook%20-%20improved%20model.ipynb).
