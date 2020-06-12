from tkinter.filedialog import askopenfilename
import frame as f
import csv

# Main use is for file/directory work
import os

# Data analysis libraries:
# Pandas is good at data cleaning
# NumPy is great for number crunching
# MatPlotLib is AMAZING for data visuals - Think about using ***Seaborn*** sometime though...
#   and it can also export these visuals to different formats - PDF would likely be best for SGS
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from textwrap import wrap, fill


def find_file():
    print("Browse")
    file = askopenfilename(filetypes=(("CSV", "*.csv"),
                                      ("Excel", "*.xls"),
                                      ("**TEST**", "*.*")  # Comment this out when program is done
                                      ))
    f.AppFrame.filename = file
    print(str(file))


def upload():  # Ensuring data can be read then analyzing
    print("Upload")
    print(pd.DataFrame(pd.read_csv(f.AppFrame.filename)))
    analyze()


def analyze():  # ANALYZING DATA
    to_analyze = pd.read_csv(f.AppFrame.filename)
    df = pd.DataFrame(to_analyze)
    responses = []
    with open(f.AppFrame.filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        categories = next(csv_reader)

        # Uncomment this for debug when needed
        # for row in csv_reader:  # Extracts data row by row into responses[]
        #     responses.append(row)
        # print("--------------------------------------------")
        # for fields in categories:
        #     print(df[fields].value_counts())
        #     print("--------------------------------------------")

    file_name = "/Charts"
    path = os.path.dirname(f.AppFrame.filename) + file_name

    with PdfPages( path + ".pdf" ) as export_pdf:
        for col in df.columns:
            plt.style.use( 'ggplot' )
            plt.title( label="\n".join(wrap(col,50)), loc='center' )
            plt.xticks( wrap = True )
            plt.tight_layout()
            to_analyze[ col ].hist(alpha=0.5,histtype='bar',ec='black')
            export_pdf.savefig()
            plt.close()

