from flask import Flask , render_template,request
import pickle
import joblib
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')



@app.route('/heart' , methods = ['POST','GET'])
def submit():
    if request.method == 'POST':
        age = int(request.form['age'])
        Cholesterol = int(request.form['Cholesterol'])
        Thalach = int(request.form['Thalach'])
        Oldpeak =float(request.form['Oldpeak'])
        exang =int(request.form['exang'])
        ca =int(request.form['ca'])
        cp =int(request.form['cp'])
        thal =int(request.form['thal'])

        # Load the Model back from file
        with open("HealthCare_Heart_Disease_Prediction.pkl", 'rb') as file:
            Pickled_RF_Model = pickle.load(file)
        result = Pickled_RF_Model.predict([[age,Cholesterol,Thalach,exang,Oldpeak,ca,cp,thal]])
        if result[0] == 0:
            return render_template('heart.html',data=["Congratulations ,You don't have heart Disease",'green'])
        else:
            return render_template('heart.html',data=["I feel so sorry for you, You have heart Disease ,Please immediately Consult doctors",'red'])

    else :
        return render_template('heart.html')



@app.route('/cancer', methods = ['POST','GET'])
def cancer():
    if request.method == 'POST':
        area_mean = float(request.form['area_mean'])
        area_se = float(request.form['area_se'])
        smothness_worst = float(request.form['smothness_worst'])
        concavity_worst =float(request.form['concavity_worst'])
        symmetry_worst =float(request.form['symmetry_worst'])

        # Load the Model back from file
        with open("Healthcare_Cancer_Predi.pkl", 'rb') as file:
            Pickled_RF_Model = pickle.load(file)
        result = Pickled_RF_Model.predict([[area_mean,area_se,smothness_worst,concavity_worst,symmetry_worst]])
        if result[0] == 0:
            return render_template('cancer.html',data=["Congratulations ,You don't have Cancer Disease",'green'])
        else:
            return render_template('cancer.html',data=["I feel so sorry for you, You have Cancer Disease ,Please immediately Consult doctors",'red'])

    else :
        return render_template('cancer.html')

@app.route('/kidney', methods = ['POST','GET'])
def kidney():
    if request.method == 'POST':
        sg = float(request.form['sg'])
        al = float(request.form['al'])
        sc = float(request.form['sc'])
        hemo =float(request.form['hemo'])
        pcv =float(request.form['pcv'])
        htn = float(request.form['htn'])
        #
        # print(sg,al,sc,hemo,pcv,htn)
        # return "Data Submitted successfully"

        # Load the Model back from file
        with open("Healt_Care_Chronic_Kideny_Prediction.pkl", 'rb') as file:
            Pickled_RF_Model = pickle.load(file)
        result = Pickled_RF_Model.predict([[sg,al,sc,hemo,pcv,htn]])
        if result[0] == 0:
            return render_template('kidney.html',data=["Congratulations ,You don't have kidney Disease",'green'])
        else:
            return render_template('kidney.html',data=["I feel so sorry for you, You have kidney Disease , Please immediately Consult doctors",'red'])

    else :
        return render_template('kidney.html')


@app.route('/diabetes', methods = ['POST','GET'])
def diabetes():
    if request.method == 'POST':
        Glucose = float(request.form['Glucose'])
        blood = float(request.form['blood'])
        Skin = float(request.form['Skin'])
        Insulin =float(request.form['Insulin'])
        BMI =float(request.form['BMI'])
        function = float(request.form['function'])
        Age = float(request.form['Age'])

        # print(Glucose,blood,Skin,Insulin,BMI,function,Age)
        # return "Data Submitted successfully"

        # Load from file
        model = joblib.load("Health_Care_Diabetes_Prediction.pkl")
        result = model.predict([[Glucose,blood,Skin,Insulin,BMI,function,Age]])
        if result[0] == 0:
            return render_template('diabetes.html',data=["Congratulations ,You don't have Diabetes ",'green'])
        else:
            return render_template('diabetes.html',data=["I feel so sorry for you, You have Diabetes , Please immediately Consult doctors",'red'])

    else :
        return render_template('diabetes.html')




@app.route('/liver', methods = ['POST','GET'])
def liver():
    if request.method == 'POST':
        Age = float(request.form['Age'])
        Gender = int(request.form['Gender'])
        total_bilirubin = float(request.form['total_bilirubin'])
        direct_bilirubin =float(request.form['direct_bilirubin'])
        Alkaline_Phosphotase =float(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = float(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = float(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_globulin_ratio = float(request.form['Albumin_globulin_ratio'])

        # print(Age,Gender,total_bilirubin,direct_bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_globulin_ratio)
        # return "Data Submitted successfully"

        # Load from file
        model = joblib.load("Health_Care_Liver_Prediction.pkl")
        result = model.predict([[Age,Gender,total_bilirubin,direct_bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_globulin_ratio]])
        if result[0] == 0:
            return render_template('liver.html',data=["Congratulations ,You don't have liver Disease ",'green'])
        else:

            return render_template('liver.html',data=["I feel so sorry for you, You have liver Disease , Please immediately Consult doctors",'red'])

    else :
        return render_template('liver.html')



@app.route('/about')
def about():
    return render_template('about.html')




if __name__ == "__main__":
    app.run(debug=True)