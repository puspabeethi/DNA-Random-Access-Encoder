import datetime
import DNA_DATA_ENCODER

begin_time = datetime.datetime.now()

DNA_DATA_ENCODER.encoder(file_name="test.txt", oligo_length=230, primer_pair_count=72)

print(datetime.datetime.now() - begin_time)
