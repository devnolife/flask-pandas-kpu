from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Step 1: Route to upload the file
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            # Redirect to next step
            return redirect(url_for('input_kabupaten', filepath=filepath))
    return render_template('index.html')

# Step 2: Input Kode Kabupaten
@app.route('/input_kabupaten/<path:filepath>', methods=['GET', 'POST'])
def input_kabupaten(filepath):
    if request.method == 'POST':
        kode_kab = request.form['kode_kab']
        return redirect(url_for('input_kecamatan', filepath=filepath, kode_kab=kode_kab))
    return render_template('input_kabupaten.html')

# Step 3: Input Nama Kecamatan
@app.route('/input_kecamatan/<path:filepath>/<kode_kab>', methods=['GET', 'POST'])
def input_kecamatan(filepath, kode_kab):
    # Read the Excel file
    df = pd.read_excel(filepath, header=4)
    
    # Get unique Kecamatan names
    kecamatan_list = df['Unnamed: 1'].dropna().unique().tolist()

    if request.method == 'POST':
        kecamatan = request.form['kecamatan']
        return redirect(url_for('input_kelurahan', filepath=filepath, kode_kab=kode_kab, kecamatan=kecamatan))
    return render_template('input_kecamatan.html', kecamatan_list=kecamatan_list)

# Step 4: Input Nama Kelurahan
@app.route('/input_kelurahan/<path:filepath>/<kode_kab>/<kecamatan>', methods=['GET', 'POST'])
def input_kelurahan(filepath, kode_kab, kecamatan):
    # Read the Excel file
    df = pd.read_excel(filepath, header=4)
    
    # Filter by selected Kecamatan and get unique Kelurahan names
    kelurahan_list = df[df['Unnamed: 1'] == kecamatan]['Unnamed: 3'].dropna().unique().tolist()

    if request.method == 'POST':
        kelurahan = request.form['kelurahan']
        # Proceed with data processing and cleaning
        return redirect(url_for('clean_data', filepath=filepath, kode_kab=kode_kab, kecamatan=kecamatan, kelurahan=kelurahan))
    
    # Debugging step: Print the extracted list of Kelurahan
    print("Kelurahan List: ", kelurahan_list)  # This will help you see if it's extracting properly
    
    return render_template('input_kelurahan.html', kelurahan_list=kelurahan_list)
# Step 5: Clean Data
@app.route('/clean_data/<path:filepath>/<kode_kab>/<kecamatan>/<kelurahan>', methods=['GET'])
def clean_data(filepath, kode_kab, kecamatan, kelurahan):
    # Read the Excel file and apply the cleaning process here
    df = pd.read_excel(filepath, header=4)
    
    # Filter the data based on Kecamatan and Kelurahan
    filtered_df = df[(df['Unnamed: 1'] == kecamatan) & (df['Unnamed: 3'] == kelurahan)]
    
    # Cleaning logic here...
    # You can return or save the cleaned data as needed
    return render_template('result.html', tables=[filtered_df.to_html(classes='data')], titles=filtered_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
