import os
import argparse
from tqdm import tqdm
from random import shuffle

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train_list", type=str, default="./filelists/list.txt", help="path to train list")
    parser.add_argument("--val_list", type=str, default="./filelists/list_val.txt", help="path to val list")
    parser.add_argument("--source_list", type=str, default="./filelists/list_source.txt", help="path to source list")
    args = parser.parse_args()
    source = []
    train = []
    val = []
    
    with open(args.source_list, 'r', encoding='utf-8') as f:
        source = f.readlines()
        shuffle(source)
        train += source[int(len(source) / 11):]
        val += source[:int(len(source) / 11)]
    shuffle(train)
    shuffle(val)
    
    with open(args.train_list, "w", encoding='utf-8') as f:
        for fname in tqdm(train):
            wavpath = fname
            f.write(wavpath)    
            
    with open(args.val_list, "w", encoding='utf-8') as f:
        for fname in tqdm(val):
            wavpath = fname
            f.write(wavpath)