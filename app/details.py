from flask import Flask, render_template
import matplotlib.pyplot as plt

# Responsible for running web app and rendering usage text stats as text if required.

app = Flask(__name__)


# This URL has the textual usage details hidden
@app.route('/')
def hide():
    return render_template('display.html')

# This URL has textual usage details shown along with pie graphs.
@app.route('/showdetails')
def show():
    f = open("data.txt", "r")
    lines = f.readlines()
    f.close()
    ltc = 0
    htc = 0
    actc = 0
    time = round( len(lines)*5/60, 4 )
    index = 0
    lcount = 0
    for line in lines:
        if line[0] == "0":
            if line[2] == "1":
                ltc = ltc + 1

            if line[4] == "1":
                htc = htc + 1

            if line[6] == "1":
                actc = actc + 1
        else:
            if index >= 1 and index < (len(lines) - 1):
                if lines[index+1][0] == "0" and lines[index-1][0] == "1":
                    lcount = lcount + 1
        index = index + 1

    ltime = round( (ltc*5)/60 , 3 )
    htime = round( (htc*5)/60 , 3 )
    actime = round( (actc*5)/60, 3 )
    acpc = round( ((actc*5)*318)/3600000, 3 )
    lpc = round( (ltc*5)*10/3600000, 3 )
    htc = round( (htc*5)*4350/36000, 3 )

    return render_template('showdeets.html', Time=time, Ltime=ltime, Htime=htime, ACtime=actime, Lcount=lcount, LEne=lpc, HEne=htc, ACEne=acpc)

if __name__ == '__main__':
   app.run(port = '6007', debug = True)
