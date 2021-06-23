from flask import Flask, render_template
import matplotlib.pyplot as plt
from graphgen import load_and_plot

# Responsible for running web app and rendering usage text stats as text if required.

app = Flask(__name__)
filepath = "data.txt"
DATA_FILE_LAST_MODIFIED = 0.0

# This URL has textual usage details shown along with pie graphs.
@app.route('/showdetails')
def show():
    global DATA_FILE_LAST_MODIFIED
    DATA_FILE_LAST_MODIFIED = load_and_plot(filepath, DATA_FILE_LAST_MODIFIED)
    # open data file for analysis.
    f = open(filepath, "r")
    # store lines in file into list
    lines = f.readlines()
    # close file
    f.close()
    # stores number of '1's in the light column
    ltc = 0
    # stores number of '1's in the heater column
    htc = 0
    # stores number of '1's in the AC column
    actc = 0
    # Find the total time of observation
    time = round( len(lines)*5/60, 4 )
    # Used to iterate through list of lines
    index = 0
    # Used to count number of times people leave the room (1 followed by 0 in user column)
    lcount = 0
    # These variables help find the average time a user spends in a room continuously
    streaks = []
    current_streak = 0
    #--------------------------------------------------------------------------------------
    for line in lines:
        if line[0] == "0":
            # light on
            if line[2] == "1":
                ltc = ltc + 1
            # heater on
            if line[4] == "1":
                htc = htc + 1
            # AC on
            if line[6] == "1":
                actc = actc + 1

        else:
            # User present so we add to streak
            current_streak += 1
            # Note that the user leaves a room by looking ahead.
            if index >= 1 and index < (len(lines) - 1):
                if lines[index+1][0] == "0" and lines[index-1][0] == "1":
                    lcount = lcount + 1
                    # Since user leaving, save old streak and start new one.
                    streaks.append(current_streak)
                    current_streak = 0
        index = index + 1

    # Prepare statistics
    ltime = round( (ltc*5)/60 , 3 )
    htime = round( (htc*5)/60 , 3 )
    actime = round( (actc*5)/60, 3 )
    acpc = round( ((actc*5)*318)/3600000, 3 )
    lpc = round( (ltc*5)*10/3600000, 3 )
    htc = round( (htc*5)*4350/36000, 3 )
    avg_user_time = 0
    if len(streaks) > 0:
        avg_user_time = round( ((sum(streaks)*5)/(len(streaks)*60)), 3)

    return render_template('showdeets.html', Time=time, Ltime=ltime, Htime=htime, ACtime=actime, A_U_T=avg_user_time, Lcount=lcount, LEne=lpc, HEne=htc, ACEne=acpc)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == '__main__':
   app.run(port = '6007', debug = True)
   app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
