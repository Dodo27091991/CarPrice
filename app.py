from flask import Flask,render_template,jsonify
from flask_restx import Api,Resource
import pickle
import math
from scipy.stats import zscore
import pandas as pd
import numpy as np

app = Flask(__name__)
api=Api(app)

model=pickle.load(open('Carprice.pickle','rb'))

@app.route("/new")
def index():
    return render_template("index.html")


#@app.route("/predict/<int:symboling>,<int:compressionratio>,<int:enginesize>,<int:milage>,<int:cyliender_No>,<int:category_0>,<int:category_1>,<int:category_2>,<int:fueltype_diesel>,<int:fueltype_gas>,<int:fuelsystem_1bbl>,<int:fuelsystem_2bbl>,<int:fuelsystem_4bbl>,<int:fuelsystem_idi>,<int:fuelsystem_mfi>,<int:fuelsystem_mpfi>,<int:fuelsystem_spdi>,<int:fuelsystem_spfi>,<int:enginetype_dohc>,<int:enginetype_l>,<int:enginetype_ohc>,<int:enginetype_ohcf>,<int:enginetype_ohcv>,<int:enginetype_rotor>,<int:drivewheel_4wd>,<int:drivewheel_fwd>,<int:drivewheel_rwd>,<int:carbody_convertible>,<int:carbody_hardtop>,<int:carbody_hatchback>,<int:carbody_sedan>,<int:carbody_wagon>,<int:aspiration_std>,<int:aspiration_turbo>")
#def predict(symboling,compressionratio,enginesize,milage,cyliender_No,category_0,category_1,category_2,fueltype_diesel,fueltype_gas,fuelsystem_1bbl,fuelsystem_2bbl,fuelsystem_4bbl,fuelsystem_idi,fuelsystem_mfi,fuelsystem_mpfi,fuelsystem_spdi,fuelsystem_spfi,enginetype_dohc,enginetype_dohcv,enginetype_l,enginetype_ohc,enginetype_ohcf,enginetype_ohcv,enginetype_rotor,drivewheel_4wd,drivewheel_fwd,drivewheel_rwd,carbody_convertible,carbody_hardtop,carbody_hatchback,carbody_sedan,carbody_wagon,aspiration_std,aspiration_turbo):
#    print("Hello there")
#    print(symboling,compressionratio,enginesize,milage,cyliender_No,category_0,category_1,category_2,fueltype_diesel,fueltype_gas,fuelsystem_1bbl,fuelsystem_2bbl,fuelsystem_4bbl,fuelsystem_idi,fuelsystem_mfi,fuelsystem_mpfi,fuelsystem_spdi,fuelsystem_spfi,enginetype_dohc,enginetype_dohcv,enginetype_l,enginetype_ohc,enginetype_ohcf,enginetype_ohcv,enginetype_rotor,drivewheel_4wd,drivewheel_fwd,drivewheel_rwd,carbody_convertible,carbody_hardtop,carbody_hatchback,carbody_sedan,carbody_wagon,aspiration_std,aspiration_turbo)
        
#    return jsonify({"msg":"This car price is different"})

#"symboling,compressionratio,enginesize,milage,cyliender_No,category_0,category_1,category_2,fueltype_diesel,fueltype_gas,fuelsystem_1bbl,fuelsystem_2bbl,fuelsystem_4bbl,fuelsystem_idi,fuelsystem_mfi,fuelsystem_mpfi,fuelsystem_spdi,fuelsystem_spfi,enginetype_dohc,enginetype_dohcv,enginetype_l,enginetype_ohc,enginetype_ohcf,enginetype_ohcv,enginetype_rotor,drivewheel_4wd,drivewheel_fwd,drivewheel_rwd,carbody_convertible,carbody_hardtop,carbody_hatchback,carbody_sedan,carbody_wagon,aspiration_std,aspiration_turbo"
@api.route("/predict/<int:symboling>,<int:compressionratio>,<int:enginesize>,<int:milage>,<int:cyliender_No>,<int:category_0>,<int:category_1>,<int:category_2>,<int:fueltype_diesel>,<int:fueltype_gas>,<int:fuelsystem_1bbl>,<int:fuelsystem_2bbl>,<int:fuelsystem_4bbl>,<int:fuelsystem_idi>,<int:fuelsystem_mfi>,<int:fuelsystem_mpfi>,<int:fuelsystem_spdi>,<int:fuelsystem_spfi>,<int:enginetype_dohc>,<int:enginetype_dohcv>,<int:enginetype_l>,<int:enginetype_ohc>,<int:enginetype_ohcf>,<int:enginetype_ohcv>,<int:enginetype_rotor>,<int:drivewheel_4wd>,<int:drivewheel_fwd>,<int:drivewheel_rwd>,<int:carbody_convertible>,<int:carbody_hardtop>,<int:carbody_hatchback>,<int:carbody_sedan>,<int:carbody_wagon>,<int:aspiration_std>,<int:aspiration_turbo>")
class Predict(Resource):
    def get(self,symboling, compressionratio, enginesize, milage, cyliender_No, category_0, category_1, category_2, fueltype_diesel, fueltype_gas, fuelsystem_1bbl, fuelsystem_2bbl, fuelsystem_4bbl, fuelsystem_idi, fuelsystem_mfi, fuelsystem_mpfi, fuelsystem_spdi, fuelsystem_spfi, enginetype_dohc, enginetype_dohcv, enginetype_l, enginetype_ohc, enginetype_ohcf, enginetype_ohcv, enginetype_rotor, drivewheel_4wd, drivewheel_fwd, drivewheel_rwd, carbody_convertible, carbody_hardtop, carbody_hatchback, carbody_sedan, carbody_wagon, aspiration_std, aspiration_turbo):
        print("Hello there",flush=True)

        symboling=symboling-3
        #symboling=3
        #compressionratio=9
        #enginesize=130
        #milage=48
        #cyliender_No=4


        #columns=['symboling', 'compressionratio', 'enginesize', 'milage', 'cyliender_No', 'category_0', 'category_1', 'category_2', 'fueltype_diesel', 'fueltype_gas', 'fuelsystem_1bbl', 'fuelsystem_2bbl', 'fuelsystem_4bbl', 'fuelsystem_idi', 'fuelsystem_mfi', 'fuelsystem_mpfi', 'fuelsystem_spdi', 'fuelsystem_spfi', 'enginetype_dohc', 'enginetype_dohcv', 'enginetype_l', 'enginetype_ohc', 'enginetype_ohcf', 'enginetype_ohcv', 'enginetype_rotor', 'drivewheel_4wd', 'drivewheel_fwd', 'drivewheel_rwd', 'carbody_convertible', 'carbody_hardtop', 'carbody_hatchback', 'carbody_sedan', 'carbody_wagon', 'aspiration_std', 'aspiration_turbo']
        independent_variable=[symboling, compressionratio, enginesize, milage, cyliender_No, category_0, category_1, category_2, fueltype_diesel, fueltype_gas, fuelsystem_1bbl, fuelsystem_2bbl, fuelsystem_4bbl, fuelsystem_idi, fuelsystem_mfi, fuelsystem_mpfi, fuelsystem_spdi, fuelsystem_spfi, enginetype_dohc, enginetype_dohcv, enginetype_l, enginetype_ohc, enginetype_ohcf, enginetype_ohcv, enginetype_rotor, drivewheel_4wd, drivewheel_fwd, drivewheel_rwd, carbody_convertible, carbody_hardtop, carbody_hatchback, carbody_sedan, carbody_wagon, aspiration_std, aspiration_turbo]
        data=pd.DataFrame(independent_variable)
        data=data.apply(zscore)
        data=data.values.reshape(1,-1)
        print("All good")
        try:
            pv=model.predict(data)
            result=pv[0]
            result=math.pow(10,result)
            print(result)
            #pv=(10**pv[0])
        except Exception as e:
            print(e)
        return jsonify({"msg": result})
    
if __name__ == '__main__':
    app.run(debug=True)