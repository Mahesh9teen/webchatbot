from flask import Flask,render_template,request
import os
from langchain.llms import OpenAI
os.environ['OPENAI_API_KEY']='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'
app=Flask(__name__)

def demon(text):
    mahesh=OpenAI(openai_api_key= os.environ['OPENAI_API_KEY'],temperature=0.4)

    result=mahesh.predict(text)
    return  result

@app.route('/',methods=['GET','POST'])
def main():
    web='wait...'
    somting='mahi'
    BGimg = 'templates/BGimg.jpg'
    if request.method=='POST':
        somting=request.form['spy']
        web=demon(somting)
        
    return render_template('index.html',mmm=web, BGimg=BGimg)
#appgg
#ghmghm

if __name__ =='__main__':
    app.run(debug=True)