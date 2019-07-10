import pydub
import pydub.silence as sl
import sys
import re
import datetime
import glob
from tqdm import tqdm


silence_len = 3000  # Минимальная длина промежутка молчания.
date_rgx = re.compile(r'.*recording-(\d{8})')


def get_date(file_name):
    s = date_rgx.match(file_name).group(1)
    return datetime.datetime.strptime(s, '%Y%m%d')


def print_results(records):
    for k, v in records.items():
        print(f'{k.strftime("%Y-%m-%d")} : {round(v)} minute(s)')


def main(args):

    if(len(args) < 1):
        files = glob.glob("./*.mp3")
    else:
        files = glob.glob(f'{args[0].rstrip("/")}/*.mp3')

    if(len(files) < 1):
        print('Записи не найдены')
        return
    records = {}
    print('Обработка...')
    for file in tqdm(files):
        audio = pydub.AudioSegment.from_mp3(file)
        sound_spans = sl.detect_nonsilent(audio, min_silence_len=silence_len,
                                          seek_step=500,
                                          silence_thresh=-40)
        d = get_date(file)
        if d in records:
            records[d] += sum([span[1]-span[0]
                              for span in sound_spans])/1000/60
        else:
            records[d] = sum([span[1]-span[0]
                              for span in sound_spans])/1000/60

    print('\nГотово:\n')
    print_results(records)


if __name__ == "__main__":
    main(sys.argv[1:])
