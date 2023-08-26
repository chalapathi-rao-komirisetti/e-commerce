import base64
import streamlit as st
import Amazon
import Noon
import Saco
import Extras
import JarirBookstore
import time
import pandas as pd



global Quit_Variable

Quit_Variable = 0

m = st.markdown("""
<style>
div.stButton > button:Download Table {
    background-color: #0000FF;
    color:#ffffff;
}
div.stButton > button:hover {
    background-color: #FF0000;
    color:##ff99ff;
    }
</style>""", unsafe_allow_html=True)


st.title('Price Convertor Tool')

menu = ['Select search Type' ,'Single Product' , 'Multiple Product']

Choice = st.selectbox('Search Type', menu)



def mainwork(ii):
    global Quit_Variable
    try:

        try:
            data1 = JarirBookstore.JarirBookStore(ii)
        except:
            print('ERROR CAME.....RE-RUNNING THE PROGRAM')
            data1 = JarirBookstore.JarirBookStore(ii)

        time.sleep(10)
        
        try:
            data2 = Amazon.Amazon(ii)
        except:
            print('ERROR CAME.....RE-RUNNING THE PROGRAM')
            data2 = Amazon.Amazon(ii)

        time.sleep(10)
        
        try:
            data3 = Noon.Noon(ii)
        except:
            print('ERROR CAME.....RE-RUNNING THE PROGRAM')
            data3 = Noon.Noon(ii)

        time.sleep(10)
        
        try:
            data4 = Saco.Saco(ii)
        except:
            print('ERROR CAME.....RE-RUNNING THE PROGRAM')
            data4 = Saco.Saco(ii)

        time.sleep(10)
        
        try:
            data5 = Extras.Extras(ii)
        except:
            print('ERROR CAME.....RE-RUNNING THE PROGRAM')
            data5 = Extras.Extras(ii)

        df_result = pd.concat([data1, data2, data3, data4, data5])
        
        df_result = df_result.dropna()

        df_result['aman'] = df_result['Product Name'] + 'True'

        for i in ii.split():
            df_result['aman'] = df_result['aman'].apply(lambda x: str(x) if (i.lower() in str(x).lower() and 'True' in str(x)) else str(x).replace('True', 'False'))
            df_result['aman2'] = df_result['aman'].apply(lambda x: True if (i.lower() in str(x).lower() and 'True' in str(x)) else False)

        d = df_result[df_result['aman2'] == True]
        d.drop(['aman', 'aman2'], axis=1, inplace=True)

        return d

    except Exception as e:

        Quit_Variable = Quit_Variable + 1

        if (Quit_Variable <= 1):
            st.write(Quit_Variable)
            print('Error Occurered....Running program again')
            mainwork(ii)

        elif (Quit_Variable > 1):
            st.stop()
            exit()



def download_Button(my_data):
    csv = my_data.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    st.markdown(href, unsafe_allow_html=True)


if(Choice == 'Single Product'):
    a = st.text_input('ProductCategory')
    if(len(str(a)) > 0 and Quit_Variable <=10):
        my_data = mainwork(a)
        st.dataframe(my_data)

        download_Button(my_data)

    elif(Quit_Variable>10):
        st.stop()
        exit()


if(Choice == 'Multiple Product'):
    data = st.file_uploader('Upload an Excel File',type=['xlsx','csv'])
    if(data):
        temp = pd.read_excel(data)
        l = []
        for iii in temp['Product Name']:
            temptemp = mainwork(iii)
            l.append(temptemp)

        my_data = pd.concat(l)

        download_Button(my_data)