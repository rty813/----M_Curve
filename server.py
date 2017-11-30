# coding=utf-8
import random, math
from pyecharts import Overlap, Line
from pyecharts.constants import DEFAULT_HOST
from flask import Flask, render_template, request
from theta_beta_M import calc
from flask_wtf import Form
from wtforms import StringField
import numpy as np
from wtforms.validators import DataRequired


class MyForm(Form):
    m = StringField('M', validators=[DataRequired()])
    theta = StringField('theta(Not Nesseary)')
    beta = StringField('beta(Not Nesseary)')


app = Flask(__name__)
app.secret_key = '1234567'


@app.route("/", methods=('GET', 'POST'))
def hello():
    form = MyForm()
    if form.validate_on_submit():
        m_str = form.data['m'].split(' ')
        theta_str = form.data['theta'].split(' ')
        beta_str = form.data['beta'].split(' ')
        m_list = [float(st) for st in m_str]
        theta_list = []
        beta_list = []
        if theta_str != [u'']:
            theta_list = [float(st) for st in theta_str]
        if beta_str != [u'']:
            beta_list = [float(st) for st in beta_str]

        s2d = line(m_list, theta_list, beta_list)
        return render_template('pyecharts.html',
                               myechart=s2d.render_embed(),
                               host='http://rty813.xyz/echarts/',
                               script_list=s2d.get_js_dependencies(),
                               m=form.data['m'])

    return render_template('input.html', form=form)


def line(m_list, theta_list, beta_list):
    line = Line()
    for m in m_list:
        [theta, beta] = calc(m)
        theta_str = [str(t) for t in theta]
        beta_str = [str(t) for t in beta]
        mark_list = []
        for mark_theta in theta_list:
            idx = (np.abs(theta - mark_theta)).argmin()
            x = theta_str[idx]
            y = beta_str[idx]
            app.logger.warning(x)
            app.logger.warning(y)
            mark_list.append({"coord": [x, y], "name": "θ:%s β:%s" % (x, y)})
        for mark_beta in beta_list:
            idx = (np.abs(beta - mark_beta)).argmin()
            x = theta_str[idx]
            y = beta_str[idx]
            app.logger.warning(x)
            app.logger.warning(y)
            mark_list.append({"coord":[x, y], "name":"θ:%s β:%s" %(x,y)})

        line.add("M=" + str(m), beta_str, theta_str, mark_point=mark_list, is_smooth=True, xaxis_min="0", is_convert=True, is_more_utils=True, line_width=4, xaxis_name="θ", yaxis_name="β", yaxis_name_pos='end', xaxis_name_pos='end')
    return line


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
