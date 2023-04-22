from bokeh.embed import components
from bokeh.resources import INLINE
from flask import Flask, render_template

from huitu import shu,sheng_ditu,city_ditu,beijing_leibie,top5_leibie,leibie_xinzi,xinzi_sl,\
    top5xz_lb,xueli,xl_xz,gznx,rz_gm,gwfl,dw_xz,cp_ciyu,js_ciyu,xs_ciyu,\
    yy_ciyu,sj_ciyu,sc_ciyu,zn_ciyu,js_shu,js_shengmap,js_city_sl,js_zhucitu,\
    jsxinzi,jszuigao,jszuidi,nxxllx,js_ruzi,js_gm,js_dingwei,js_dwxz,js_fl,js_gz,cp_shu,cp_shengmap,cp_city_sl,cp_zhucitu,\
    cpxinzi,cpzuigao,cpzuidi,cpnxxllx,cp_ruzi,cp_gm,cp_dingwei,cp_dwxz,cp_fl,cp_gz,sj_shu,sj_shengmap,sj_city_sl,sj_zhucitu,\
    sjxinzi,sjzuigao,sjzuidi,sjnxxllx,sj_ruzi,sj_gm,sj_dingwei,sj_dwxz,sj_fl,sj_gz,yy_shu,yy_shengmap,yy_city_sl,yy_zhucitu,\
    yyxinzi,yyzuigao,yyzuidi,yynxxllx,yy_ruzi,yy_gm,yy_dingwei,yy_dwxz,yy_fl,yy_gz

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/docs',methods=["GET","POST"])
def docs():
    tu1=shu()
    tu2=sheng_ditu()
    tu3=city_ditu()
    tu4=beijing_leibie()
    tu5=top5_leibie()
    js_resources = INLINE.render_js()
    css_resources = INLINE.render_css()
    script1, div1 = components(tu5)
    tu6=leibie_xinzi()
    js_resources2 = INLINE.render_js()
    css_resources2 = INLINE.render_css()
    script2, div2= components(tu6)
    tu7=xinzi_sl()
    # js_resources3 = INLINE.render_js()
    # css_resources3= INLINE.render_css()
    # script3, div3= components(tu7)
    tu8=top5xz_lb()
    js_resources4 = INLINE.render_js()
    css_resources4= INLINE.render_css()
    script4, div4= components(tu8)
    tu9=xueli()
    tu10=xl_xz()
    js_resources5 = INLINE.render_js()
    css_resources5= INLINE.render_css()
    script5, div5= components(tu10)
    tu11=gznx()
    tu12=rz_gm()
    tu13=gwfl()
    tu14=dw_xz()
    js_resources6 = INLINE.render_js()
    css_resources6= INLINE.render_css()
    script6, div6= components(tu14)
    return render_template('docs.html',
                           the_data1=tu1,
                           the_data2=tu2,
                           the_data3=tu3,
                           the_data4=tu4,
                           the_data5=tu5,
                           js_resources=js_resources,
                           css_resources=css_resources,
                           plot_script=script1,
                           plot_div=div1,
                           the_data6=tu6,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script2=script2,
                           plot_div2=div2,
                           the_data7=tu7,
                           # js_resources3=js_resources3,
                           # css_resources3=css_resources3,
                           # plot_script3=script3,
                           # plot_div3=div3,
                           the_data8=tu8,
                           js_resources4=js_resources4,
                           css_resources4=css_resources4,
                           plot_script4=script4,
                           plot_div4=div4,
                           the_data9=tu9,
                           js_resources5=js_resources5,
                           css_resources5=css_resources5,
                           plot_script5=script5,
                           plot_div5=div5,
                           the_data11=tu11,
                           the_data12=tu12,
                           the_data13=tu13,
                           the_data14=tu14,
                           js_resources6=js_resources6,
                           css_resources6=css_resources6,
                           plot_script6=script6,
                           plot_div6=div6,
                           )

@app.route('/ciyun',methods=["GET","POST"])
def ciyun():
    js_tu=js_ciyu()
    cp_tu=cp_ciyu()
    yy_tu=yy_ciyu()
    zn_tu=zn_ciyu()
    sc_tu=sc_ciyu()
    sj_tu=sj_ciyu()
    xs_tu=xs_ciyu()
    return render_template("ciyuntu.html",
                           the_data1=cp_tu,
                           the_data2=js_tu,
                           the_data3=yy_tu,
                           the_data4=sj_tu,
                           the_data5=sc_tu,
                           the_data6=zn_tu,
                           the_data7=xs_tu
                           )

@app.route('/baogao',methods=["GET","POST"])
def baogao():
    return render_template("baogao.html")

@app.route('/xuexi',methods=["GET","POST"])
def xuexi():
    return render_template("xuexi.html")
@app.route('/jishu',methods=["GET","POST"])
def jishu():
    tu1=js_shu()
    tu2=js_shengmap()
    tu3=js_city_sl()
    tu4=js_zhucitu()
    tu5=jsxinzi()
    tu6=jszuigao()
    js_resources1 = INLINE.render_js()
    css_resources1 = INLINE.render_css()
    script1, div1 = components(tu6)
    tu7=jszuidi()
    js_resources2 = INLINE.render_js()
    css_resources2 = INLINE.render_css()
    script2, div2 = components(tu7)
    tu8=nxxllx()
    tu9=js_ruzi()
    tu10=js_gm()
    tu11=js_dingwei()
    tu12=js_dwxz()
    js_resources3 = INLINE.render_js()
    css_resources3 = INLINE.render_css()
    script3, div3 = components(tu12)
    tu13=js_fl()
    tu14=js_gz()
    return render_template("jishu.html",
                           the_data1=tu1,
                           the_data2=tu2,
                           the_data3=tu3,
                           the_data4=tu4,
                           the_data5=tu5,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script1=script1,
                           plot_div1=div1,
                           the_data6=tu6,
                           the_data7=tu7,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script2=script2,
                           plot_div2=div2,
                           the_data8=tu8,
                           the_data9=tu9,
                           the_data10=tu10,
                           the_data11=tu11,
                           the_data12=tu12,
                           js_resources3=js_resources3,
                           css_resources3=css_resources3,
                           plot_script3=script3,
                           plot_div3=div3,
                           the_data13=tu13,
                           the_data14=tu14,
                           )

@app.route('/chanpin',methods=["GET","POST"])
def chanpin():
    tu1=cp_shu()
    tu2=cp_shengmap()
    tu3=cp_city_sl()
    tu4=cp_zhucitu()
    tu5=cpxinzi()
    tu6=cpzuigao()
    js_resources1 = INLINE.render_js()
    css_resources1 = INLINE.render_css()
    script1, div1 = components(tu6)
    tu7=cpzuidi()
    js_resources2 = INLINE.render_js()
    css_resources2 = INLINE.render_css()
    script2, div2 = components(tu7)
    tu8=cpnxxllx()
    tu9=cp_ruzi()
    tu10=cp_gm()
    tu11=cp_dingwei()
    tu12=cp_dwxz()
    js_resources3 = INLINE.render_js()
    css_resources3 = INLINE.render_css()
    script3, div3 = components(tu12)
    tu13=cp_fl()
    tu14=cp_gz()
    return render_template("chanpin.html",
                           the_data1=tu1,
                           the_data2=tu2,
                           the_data3=tu3,
                           the_data4=tu4,
                           the_data5=tu5,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script1=script1,
                           plot_div1=div1,
                           the_data6=tu6,
                           the_data7=tu7,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script2=script2,
                           plot_div2=div2,
                           the_data8=tu8,
                           the_data9=tu9,
                           the_data10=tu10,
                           the_data11=tu11,
                           the_data12=tu12,
                           js_resources3=js_resources3,
                           css_resources3=css_resources3,
                           plot_script3=script3,
                           plot_div3=div3,
                           the_data13=tu13,
                           the_data14=tu14,
                           )

@app.route('/sheji',methods=["GET","POST"])
def sheji():
    tu1=sj_shu()
    tu2=sj_shengmap()
    tu3=sj_city_sl()
    tu4=sj_zhucitu()
    tu5=sjxinzi()
    tu6=sjzuigao()
    js_resources1 = INLINE.render_js()
    css_resources1 = INLINE.render_css()
    script1, div1 = components(tu6)
    tu7=sjzuidi()
    js_resources2 = INLINE.render_js()
    css_resources2 = INLINE.render_css()
    script2, div2 = components(tu7)
    tu8=sjnxxllx()
    tu9=sj_ruzi()
    tu10=sj_gm()
    tu11=sj_dingwei()
    tu12=sj_dwxz()
    js_resources3 = INLINE.render_js()
    css_resources3 = INLINE.render_css()
    script3, div3 = components(tu12)
    tu13=sj_fl()
    tu14=sj_gz()
    return render_template("sheji.html",
                           the_data1=tu1,
                           the_data2=tu2,
                           the_data3=tu3,
                           the_data4=tu4,
                           the_data5=tu5,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script1=script1,
                           plot_div1=div1,
                           the_data6=tu6,
                           the_data7=tu7,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script2=script2,
                           plot_div2=div2,
                           the_data8=tu8,
                           the_data9=tu9,
                           the_data10=tu10,
                           the_data11=tu11,
                           the_data12=tu12,
                           js_resources3=js_resources3,
                           css_resources3=css_resources3,
                           plot_script3=script3,
                           plot_div3=div3,
                           the_data13=tu13,
                           the_data14=tu14,
                           )

@app.route('/yunying',methods=["GET","POST"])
def yunying():
    tu1=yy_shu()
    tu2=yy_shengmap()
    tu3=yy_city_sl()
    tu4=yy_zhucitu()
    tu5=yyxinzi()
    tu6=yyzuigao()
    js_resources1 = INLINE.render_js()
    css_resources1 = INLINE.render_css()
    script1, div1 = components(tu6)
    tu7=yyzuidi()
    js_resources2 = INLINE.render_js()
    css_resources2 = INLINE.render_css()
    script2, div2 = components(tu7)
    tu8=yynxxllx()
    tu9=yy_ruzi()
    tu10=yy_gm()
    tu11=yy_dingwei()
    tu12=yy_dwxz()
    js_resources3 = INLINE.render_js()
    css_resources3 = INLINE.render_css()
    script3, div3 = components(tu12)
    tu13=yy_fl()
    tu14=yy_gz()
    return render_template("yunying.html",
                           the_data1=tu1,
                           the_data2=tu2,
                           the_data3=tu3,
                           the_data4=tu4,
                           the_data5=tu5,
                           js_resources1=js_resources1,
                           css_resources1=css_resources1,
                           plot_script1=script1,
                           plot_div1=div1,
                           the_data6=tu6,
                           the_data7=tu7,
                           js_resources2=js_resources2,
                           css_resources2=css_resources2,
                           plot_script2=script2,
                           plot_div2=div2,
                           the_data8=tu8,
                           the_data9=tu9,
                           the_data10=tu10,
                           the_data11=tu11,
                           the_data12=tu12,
                           js_resources3=js_resources3,
                           css_resources3=css_resources3,
                           plot_script3=script3,
                           plot_div3=div3,
                           the_data13=tu13,
                           the_data14=tu14,
                           )

if __name__ == '__main__':
    app.run()