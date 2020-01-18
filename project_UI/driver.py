from flask import Flask, request, render_template
import ml
import Recommend
import time
import generate_chart

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

# @app.route('/analysis1', methods=["POST"])
# def analysis():
#     location = int(request.form['location'])
#     # values = ['location']
#     # print(values)
#     #prediction = ml.classifier_nb.predict([values])
#     # print(f"income = {prediction[0]}")
#     # return render_template("industry.html", result=prediction[0])

@app.route('/analysis.html')
def analysisGet():
    return render_template("analysis.html")
#=========================================================================
df = generate_chart.load_data()
#==========================================================================
@app.route('/industry', methods=["POST"])
def getIndustryTrend():
    df = generate_chart.load_data();
    generate_chart.industry_based_plot(df);
    time.sleep(2)
    return render_template("industry.html")

@app.route('/industry.html')
def industryGet():
    return render_template("industry.html")
#==========================================================================

@app.route('/company', methods=["POST"])
def getCompanyTrend():
    df = generate_chart.load_data();
    generate_chart.company_cont_plot(df);
    time.sleep(2)
    return render_template("company.html")

@app.route('/company.html')
def companyGet():
    # generate_chart.company_cont_plot(df);
    # time.sleep(2)
    return render_template("company.html")
#==============================================================================
@app.route('/jobtitle', methods=["POST"])
def getTrendingJob():
    df = generate_chart.load_data();
    generate_chart.company_cont_plot(df);
    time.sleep(2)
    return render_template("jobtitle.html")

@app.route('/jobtitle.html')
def getJobTitle():
    # generate_chart.jobtittle_plot(df);
    # time.sleep(2)
    return render_template("jobtitle.html")
#==============================================================================

@app.route('/predict.html')
def predictGet():
    return render_template("predict.html")

@app.route('/predict', methods=["POST"])
def predict():
    location=int(request.form['location'])
    industry = int(request.form['industry'])
    skills = int(request.form['skills'])
    avg_experience = int(request.form['minExp'])
    # education = int(request.form['education'])
    edu  = request.form['a']
    di_gr = { "ug" : 0 , "pg" : 0 , "doc" : 0 }
    upd_di_gr = {edu : 1}
    di_gr.update(upd_di_gr);
    i_di_ug = []
    i_di_ug = list(di_gr.values());
    # i_di_ug = []
    # for val1  in  di_gr:
    #     i_di_ug.append(di_g[val1])
    # Doctorate = int(request.form['Doctorate'])
    values = [location,industry,skills,avg_experience,i_di_ug[0],i_di_ug[1],i_di_ug[2]]

    prediction = ml.build_random_forest_model().predict([values])
    #print(f"Number of Openings = {round(prediction[0])}")

    return render_template("result.html", result=round(prediction[0]))
#=====================================================================================
@app.route('/recommend.html')
def recoGet():
    return render_template("recommend.html")

@app.route('/recommend', methods=["POST"])
def recoPost():
    location_f=request.form['location']
    industry_f = request.form['industry']
    skills_f = request.form['skills']
    avg_experience_f = request.form['minExp']
    # education = int(request.form['education'])
    edu  = request.form['a']
    di_gr = { "ug" : 0 , "pg" : 0 , "doc" : 0 }
    upd_di_gr = {edu : 1}
    di_gr.update(upd_di_gr);
    i_di_ug = []
    i_di_ug = list(di_gr.values());
    # values = [location,industry,skills,avg_experience,i_di_ug[0],i_di_ug[1],i_di_ug[2]]
    #
    # jobs = Recommend.recommend()
    # jobs.createGlobalTempView("Naukri")
    result=Recommend.recommend(industry_f,location_f,skills_f,avg_experience_f)
    return render_template("result_reco.html", data=result)
#=====================================================================================

app.run(host='0.0.0.0',port=4400, debug=True)