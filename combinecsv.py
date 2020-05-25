import shutil
import glob
#the path of the csv files to combine
path = r'/Users/csaavedra/nps upload' 
allFiles = glob.glob(path + "/*.csv")
#name your output file
with open('nps_full_upload_april2020.csv', 'wb') as outfile:
    for i, fname in enumerate(allFiles):
        with open(fname, 'rb') as infile:
            if i != 0:
                infile.readline()  # Throw away header on all but first file
            # Block copy rest of file from input to output without parsing
            shutil.copyfileobj(infile, outfile)
            print(fname + " has been imported.")
