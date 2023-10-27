
### :mortar_board: Requirements
After creating, the project will open. From the bottom, click on <code>Terminal</code>. Then:
* <code>pip install librosa</code>
* <code>pip install matplotlib</code>
* <code>pip install tensorflow</code>
* <code>pip install easygui</code>

## :scroll: Folder Structure & Code
* Copy and paste the folder <code>Full Dataset wav</code> from this [link](https://drive.google.com/drive/folders/1Qhbkwe_-YTcUpX4WdL_FgtgirT0ik73D?usp=drive_link) to the same <code>PyCharm</code> project folder

## :star2: Running The Project
* Run <code>prepare_dataset.py</code> to preprocess the dataset and create a <code>json</code> file with all processed data
* Run <code>cnn_train_test.py</code> to train the CNN model and save it
* Run <code>predict.py</code> to load the saved CNN model and use it to classify any <code>wav</code> file selected using the file explorer
