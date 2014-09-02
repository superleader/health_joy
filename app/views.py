from flask import render_template, flash, redirect, request
from app import app, db
from app.models import Product, Package
import urllib2
import zipfile

url = 'http://www.fda.gov/downloads/Drugs/DevelopmentApprovalProcess/UCM070838.zip'
@app.route('/')
@app.route('/index')
def index():    
    arch_name = '/tmp/test.zip'
    zfile = open(arch_name, 'w')
    zfile.write(urllib2.urlopen(url).read())
    zfile.close()
    
    fh = open(arch_name, 'rb')
    z = zipfile.ZipFile(fh)
    for name in z.namelist():
        outfile = open(name, 'wb')
        outfile.write('/tmp/' + z.read(name))
        outfile.close()
    fh.close()
    
    product_file = open('product.txt')
    
    # miss titles
    for row in product_file:
        break
    i = 0
    for row in product_file:
        pr = row.split('\t')
        if not Product.query.filter(Product.ndc == pr[1]).first():    
            p = Product()
            p.id = pr[0]
            p.ndc = pr[1]
            p.typename = pr[2]
            p.proprietary_name = pr[3]
            p.proprietary_name_suffix = pr[4]
            p.non_proprietary_name = pr[5]
            p.dos_age_for_name = pr[6]
            p.route_name = pr[7]
            p.start_marketing_date = pr[8]
            p.end_marketing_date = pr[9]
            p.marketing_category_name = pr[10]
            p.application_number = pr[11]
            p.label_name = pr[12]
            p.substance_name = pr[13]
            p.active_numerator_strength = pr[14]
            p.active_ingred_unit = pr[15]
            p.pharm_classes = pr[16]
            p.deaschedule = pr[17]
            p.packages = []
            db.session.add(p)
            db.session.commit()
        i += 1
        if i > 1000:
            break
    product_file.close()

    return render_template('index.html')



@app.route('/list')
def list():   
    q = request.args.get('q')
    if q:
        products = Product.query.filter(Product.proprietary_name.like("%" + q + "%") ).all()[:1000]
    else:
        products = Product.query.all()[:1000]
    return render_template('list.html', products = products, q=q)

    