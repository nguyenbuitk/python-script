from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("data_small/stations.txt", skiprows=17)
# select 2 column
stations = stations[["STAID", "STANAME                                 "]]

@app.route("/")
def home():
    return render_template("home.html", data=stations.to_html())

@app.route("/api/v1/<station>/<date>")
def about(station, date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    # This line filters the DataFrame to include rows where the value in the '    DATE' column is date
    # squeeze(): remove the title row
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return {"station": station,
            "date": date,
            "temperature": temperature}

@app.route("/api/v1/<station>")
def all_data(station):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = []
    for index, row in df.iterrows():
        result.append({"station": station,
                       "date": row["    DATE"],
                       "temperature": row['   TG']/10})
    return result
    
@app.route("/api/v1/yearly/<station>/<year>")
def yearly(station, year):
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = []
    for index, row in df.iterrows():
        print(type(row['    DATE'].year))
        if row['    DATE'].year == int(year):
            result.append(({"station": station,
                            "date": row["    DATE"],
                            "temperature": row['   TG']/10,
                            "year": year}))
    return result
if __name__ == "__main__":
    app.run(debug=True)