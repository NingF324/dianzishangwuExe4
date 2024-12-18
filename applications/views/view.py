from applications.views import index_bp
from flask import Flask, render_template, request, redirect, url_for
from applications.users import *
from models import *


@index_bp.route('/login')
def login_index():
    return render_template('login.html')


@index_bp.route('/register')
def register_index():
    return render_template('register.html')


@index_bp.route('/')
def home_page():
    return render_template('homepage.html')


@index_bp.route('/details')
def detail_page():
    commentword = request.args.get('commentword')
    piclink = request.args.get('piclink')
    introduction = request.args.get('introduction')
    seedword = request.args.get('seedword')
    seedword_model = SeedWordModel.query.filter_by(word=seedword).first()
    compword_model = CompWordModel.query.filter_by(word=commentword).first()
    if commentword:
        middle = SeedwordCompword.query.filter_by(seedword_id=seedword_model.id, compword_id=compword_model.id).first()
        grade = middle.grade
    else:
        grade = seedword_model.grade

    return render_template('details.html', thisword=commentword, thislink=piclink, introduction=introduction,
                           seedword=seedword, grade=grade)


# @index_bp.route('/lists')
# def list_page():
#     return render_template('listing.html')

@index_bp.route('/report', methods=['GET'])
def report_page():
    seedword = request.args.get('seedword')
    compword = request.args.get('compword')
    # 在这里可以使用 seedword 和 compword 进行相应的处理
    return render_template('report.html', seedword=seedword, compword=compword)
