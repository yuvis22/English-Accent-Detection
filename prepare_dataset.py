import json
import os
import math
import librosa

DATASET_PATH = r"C:\Users\HP\OneDrive\Desktop\desktopp\sccent detection\English-Accent-Detection\Full Dataset wav"
JSON_PATH = "data.json"
SAMPLE_RATE = 22050


def save_mfcc(dataset_path, json_path, num_mfcc=13, n_fft=2048, hop_length=512, segment_duration=3):
    """Extracts MFCCs from music dataset and saves them into a json file along witgh genre labels.

        :param dataset_path (str): Path to dataset
        :param json_path (str): Path to json file used to save MFCCs
        :param num_mfcc (int): Number of coefficients to extract
        :param n_fft (int): Interval we consider to apply FFT. Measured in # of samples
        :param hop_length (int): Sliding window for FFT. Measured in # of samples
        :param: num_segments (int): Number of segments we want to divide sample tracks into
        :return:
        """

  
    data = {
        "mapping": [],
        "labels": [],
        "mfcc": []
    }

    samples_per_segment = segment_duration * SAMPLE_RATE
    num_mfcc_vectors_per_segment = math.ceil(samples_per_segment / hop_length)


    for i, (dirpath, dirnames, filenames) in enumerate(os.walk(dataset_path)):


        if dirpath is not dataset_path:

            # save genre label (i.e., sub-folder name) in the mapping
            semantic_label = dirpath.split("\\")[-1]
            data["mapping"].append(semantic_label)
            print("\nProcessing: {}".format(semantic_label))

            # process all audio files in genre sub-dir
            for f in filenames:

                # load audio file
                file_path = os.path.join(dirpath, f)
                signal, sample_rate = librosa.load(file_path, sr=SAMPLE_RATE)

                track_duration = librosa.get_duration(y=signal, sr=sample_rate)
                num_segments = math.floor(track_duration / segment_duration)

       
                for d in range(num_segments):

                   
                    start = samples_per_segment * d
                    finish = start + samples_per_segment


                    mfcc = librosa.feature.mfcc(y=signal[start:finish],sr=sample_rate, n_mfcc=num_mfcc, n_fft=n_fft, hop_length=hop_length) 

                    mfcc = mfcc.T

                  
                    if len(mfcc) == num_mfcc_vectors_per_segment:
                        data["mfcc"].append(mfcc.tolist())
                        data["labels"].append(i - 1)
                        print("{}, segment:{}".format(file_path, d + 1))


    with open(json_path, "w") as fp:
        json.dump(data, fp, indent=4)


if __name__ == "__main__":
    save_mfcc(DATASET_PATH, JSON_PATH, segment_duration=3)  
