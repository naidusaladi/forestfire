import streamlit as st
import pickle

dec_clf=pickle.load(open("C:\\Users\\DELL\\Desktop\\fire1\\decisiontreeclf.sav",'rb'))

dec_reg=pickle.load(open("C:\\Users\\DELL\\Desktop\\fire1\\decisionregressior.sav",'rb'))

reg_clf=pickle.load(open("C:\\Users\\DELL\\Desktop\\fire1\\randomforestclf.sav",'rb'))

reg_reg=pickle.load(open("C:\\Users\\DELL\\Desktop\\fire1\\randomforest.sav",'rb'))

svm_clf=pickle.load(open("C:\\Users\\DELL\\Desktop\\fire1\\svc.sav",'rb'))

svm_reg=pickle.load(open("C:\\Users\\DELL\\Desktop\\fire1\\svr.sav",'rb'))

st.title("Forest Fire Prediction")

ffmc = st.number_input(label="FFMC(18.7-96.2)",min_value=18.7, max_value=96.2,step=.5,format="%.1f")

dmc = st.number_input(label="DMC(1.1-291.3)",min_value=1.1, max_value=291.3,step=.5,format="%.1f")

dc = st.number_input(label="DC(7.9-860.6)",min_value=7.9, max_value=860.6,step=.5,format="%.1f")

isi = st.number_input(label="ISI(0.0-56.1)",min_value=0.0, max_value=56.1,step=.5,format="%.1f")

temp = st.number_input(label="TEMPERATURE(2.2-33.3)",min_value=2.2, max_value=33.3,step=.5,format="%.1f")

rh = st.number_input(label="RH(15.0-100.0)",min_value=15.0, max_value=100.0,step=.5,format="%.1f")

wind = st.number_input(label="WIND(0.4-9.4)",min_value=0.4, max_value=9.4,step=.5,format="%.1f")

rain = st.number_input(label="RAIN(0.0-6.4)",min_value=0.0, max_value=6.4,step=.5,format="%.1f")

model = st.selectbox(
    
    'Model',
    ('Decision Tree',"Random Forest" ,'SVM'))

if(st.button('predict')):
    values=[[ffmc,dmc,dc,isi,temp,rh,wind,rain]]
    if(model=='Decision Tree'):
        st.write("Decision Tree")
        dec_clf_pred=dec_clf.predict(values)
        dec_reg_pred=dec_reg.predict(values)
        
        if(dec_clf_pred==1):
            st.error("There is no fire")
        else:
            st.success("There is fire")
        st.write("Area")
        if(dec_reg_pred[0]==0):
            st.error(dec_reg_pred[0])
        else:
            st.success(dec_reg_pred[0])
 #---------------------------------------------------------------------------------           
    if(model=='Random Forest'):
        st.write("Random Forest")
        reg_clf_pred=reg_clf.predict(values)
        reg_reg_pred=reg_reg.predict(values)
        
        if(reg_clf_pred==1):
            st.error("There is no fire")
        else:
            st.success("There is fire")
        st.write("Area")
        if(reg_reg_pred[0]==0):
            st.error(reg_reg_pred[0])
        else:
            st.success(reg_reg_pred[0])
#----------------------------------------------------------------------------------
    if(model=='SVM'):
        st.write("Support Vector Machine")
        svm_clf_pred=svm_clf.predict(values)
        svm_reg_pred=svm_reg.predict(values)
        
        if(svm_clf_pred==1):
            st.error("There is no fire")
        else:
            st.success("There is fire")
        st.write("Area")
        if(svm_reg_pred[0]==0):
            st.error(svm_reg_pred[0])
        else:
            st.success(svm_reg_pred[0])
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            