import pandas as pd
from flask import Flask, render_template, send_file
import os
import webbrowser, random, threading

############### App ##################
app = Flask(__name__)

###### loading files #####
path = app.root_path
CARD_gene = pd.read_csv(os.path.join(path,"files2Read/nuc_CARD_gene.csv"))
CARD_SNP = pd.read_csv(os.path.join(path, "files2Read/nuc_CARD_var.csv"))

#################################  HOME  ###########################################################################

@app.route('/')
def main():
    return render_template('Home/home.html')

################################### Libraries ##############################################################################

@app.route('/Example/Gene_db')
def getGENE():
    gene_db = CARD_gene
    gene_db = gene_db[['Potential Resistance region', 'Region length', 'Reads mapped to region', 'reads mapped per kilobase region']]
    gene_db = tohtml_library(gene_db, "CARD_GENE")
    return render_template('libraries/CARD_GENE.html', table=gene_db, title='CARD Gene Example Output')

@app.route('/Example/SNP_db')
def getSNP():
    snp_db = CARD_SNP
    snp_db = snp_db[['Potential Resistance region', 'Region length', 'Reads mapped to region', 'reads mapped per kilobase region']]
    snp_db = tohtml_library(snp_db, "CARD_SNP")
    return render_template('libraries/CARD_SNP.html', table=snp_db, title='CARD SNP Example Output')

############################################## DOWNLOAD ###########################################################################
@app.route('/Downloads/')
def downloadLib():
    return render_template('Download/download.html')

@app.route('/Downloads/download_CARD_GENE/')
def download_CARD_Gene():
    filename = "CARD_GENE.csv"
    path_zip = os.path.join(path,"files2Read/nuc_CARD_gene.csv")
    return send_file(filename_or_fp=path_zip, attachment_filename=filename, as_attachment=True, mimetype='application/csv')

@app.route('/Downloads/download_CARD_SNP/')
def download_CARD_SNP():
    filename = "CARD_SNP.csv"
    path_zip = os.path.join(path,"files2Read/nuc_CARD_var.csv")
    return send_file(filename_or_fp=path_zip, attachment_filename=filename, as_attachment=True, mimetype='application/csv')

################### Nav-Bar ###########
@app.route('/Contact')
def getinfo():
    return render_template("Navbar/contact.html")

############################# Auxiliary method ###########

def tohtml_library(df, tableId):
    cols = df.columns
    s = '''<table id="''' + tableId + '''" class="display table table-striped table-bordered" width="100%">'''
    s = s + '''
        <thead>
            <tr>'''
    for col in cols:
        temp = '''
                <th>''' + col + '''</th>
            '''
        s = s + temp
    end_header = '''</tr>
        </thead>'''
    s = s + end_header

    s = s + '''
        <tfoot>
            <tr>'''
    for col in cols:
        print col
        if col == "BGC Product":
            col = "BGC"
            temp = '''
					<th>''' + col + '''</th>
				'''
            s = s + temp
            continue
        elif col == "MIBiG Accession":
            col = "MIBiG ac."
            temp = '''
					<th>''' + col + '''</th>
				'''
            s = s + temp
            continue
        else:
            temp = '''
				<th>''' + col + '''</th>
		    	'''
            s = s + temp

    end_foot = '''</tr>
        </tfoot>'''
    s = s + end_foot

    s = s + '''
        <tbody>'''
    for index, row in df.iterrows():
        s = s + '''
            <tr>'''
        for i in xrange(0, len(row)):
            line = str(row[i])
            if len(line) <= 50:
                temp = '''
                    <td>''' + line + '''</td>
                    '''
                s = s + temp
            else:
                temp = '''
                    <td>''' + line[0:50] + '''...''' + '''</td>
                    '''
                s = s + temp
        s = s + '''
            </tr>'''
    end_table = '''
        </tbody>
    </table>'''
    s = s + end_table
    s = s.encode('ascii', 'xmlcharrefreplace')
    return s

############# run app ############
if __name__ == '__main__':
    port = 5000 + random.randint(0, 999)
    url = "http://127.0.0.1:{0}".format(port)
    threading.Timer(1.25, lambda: webbrowser.open(url)).start()
    #webbrowser.open_new(url)
    app.run(port=port, debug=False)

    # port = int(os.environ.get('PORT', 5000))
    # url = 'http://127.0.0.1:5000'
    # webbrowser.open_new(url)
    # app.run(threaded=True, host='0.0.0.0', port=port)


