from flask import Flask, request, render_template
import re

app = Flask(__name__) 
@app.route('/', methods=['GET', 'POST']) 
def index(): 
	if request.method == 'POST': 
		# Retrieve the text from the textarea 
		text = request.form.get('textarea') 
		# Print the text in terminal for verification 
		text1 = request.form.get('textString')
		pattern = re.compile(text1)
		match = re.search(pattern,text)
		countOccurences=str(text.count(text1))
		print(countOccurences)
		if match:
			print(f"'{text1}' found in '{text.split()}'")
			return render_template('found.html',text=text,text1=text1,countOccurences=countOccurences)
		else:
			print(f"'{text1}' not found in '{text.split()}'")
			return render_template('notfound.html',text=text,text1=text1)
	return render_template('home.html') 
if __name__=='__main__':
    app.run(debug=True)