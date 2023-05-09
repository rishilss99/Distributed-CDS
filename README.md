# Distributed Image Processing using PySpark in HDFS

```
The number of images being uploaded to the internet each day is increasing at an alarming rate but the applications that can use and analyze these images are not available due to limitations in storage space required for the analysis of these large image datasets. Apache Hadoop is an open-source framework that enables distributed processing of Big Data using commodity hardware and Hadoop Distributed File System (HDFS). This project focuses on using Apache Hadoop, Apache Spark, C++ and Python programming language to analyze image datasets and using the k-means algorithm to perform color quantization and image compression.
```

## Code Structure

```
Distributed-Image-Processing
├── README.md
├── src
│   ├── main.py
│   ├── instance
│   │   ├── database.db
│   ├── website
│   │   ├───models.py
│   │   ├── views.py
│   │   ├── __init__.py
│   │   ├── auth.py    
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   ├── login.html
│   │   │   ├── signup.html
│   │   │   ├── home.html
│   │   │   └── success.html
├─── Report.pdf
├─── Presentation.ppt
├─── color_quantizer_kmeans.py
├─── Huffman Coding with K-Means
│   ├── Makefile
│   ├── img1.hpg
│   ├── img1.ppm
│   ├── kmeans.py
│   ├── kpeg.log
│   ├── my_program
│   ├── quantized_image_1.jpeg
│   ├── quantized_image_1.jpg
│   ├── new.py
│   ├── src
│   │   ├── base.cpp
│   │   ├── Image.cpp
│   │   ├── MCU.cpp
│   │   ├── run.cpp
│   │   ├── ssim.cpp
│   │   ├── Transform.cpp
│   │   ├── Utility.cpp
│   │   ├── Decoder.cpp
│   │   ├── HuffmanTree.cpp
│   ├── include (All Libs)
│   ├── build (Builds .O files)



```

### Prerequisites
```
- Python 3.8.1
- PySpark 3.2
- Hadoop 2.7.7
```
