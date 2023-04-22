# 导入模块
import operator

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import *
from bokeh.models import ColumnDataSource
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ChartType, SymbolType
# 导入bokeh模块
from bokeh.plotting import figure
# 颜色模块
from bokeh.transform import factor_cmap
from bokeh.models import FactorRange
import matplotlib.pyplot as plt
from pyecharts.charts import Tree
from pandas import DataFrame



def read_data():
    data = pd.read_excel('final_all_data.xlsx')
    return data

data=read_data()
# 7大行业树状图
def shu():
    shu_data = [
        {
            "name": "互联网行业",
            "children": [
                {"name": "技术",
                 "children": [
                     {"name": "后端开发（Java、C++、区块链）"}, {"name": "前端开发（web前端、flash、html）"},
                     {"name": "数据挖掘"}, {"name": "测试工程师"},
                     {"name": "运维工程师"}, {"name": "机器学习"}]},
                {"name": "产品",
                 "children": [
                     {"name": "产品经理"}, {"name": "产品助理"},
                     {"name": "移动产品经理"}, {"name": "电商产品经理"},
                     {"name": "产品专员"}, {"name": "数据产品经理"}
                 ]},
                {"name": "运营",
                 "children": [
                     {"name": "产品运营"}, {"name": "编辑"}, {"name": "用户运营"}, {"name": "文案策划"},
                     {"name": "内容运营"}, {"name": "新媒体运营"},
                     {"name": "数据运营"}
                 ]},
                {"name": "市场",
                 "children": [
                     {"name": "市场营销"}, {"name": "市场推广"}, {"name": "市场策划"}, {"name": "媒体公关"},
                     {"name": "广告投放"}, {"name": "网络营销"}, {"name": "品牌策划"},
                     {"name": "直播带货"}
                 ]},
                {"name": "设计",
                 "children": [
                     {"name": "UI设计"}, {"name": "平面设计"}, {"name": "网页设计"},
                     {"name": "交互设计"}, {"name": "视觉分析师"},
                     {"name": "游戏界面设计"}, {"name": "原画师"}
                 ]},
                {"name": "职能",
                 "children": [
                     {"name": "HR"}, {"name": "行政"}, {"name": "财务"}, {"name": "风控"}, {"name": "审计"},
                     {"name": "法务"}
                 ]},
                {"name": "销售",
                 "children": [
                     {"name": "销售经理"}, {"name": "销售顾问"}, {"name": "广告销售"}, {"name": "商务渠道"},
                     {"name": "电话销售"}, {"name": "渠道销售"}
                 ]},
            ]}
    ]
    hangyefenlei = (
        Tree(init_opts=opts.InitOpts(width="690px", height="650px", bg_color="rgba(156,168,184,0)"))
            .add("", data=shu_data, symbol="rect", symbol_size=12,
                 is_roam=True, initial_tree_depth=1,
                 label_opts=opts.LabelOpts(color='#965454', position='top', font_family='Arial'))
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='690px', height='650px'))
            .add(hangyefenlei, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        shuzhuang = "".join(f.readlines())
        return shuzhuang

def sheng_ditu():
    # 取出省份和省份数量做成字典
    sheng_list = list(data['省份'])
    sheng_dict = dict([[i, sheng_list.count(i)] for i in sheng_list])
    # 移除non值
    del sheng_dict['无']
    # 职位省份分布
    provice = list(sheng_dict.keys())
    provice_values = list(sheng_dict.values())
    pieces = [{"min": 2000, "max": 7500},
              {"min": 1000, "max": 1800},
              {"min": 300, "max": 500},
              {"min": 200, "max": 300},
              {"min": 100, "max": 200},
              {"min": 50, "max": 100},
              {"min": 2, "max": 50}
              ]
    # 画图
    sheng_map = (
        Map(init_opts=opts.InitOpts(
            width="850px", height="600px", bg_color="rgba(156,168,184,0)", ))
            .add("", data_pair=[list(z) for z in zip(provice, provice_values)],
                 maptype="china",
                 symbol="roundRect", is_selected=True, is_map_symbol_show=False)
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                pos_left='10%',
                pos_top='40%',
                is_piecewise=True,
                is_calculable=False,
                pos_bottom=100,
                pieces=pieces,
                range_color=["#b5c4b1", "#9ca8b8", "#965454"],
            )))
    grid = (
        Grid(init_opts=opts.InitOpts(width='850px', height='600px'))
            .add(sheng_map, grid_opts=opts.GridOpts(pos_right='3%', pos_left='3%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        shengditu = "".join(f.readlines())
        return shengditu

def city_ditu():
    # 取出省份和省份数量做成字典
    city_list = list(data['城市'])
    city_dict = dict([[i, city_list.count(i)] for i in city_list])
    # 移除non值
    del city_dict['无']
    # 职位城市分布
    cities = list(city_dict.keys())
    cities_values = list(city_dict.values())
    pieces = [{"min": 3000, "max": 7500},
              {"min": 1500, "max": 3000},
              {"min": 1000, "max": 1500},
              {"min": 200, "max": 1000},
              {"min": 50, "max": 200},
              {"min": 5, "max": 50},
              ]

    city_sum = (
        Geo(init_opts=opts.InitOpts(width="1000px", height="700px"))
            .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="#ececea"))
            .add(
            "",
            data_pair=[list(z) for z in zip(cities, cities_values)],
            type_=ChartType.EFFECT_SCATTER,
            symbol_size=8)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                pos_left='10%',
                pos_top='70%',
                is_piecewise=True,
                is_calculable=False,
                pieces=pieces,
                range_color=["#7b8b6f", "#8696a7", "#a27e7e"],
                range_size="8px",
            ),
        )

    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='850px', height='600px'))
            .add(city_sum, grid_opts=opts.GridOpts(pos_right='3%', pos_left='3%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        cityditu = "".join(f.readlines())
        return cityditu

def beijing_leibie():
    # 北京_类别数量
    bj_city = data[data["城市"] == "北京"]
    bj_list = list(bj_city['类别'])
    bj_dict = dict([[i, bj_list.count(i)] for i in bj_list])

    bj_leibie = sorted(bj_dict.keys())  # sorted(eg)
    bj_values = []
    for key in sorted(bj_dict):
        bj_values.append(bj_dict[key])
    bj_lb = (
        Bar(init_opts=opts.InitOpts(width='730px', height='450px'))
            .add_xaxis(bj_leibie)
            .add_yaxis('北京类别数量', bj_values, color='#b5c4b1')
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)
                                     ),
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                max_=2,
                range_color=['#7b8b6f']
            )
        )
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "rgb(0, 160, 221)",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right"),
        )
            .set_global_opts(title_opts=opts.TitleOpts(title="北京互联网行业各类别数量",
                                                       pos_left="center", pos_bottom=10,
                                                       title_textstyle_opts=opts.TextStyleOpts(font_size=12)),
                             ))
    grid = (
        Grid(init_opts=opts.InitOpts(width='730px', height='450px'))
            .add(bj_lb, grid_opts=opts.GridOpts(pos_right='3%', pos_left='10%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        bjlb = "".join(f.readlines())
        return bjlb

def top5_leibie():
    sh_city = data[data["城市"] == "上海"]
    sh_list = list(sh_city['类别'])
    sh_dict = dict([[i, sh_list.count(i)] for i in sh_list])
    sh_sorted = sorted(sh_dict.items(), key=lambda v: v[0])
    sh_values = []
    for i in sh_sorted:
        sh_values.append(i[1])

    sz_city = data[data["城市"] == "深圳"]
    sz_list = list(sz_city['类别'])
    sz_dict = dict([[i, sz_list.count(i)] for i in sz_list])
    sz_sorted = sorted(sz_dict.items(), key=lambda v: v[0])
    sz_values = []
    for i in sz_sorted:
        sz_values.append(i[1])

    gz_city = data[data["城市"] == "广州"]
    gz_list = list(gz_city['类别'])
    gz_dict = dict([[i, gz_list.count(i)] for i in gz_list])
    gz_sorted = sorted(gz_dict.items(), key=lambda v: v[0])
    gz_values = []
    for i in gz_sorted:
        gz_values.append(i[1])

    hz_city = data[data["城市"] == "杭州"]
    hz_list = list(hz_city['类别'])
    hz_dict = dict([[i, hz_list.count(i)] for i in hz_list])
    hz_sorted = sorted(hz_dict.items(), key=lambda v: v[0])
    hz_values = []
    for i in hz_sorted:
        hz_values.append(i[1])

    cd_city = data[data["城市"] == "成都"]
    cd_list = list(cd_city['类别'])
    cd_dict = dict([[i, cd_list.count(i)] for i in cd_list])
    cd_sorted = sorted(cd_dict.items(), key=lambda v: v[0])
    cd_values = []
    for i in cd_sorted:
        cd_values.append(i[1])

    multi_list = map(list, zip(sh_values, sz_values, gz_values, hz_values, cd_values))
    mul_list = list(multi_list)
    # 数据
    leibie = ["产品", "市场", "职能", "运营", "销售", "技术", "设计"]
    top5_city = ['上海', '深圳', '广州', '杭州', '成都']
    leibei_city_data = {
        'top5_city': top5_city,
        '产品': mul_list[0],
        '市场': mul_list[1],
        '职能': mul_list[2],
        '运营': mul_list[3],
        '销售': mul_list[4],
        '技术': mul_list[5],
        '设计': mul_list[6],
    }
    source = ColumnDataSource(data=leibei_city_data)
    color = ["#8696a7", "#9ca8b8", "#ececea", "#fffaf4", "#b5c4b1", "#96a48b", "#7b8b6f"]
    # 交互式数据
    TOOLTIPS = [
        ("$name", "@top5_city:@$name")]
    # 画布
    p = figure(x_range=top5_city,
               plot_height=450,plot_width=730,
               title="各类别数量差异",
               tooltips=TOOLTIPS)
    # 绘图,直接堆叠类别数据
    p.vbar_stack(leibie, x='top5_city', width=0.9, color=color,
                 source=source, legend_label=["产品", "市场", "职能", "运营", "销售", "技术", "设计"], name=leibie)
    # 其他
    p.y_range.start = 0
    p.y_range.end = 3750
    # 边距
    p.yaxis.ticker = [0, 150, 350, 600, 800, 1200, 1500, 1800, 2200, 2600, 3000, 3200, 3750]
    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.axis.minor_tick_line_color = None
    p.outline_line_color = None
    # 显示
    return p

def leibie_xinzi():
    xi_df = data.loc[data["平均薪资（千/月）"] < 95]
    # 平均数
    pjxz_lb = xi_df.groupby('类别')['平均薪资（千/月）'].mean().to_frame('平均薪资（千/月）').reset_index()
    pjxz_lb['平均薪资（千/月）'] = pjxz_lb['平均薪资（千/月）'].round(decimals=1)
    pjxz_lb = pjxz_lb.sort_values('平均薪资（千/月）', ascending=False)[:10]
    # 中位数
    zwxz_lb = xi_df.groupby('类别')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    zwxz_lb['平均薪资（千/月）'] = zwxz_lb['平均薪资（千/月）'].round(decimals=1)
    zwxz_lb = zwxz_lb.sort_values('平均薪资（千/月）', ascending=False)[:10]
    x_data = pjxz_lb['类别'].values.tolist()
    pj_y_data = pjxz_lb['平均薪资（千/月）'].values.tolist()
    zw_y_data = zwxz_lb['平均薪资（千/月）'].values.tolist()
    # 准备x轴数据
    xin_zi = ['薪资平均', '薪资中位']
    x = [(lei, wages) for lei in x_data for wages in xin_zi]
    # 准备y轴数据
    y = sum(zip(pj_y_data, zw_y_data), ())
    # 准备ColumnDataSource
    source = ColumnDataSource(data=dict(x_axis=x, y_counts=y))
    # 准备tooltips 鼠标移入显示数据
    TOOLTIPS = [
        ("counts", "@y_counts" + "（千/月）"),
        ("描述", "@x_axis")]
    color = ["#9ca8b8", "#b5c4b1"]
    # 画布
    p2 = figure(
        x_range=FactorRange(*x),
        plot_height=450,plot_width=730,
        title="7大类别薪资平均值及中位数",
        tooltips=TOOLTIPS
    )
    # 绘制图形 vbar 垂直柱状图
    p2.vbar(
        x='x_axis',
        top="y_counts",
        width=0.8,
        source=source,
        fill_color=factor_cmap('x_axis',
                               palette=color,
                               factors=xin_zi,
                               start=1, end=2)
    )
    p2.y_range.start = 0
    p2.x_range.range_padding = 0.1
    p2.xaxis.major_label_orientation = 1
    # p.yaxis.axis_label = "薪资（千/月）"  # y轴名称
    p2.axis.axis_label_text_font_style = 'bold'
    p2.yaxis.major_label_text_font_size = '14px'
    return p2

def xinzi_sl():
    # 取出薪资数量做成字典
    xin = data.loc[data["平均薪资（千/月）"] < 90]
    xi_df = xin[~xin['省份'].isin(["无"])]
    shengfen_average = xi_df.groupby('省份')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    shengfen_average['平均薪资（千/月）'] = shengfen_average['平均薪资（千/月）'].round(decimals=1)
    shengfen_average = shengfen_average.sort_values('平均薪资（千/月）', ascending=False)

    x_data = shengfen_average['省份'].values.tolist()
    y_data = shengfen_average['平均薪资（千/月）'].values.tolist()

    line = Line(init_opts=opts.InitOpts(width='750px', height='400px'))
    line.add_xaxis(x_data)
    line.add_yaxis('平均薪资（千/月）', y_data, color="#9ca8b8")
    grid = (
        Grid(init_opts=opts.InitOpts(width='730px', height='450px'))
            .add(line, grid_opts=opts.GridOpts(pos_right='3%', pos_left='10%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        sf_xz = "".join(f.readlines())
        return sf_xz

def xinzi_zw():
    xi_df2 = data.loc[data["最高薪资（千/月）"] < 120]
    # 最低平均薪资
    pjzd_lb = xi_df2.groupby('类别')['最低薪资（千/月）'].median().to_frame('最低薪资（千/月）').reset_index()
    pjzd_lb['最低薪资（千/月）'] = pjzd_lb['最低薪资（千/月）'].round(decimals=1)
    pjzd_lb = pjzd_lb.sort_values('最低薪资（千/月）', ascending=False)[:10]
    # 最高平均薪资
    pjzg_lb = xi_df2.groupby('类别')['最高薪资（千/月）'].median().to_frame('最高薪资（千/月）').reset_index()
    pjzg_lb['最高薪资（千/月）'] = pjzg_lb['最高薪资（千/月）'].round(decimals=1)
    pjzg_lb = pjzg_lb.sort_values('最高薪资（千/月）', ascending=False)[:10]
    x_data = pjzd_lb['类别'].values.tolist()
    zd_y_data = pjzd_lb['最低薪资（千/月）'].values.tolist()
    zg_y_data = pjzg_lb['最高薪资（千/月）'].values.tolist()
    multi_list2 = map(list, zip(x_data, zd_y_data, zg_y_data))
    mul_list2 = list(multi_list2)
    mul_data = DataFrame(mul_list2)
    mul_data.rename(columns={0: '类别', 1: '最低薪资', 2: '最高薪资'}, inplace=True)  # 注意这里0和1都不是字符串
    c = {'蓝色': '#7a7281', '绿色': '#7b8b6f', '深灰色': '#656565', '雾蓝色': '#dfd7d7'}
    mul_data['变化'] = mul_data.iloc[:, 2] - mul_data.iloc[:, 1]
    # 使用「面向对象」的方法画图，定义图片的大小
    fig, ax = plt.subplots(figsize=(10, 6))
    # 设置背景颜色
    fig.set_facecolor('w')
    ax.set_facecolor('w')
    # 定义范围
    rng = range(1, len(mul_data.index) + 1)
    rng_pos = list(map(lambda x: x + 1, mul_data[mul_data['变化'] >= 0].index))
    # 绘制哑铃图中间的线条
    ax.hlines(y=rng_pos, xmin=mul_data[mul_data['变化'] >= 0].iloc[:, 1], xmax=mul_data[mul_data['变化'] >= 0].iloc[:, 2],
              color=c['雾蓝色'], zorder=1, lw=5)
    # 绘制哑铃图两头的圆点
    ax.scatter(mul_data.iloc[:, 1], rng, color=c['蓝色'], label=xi_df2.columns[1], s=200, zorder=4)
    ax.scatter(mul_data.iloc[:, 2], rng, color=c['绿色'], label=xi_df2.columns[2], s=200, zorder=4)
    # 显示数据标签
    for i, (txt1, txt2) in enumerate(zip(mul_data.iloc[:, 1], mul_data.iloc[:, 2])):
        ax.annotate(mul_data.columns[1] + ' ' + '{0}'.format(float(txt1)) + '千/月',
                    (mul_data.iloc[:, 1][i], mul_data.index[i] + 0.7), color=c['蓝色'], ha='center', va='center',
                    fontsize=14)
        ax.annotate(mul_data.columns[2] + ' ' + '{0}'.format(float(txt2)) + '千/月',
                    (mul_data.iloc[:, 2][i], mul_data.index[i] + 1.3), color=c['绿色'], ha='center', va='center',
                    fontsize=14)
        # 设置 Y 轴标签
    plt.yticks(rng, mul_data.iloc[:, 0], ha='left', color=c['深灰色'], size=18)
    plt.xticks(ha='center', color=c['深灰色'], size=16)
    # 隐藏边框
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.set_xlim(0, 35)
    ax.xaxis.set_visible(False)
    ax.invert_yaxis()
    return plt

def qu(city):
    shai=data[['类别','城市','平均薪资（千/月）']]
    quzhi=shai[['类别','城市','平均薪资（千/月）']]
    re_quzhi=quzhi.rename(columns={'平均薪资（千/月）':'平均薪资'})
    re_quzhi2=re_quzhi[(re_quzhi['城市'] == city)]
    divorces=re_quzhi2.groupby('类别')['平均薪资'].median().to_frame('平均薪资').reset_index()
    divorces['平均薪资']=divorces['平均薪资'].round(decimals=1) #四舍五入
#     divorces  =divorces.sort_values('平均薪资',ascending=False)
    y_data = divorces['平均薪资'].values.tolist()
    return y_data

def top5xz_lb():
    shai_leibie = ['产品', '市场', '技术', '职能', '设计', '运营', '销售']
    shai_city = ["北京", "上海", "深圳", "广州", "杭州"]
    source = ColumnDataSource(data=dict(
        lb_shai=shai_leibie,
        北京=qu(city=shai_city[0]),
        上海=qu(city=shai_city[1]),
        深圳=qu(city=shai_city[2]),
        广州=qu(city=shai_city[3]),
        杭州=qu(city=shai_city[4]),
    ))
    # 设置工具条
    TOOLS = 'pan,wheel_zoom,box_zoom,reset,save'
    # 画布
    p = figure(x_range=shai_leibie, y_range=(7, 30), tools=TOOLS, plot_width=730, plot_height=500,
               tooltips='<font face="Arial" size="0.2">$name @$name{0.0}（千/月）</font>')
    # 定义画布的内容（坐标轴刻度）models
    p.hover.mode = 'vline'
    # 横轴坐标轴数据设置
    p.yaxis.axis_label = '薪资'
    p.title.text = '职位数量TOP5城市各类别薪资中位数'
    # 绘图  字典取值dict_name["year"]
    p.line('lb_shai', '北京', color='#965454', line_width=2, source=source, name="北京", legend_label='_北京_')
    p.line('lb_shai', '上海', color='#7a7281', line_width=2, source=source, name="上海", legend_label='_上海_')
    p.line('lb_shai', '深圳', color='#656565', line_width=2, source=source, name="深圳", legend_label='_深圳_', line_dash="4 4")
    p.line('lb_shai', '广州', color='#8696a7', line_width=2, source=source, name="广州", legend_label='_广州_')
    p.line('lb_shai', '杭州', color='#7b8b6f', line_width=2, source=source, name="杭州", legend_label='_杭州_')
    # 显示
    return p

def xueli():
    l1 = (
        Liquid()
            .add("占比", [0.02, 0.01],
                 center=["20%", "60%"],
                 color=['#7a7281'],
                 label_opts=opts.LabelOpts(
                     font_size=16,
                     formatter=JsCode(
                         """function (param) {
                                 return ('硕士及以上：'+Math.floor(param.value * 10000) / 100) + '%';
                             }"""), position="inside")))

    l2 = Liquid().add(
        "占比",
        [0.7, 0.2, 0.5, 0.3],
        center=["40%", "60%"],
        color=['#a27e7e'],
        label_opts=opts.LabelOpts(
            font_size=20,
            formatter=JsCode(
                """function (param) {
                        return ('本科：'+Math.floor(param.value * 10000) / 100) + '%';
                    }"""), position="inside"))

    l3 = (
        Liquid()
            .add("占比", [0.17, 0.15, 0.1],
                 center=["60%", "60%"], is_outline_show=True,
                 color=['#8696a7'],
                 label_opts=opts.LabelOpts(
                     font_size=20,
                     formatter=JsCode(
                         """function (param) {
                                 return ('大专：'+Math.floor(param.value * 10000) / 100) + '%';
                             }"""), position="inside", )))

    l4 = Liquid().add(
        "占比",
        [0.12, 0.05],
        center=["80%", "60%"],
        color=['#b5c4b1'],
        label_opts=opts.LabelOpts(
            font_size=20,
            formatter=JsCode(
                """function (param) {
                        return ('不限：'+Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ),
    )
    grid = Grid(init_opts=opts.InitOpts(width='860px', height="260px")).add(l1, grid_opts=opts.GridOpts()).add(l2,
                                                                                                               grid_opts=opts.GridOpts()).add(
        l3, grid_opts=opts.GridOpts()).add(l4, grid_opts=opts.GridOpts())
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        xl = "".join(f.readlines())
        return xl

def xl_xz():
    xueli_data = data[["学历要求", "平均薪资（千/月）", "类别"]]
    xueli_data = xueli_data.loc[xueli_data["平均薪资（千/月）"] < 95]
    xueli_data["学历要求"] = xueli_data["学历要求"].str.replace("博士", "硕士")
    xueli_data["学历要求"] = xueli_data["学历要求"].str.replace("硕士", "硕士及以上")
    # xueli_data=xueli_data.rename(columns={0:'学历要求',1:'平均薪资',2:'类别'},inplace=True)
    xueli_data.columns = ["xueli", "xinzi", "leibie"]
    # 数据整理
    palette = ["#b5c4b1", "#7a7281", "#9ca8b8", "#a27e7e"]
    group = xueli_data.groupby(['xueli', 'leibie'])
    index_cmap = factor_cmap('xueli_leibie',
                             palette=palette,
                             factors=(xueli_data.xueli.unique()),
                             end=1)
    # 画布
    xueli_xinzi = figure(plot_height=450,
                         plot_width=730,
                         x_range=group,
                         title="7大类型不同学历薪资水平",
                         tooltips=[("平均薪资", "@xinzi_mean" + '（千/月）'), ("学历, 类别", "@xueli_leibie")])
    # 绘图
    xueli_xinzi.vbar(x='xueli_leibie',
                     top='xinzi_mean',
                     width=0.8,
                     source=group,
                     line_color="white",
                     fill_color=index_cmap)
    # 其他
    xueli_xinzi.y_range.start = 0
    xueli_xinzi.xgrid.grid_line_color = None
    # p.xaxis.axis_label = "7大类型不同学历薪资水平展示"
    xueli_xinzi.xaxis.major_label_orientation = 1.2
    xueli_xinzi.outline_line_color = "#fffaf4"
    # 显示
    return xueli_xinzi

def gznx():
    l1 = (
        Liquid()
            .add("占比", [0.134, 0.12, 0.05], shape=SymbolType.DIAMOND, is_outline_show=False,
                 center=["17%", "60%"],
                 color=['#9ca8b8'],
                 label_opts=opts.LabelOpts(
                     font_size=12,
                     formatter=JsCode(
                         """function (param) {
                                 return ('5年以上：'+Math.floor(param.value * 10000) / 100) + '%';
                             }"""
                     ),
                     position="inside",
                 ), )
            .set_global_opts(title_opts=opts.TitleOpts())
    )

    l2 = Liquid().add(
        "占比",
        [0.308, 0.2, 0.05], shape=SymbolType.DIAMOND, is_outline_show=False,
        center=["34.4%", "60%"],
        color=['#8696a7'],
        label_opts=opts.LabelOpts(
            font_size=12,
            formatter=JsCode(
                """function (param) {
                        return ('3-5年：'+Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ),
    )

    l3 = (
        Liquid()
            .add("占比", [0.207, 0.18, 0.08], shape=SymbolType.DIAMOND, is_outline_show=False,
                 center=["52%", "60%"],
                 color=['#fffaf4'],
                 label_opts=opts.LabelOpts(
                     font_size=12,
                     formatter=JsCode(
                         """function (param) {
                                 return ('1-3年：'+Math.floor(param.value * 10000) / 100) + '%';
                             }"""
                     ),
                     position="inside",  # 标题在内
                 ), )
            .set_global_opts(title_opts=opts.TitleOpts())
    )

    l4 = Liquid().add(
        "占比",
        [0.12, 0.09, 0.03], shape=SymbolType.DIAMOND, is_outline_show=False,
        center=["69%", "60%"],
        color=['#96a48b'],
        label_opts=opts.LabelOpts(
            font_size=12,
            formatter=JsCode(
                """function (param) {
                        return ('不限：'+Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ),
    )

    l5 = Liquid().add(
        "占比",
        [0.132, 0.08, 0.03], shape=SymbolType.DIAMOND, is_outline_show=False,
        center=["86%", "60%"],
        color=['#a6a6a8'],
        label_opts=opts.LabelOpts(
            font_size=12,
            formatter=JsCode(
                """function (param) {
                        return ('在校/应届：'+Math.floor(param.value * 10000) / 100) + '%';
                    }"""
            ),
            position="inside",
        ),
    )

    grid = Grid(init_opts=opts.InitOpts(width='860px', height="260px")).add(l1, grid_opts=opts.GridOpts()).add(l2,
                                                                                                               grid_opts=opts.GridOpts()).add(
        l3, grid_opts=opts.GridOpts()).add(l4, grid_opts=opts.GridOpts()).add(l5, grid_opts=opts.GridOpts())
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        gongzuo = "".join(f.readlines())
        return gongzuo

def rz_gm():
    # 获取不同融资情况的数量
    ruzi_num = data['融资情况'].value_counts()
    ruzi_s = ruzi_num.index.tolist()
    num_s = [i for i in ruzi_num]
    data_pair1 = [list(z) for z in zip(ruzi_s, num_s)]

    # 获取不同公司规模的数量
    gongsi_num = data['公司规模'].value_counts()
    gongsi_e = gongsi_num.index.tolist()
    num_e = [i for i in gongsi_num]
    data_pair2 = [list(z) for z in zip(gongsi_e, num_e)]

    # 开始画图
    ruzi_bar = (
        Bar()
            .add_xaxis(ruzi_s)
            .add_yaxis("", num_s, color='#b5c4b1')
            .set_global_opts(title_opts=opts.TitleOpts(title="不同公司融资情况岗位数量", pos_left="15%",
                                                       title_textstyle_opts=opts.TextStyleOpts(font_size="16px"), ))
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="average", type_="average")]))
    )
    gongsi_bar = (
        Bar()
            .add_xaxis(gongsi_e)
            .add_yaxis("", num_e, color='#9ca8b8')
            .set_global_opts(title_opts=opts.TitleOpts(title="不同公司规模岗位数量",
                                                       pos_right="20%",
                                                       title_textstyle_opts=opts.TextStyleOpts(font_size="16px")))
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=False),
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_="max", name="max")
                , opts.MarkPointItem(name="min", type_="min")]))
    )

    ruzi_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair1,
                 rosetype="area", center=['25%', "75%"], radius=["10%", '25%'])
            .set_colors(["#b5c4b1", "#8696a7", "#9ca8b8", "#ececea", "#7a7281", "#fffaf4", "#a27e7e", "#ead0d1"])
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同公司融资情况岗位数量占比",
                                                       pos_left="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色
                                                       title_textstyle_opts=opts.TextStyleOpts(font_size="16px")),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))
    gongsi_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair2, rosetype="area", center=['75%', "75%"], radius=["10%", '25%'])
            .set_colors(["#b5c4b1", "#8696a7", "#9ca8b8", "#ececea", "#7a7281", "#fffaf4", "#a27e7e", "#ead0d1"])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同公司规模岗位数量占比",
                                                       pos_right="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色
                                                       title_textstyle_opts=opts.TextStyleOpts(font_size="16px"),
                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False),

                             ))

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(ruzi_bar, grid_opts=opts.GridOpts(pos_right="60%", pos_bottom='60%'))
    grid.add(gongsi_bar, grid_opts=opts.GridOpts(pos_left="60%", pos_bottom='60%'))
    grid.add(ruzi_pie, grid_opts=opts.GridOpts(pos_right="60%", pos_top="60%"))  # 改center
    grid.add(gongsi_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='60%'))
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        rongziguimo = "".join(f.readlines())
        return rongziguimo

def dw_xz():
    gsdw = pd.concat([data, data['公司定位'].str.split('、', expand=True)], axis=1).drop('公司定位', axis=1)
    gsdw.rename(columns={0: '公司定位'}, inplace=True)
    gsdw1 = pd.concat([gsdw, gsdw['公司定位'].str.split('，', expand=True)], axis=1).drop('公司定位', axis=1)
    gsdw1.rename(columns={0: '公司定位'}, inplace=True)
    salary_average = gsdw.groupby('公司定位')['平均薪资（千/月）'].mean().to_frame('平均薪资（千/月）').reset_index()
    salary_average['平均薪资（千/月）'] = salary_average['平均薪资（千/月）'].round(decimals=1)
    salary_average = salary_average.sort_values('平均薪资（千/月）', ascending=False)[:15]
    factors = salary_average['公司定位'].values.tolist()
    x = salary_average['平均薪资（千/月）'].values.tolist()
    fig = figure(
        title="所属公司定位平均薪资(千/月)",
        toolbar_location=None,
        tools="hover",
        y_range=factors,
        x_range=[0, 35],
        tooltips=[('平均薪资', '￥@x' + "（千/月）")],
        plot_width=750,
        plot_height=500)

    fig.segment(0, factors, x, factors, line_width=3, line_color="#AA6767")
    fig.circle(x, factors, size=18, fill_color="#8389FF", line_color="#AA6767", line_width=4)
    fig.xgrid.grid_line_color = None
    fig.ygrid.grid_line_color = None
    return fig

fuli_cppx=[('团队', 2694),
 ('氛围', 1899),
 ('双休', 1586),
 ('六险一金', 1309),
 ('发展', 1150),
 ('空间', 1139),
 ('健身', 1130),
 ('五险一金', 1120),
 ('瑜伽', 1107),
 ('福利', 1043),
 ('晋升', 950),
 ('周末', 924),
 ('工作', 912),
 ('弹性', 820),
 ('管理', 707),
 ('带薪', 678),
 ('免费', 645),
 ('项目', 633),
 ('扁平', 591),
 ('平台', 489),
 ('节日', 478),
 ('股票', 460),
 ('奖金', 437),
 ('餐补', 433),
 ('下午茶', 408),
 ('成长', 377),
 ('行业', 364),
 ('扁平化', 362),
 ('体检', 358),
 ('大牛', 353),
 ('稳定', 349),
 ('年终奖', 338),
 ('定期', 312),
 ('三餐', 303),
 ('办公', 296),
 ('技术', 286),
 ('业务', 277),
 ('环境', 263),
 ('团建', 259),
 ('年底', 246),
 ('绩效奖金', 245),
 ('提成', 242),
 ('期权下午茶', 240),
 ('领导', 234),
 ('节假日', 233),
 ('加班', 232),
 ('氛围下午茶', 232),
 ('nice', 227),
 ('培训', 226),
 ('补贴', 226),
 ('员工', 224),
 ('轻松', 224),
 ('旅游', 218),
 ('前景', 210),
 ('薪资', 209),
 ('双薪', 206),
 ('产品', 206),
 ('期权', 202),
 ('发展前景', 202),
 ('福利待遇', 199),
 ('机会', 189),
 ('管理下午茶', 185),
 ('年轻', 184),
 ('企业', 179),
 ('补充', 171),
 ('五险一金下午茶', 163),
 ('零食', 162),
 ('带队', 161),
 ('时间', 160),
 ('交通', 151),
 ('租房', 147),
 ('核心', 142),
 ('薪酬', 139),
 ('待遇', 136),
 ('学习', 135),
 ('提供', 133),
 ('一金', 128),
 ('优秀', 120),
 ('打卡', 120),
 ('丰厚', 119),
 ('补助', 117),
 ('年终', 115),
 ('班车', 114),
 ('年终奖金', 113),
 ('调薪', 113),
 ('岗位', 113),
 ('自由', 109),
 ('快速', 107),
 ('完善', 105),
 ('二金', 105),
 ('公积金', 103),
 ('法定', 102),
 ('激励', 101),
 ('午餐', 100),
 ('互联网', 99),
 ('季度', 97),
 ('底薪', 97),
 ('转正', 96),
 ('全额', 95),
 ('专业', 94),
 ('地铁', 94),
 ('独角兽', 92),
 ('游戏', 92),
 ('实习', 91),
 ('带薪休假下午茶', 90),
 ('空间五险一金', 90),
 ('背景', 88),
 ('医疗', 87),
 ('广阔', 85),
 ('绩效', 85),
 ('上市公司', 85),
 ('导师', 84),
 ('上升', 84),
 ('入职', 82),
 ('职业', 78),
 ('文化', 78),
 ('三餐下午茶', 76),
 ('机制', 76),
 ('氛围团队', 74),
 ('运营', 74),
 ('食堂', 73),
 ('五险', 72),
 ('年轻化', 72),
 ('优质', 71),
 ('大厂', 71),
 ('资源', 71),
 ('晚餐', 70),
 ('客户', 70),
 ('空间发展', 70),
 ('市场', 70),
 ('工作制', 69),
 ('销售', 69),
 ('发挥', 69),
 ('体系', 68),
 ('健身房', 68),
 ('七险', 68),
 ('社保', 68),
 ('用户', 67),
 ('头部', 67),
 ('科技', 67),
 ('假期', 67),
 ('老板', 66),
 ('上班', 66),
 ('空间下午茶', 64),
 ('带薪休假', 64),
 ('高薪', 64),
 ('氛围五险一金', 63),
 ('包餐', 63),
 ('全勤奖', 63),
 ('上市', 63),
 ('住宿', 62),
 ('双休五险一金', 62),
 ('优厚', 62),
 ('竞争力', 62),
 ('13', 62),
 ('实力', 61),
 ('领先', 61),
 ('海外', 61),
 ('试用期', 61),
 ('购买', 61),
 ('多多', 61),
 ('长期', 60),
 ('成熟', 59),
 ('股权', 59),
 ('每年', 59),
 ('空间团队', 59),
 ('带教', 58),
 ('齐全', 57),
 ('周边', 57),
 ('职位', 57),
 ('通讯', 56),
 ('补贴下午茶', 55),
 ('福利五险一金', 55),
 ('赛道', 55),
 ('生日', 53),
 ('电商', 52),
 ('空间六险一金', 51),
 ('不定期', 51),
 ('品牌', 51),
 ('金融', 50),
 ('房补', 50),
 ('出国', 50),
 ('创业', 49),
 ('通道', 49),
 ('丰富', 49),
 ('良好', 49),
 ('媒体', 48),
 ('500', 48),
 ('奖励', 48),
 ('咖啡', 47),
 ('领域', 47),
 ('前沿', 47),
 ('融洽', 47),
 ('内部', 47),
 ('氛围六险一金', 46),
 ('培养', 45),
 ('能力', 45),
 ('分红', 45),
 ('高额', 45),
 ('收入', 45),
 ('活动', 44),
 ('商业保险', 44),
 ('创新', 44),
 ('空间平台', 44),
 ('月度', 44),
 ('上下班', 43),
 ('缴纳', 43),
 ('活力', 43),
 ('经验', 43),
 ('灵活', 43),
 ('同事', 43),
 ('和谐', 43),
 ('指导', 42),
 ('研发', 42),
 ('水果', 41),
 ('牛人', 38),
 ('大佬', 38),
 ('自研', 38),
 ('空间周末', 37),
 ('高速', 37),
 ('提升', 37),
 ('包吃', 37),
 ('超长', 37),
 ('餐费', 37),
 ('国企', 36),
 ('健康', 36),
 ('数据', 36),
 ('气氛', 36),
 ('专业培训', 36),
 ('双休团队', 36),
 ('就近', 36),
 ('体检五险一金', 35),
 ('服务', 35),
 ('挑战', 34),
 ('便利', 34),
 ('福利六险一金', 34),
 ('规范', 34),
 ('证明', 33),
 ('投资', 33),
 ('五险一金五险一金', 33),
 ('福利团队', 33),
 ('国家', 33),
 ('团队五险一金', 33),
 ('部门', 33),
 ('视野', 33),
 ('开放', 33),
 ('生日会', 32),
 ('简单', 32),
 ('工资', 32),
 ('工作餐', 32),
 ('工时', 32),
 ('两次', 32),
 ('空间双休', 32),
 ('3D', 32),
 ('云集', 31),
 ('氛围发展', 31),
 ('一日三餐', 31),
 ('设计', 31),
 ('透明', 30),
 ('规模', 30),
 ('礼金', 30),
 ('活跃', 30),
 ('潜力', 30),
 ('空间上市公司', 30),
 ('15', 30),
 ('出差', 29),
 ('集团', 29),
 ('人才', 29),
 ('旅行', 29),
 ('多次', 28),
 ('数字', 28),
 ('六险', 28),
 ('外企', 28),
 ('工业', 28),
 ('管理五险一金', 28),
 ('病假', 28),
 ('餐饮', 27),
 ('高效', 27),
 ('各类', 27),
 ('早餐', 27),
 ('加班费', 27),
 ('升职', 27),
 ('人性化', 27),
 ('购车', 27),
 ('机器人', 27),
 ('视觉', 27),
 ('分配', 27),
 ('朝阳', 26),
 ('朝九晚', 26),
 ('管理团队', 26),
 ('高温', 26),
 ('合作', 26),
 ('津贴', 26),
 ('增长', 26),
 ('购房', 26),
 ('国际化', 26),
 ('带薪休假六险一金', 26),
 ('浙大', 26),
 ('多薪', 25),
 ('双休周末', 25),
 ('精英', 25),
 ('正编', 25),
 ('迅速', 25),
 ('团队团队', 25),
 ('福利平台', 25),
 ('业绩', 24),
 ('明确', 24),
 ('方向', 24),
 ('舒适', 24),
 ('14', 24),
 ('宿舍', 24),
 ('福利上市公司', 24),
 ('旅游五险一金', 24),
 ('氛围平台', 24),
 ('全薪', 24),
 ('无责', 24),
 ('聚餐', 24),
 ('房补餐', 24),
 ('生日礼物', 24),
 ('空间晋升', 23),
 ('带队下午茶', 23),
 ('工作下午茶', 23),
 ('技能', 23),
 ('资深', 23),
 ('90', 23),
 ('空间发展前景', 23),
 ('过节', 23),
 ('无限', 23),
 ('未来', 23),
 ('优惠政策商业保险', 23),
 ('用户下午茶', 22),
 ('假日', 22),
 ('一对一', 22),
 ('打车', 22),
 ('礼品', 22),
 ('机构', 22),
 ('腾讯', 22),
 ('八险', 22),
 ('食宿', 22),
 ('打折', 22),
 ('饭补', 22),
 ('员工福利', 22),
 ('医疗保险', 22),
 ('氛围上市公司', 21),
 ('氛围扁平化', 21),
 ('人工智能', 21),
 ('盈利', 21),
 ('平台五险一金', 21),
 ('智能', 21),
 ('浓厚', 21),
 ('带薪五险一金', 21),
 ('渠道', 21),
 ('价值', 21),
 ('财务', 21)]
def gwfl():
    fuli = (
        WordCloud()
            # 主要是这里改了下，shape=（'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'）可选。
            .add("", fuli_cppx, word_size_range=[20, 90])
            .set_global_opts(title_opts=opts.TitleOpts())
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='800px', height='500px'))
            .add(fuli, grid_opts=opts.GridOpts(pos_right='1%', pos_left='3%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        gw_fl = "".join(f.readlines())
        return gw_fl

yy=[('负责', 1.0),
 ('运营', 0.8517302983004037),
 ('能力', 0.8500351355207256),
 ('经验', 0.6824027552420935),
 ('产品', 0.6351300225241785),
 ('沟通', 0.6247070369362226),
 ('用户', 0.6023738821219032),
 ('内容', 0.5982747405439235),
 ('团队', 0.5935855684354694),
 ('数据', 0.5180947700669462),
 ('分析', 0.5146237893480027),
 ('行业', 0.47662019821101226),
 ('平台', 0.47589651856444176),
 ('需求', 0.47534720965380406),
 ('优化', 0.46055804263062594),
 ('策划', 0.45492698943400695),
 ('活动', 0.4233223790551599),
 ('策略', 0.415848501611258),
 ('提升', 0.4051296197614822),
 ('项目', 0.4012593125570553),
 ('制定', 0.3749070083115946),
 ('专业', 0.36741669690581213),
 ('管理', 0.3659641876519469),
 ('目标', 0.3280567230715234),
 ('合作', 0.31957028320055697),
 ('职位', 0.3102810146338856),
 ('媒体', 0.3087717841236755),
 ('执行', 0.2913856999106787),
 ('落地', 0.29108637701119233),
 ('方案', 0.2852121652711057),
 ('视频', 0.28169119830344597),
 ('撰写', 0.2768909416549979),
 ('学习', 0.2758278727778834),
 ('文案', 0.27412450463029575),
 ('独立', 0.27097239346401886),
 ('设计', 0.27025944687409914),
 ('营销', 0.2585444384865458),
 ('资源', 0.2485211302508464),
 ('挖掘', 0.24766942945785117),
 ('市场', 0.24678431674235238),
 ('推广', 0.24204081347822887),
 ('互联网', 0.24099145468616795),
 ('职责', 0.23572140898261776),
 ('协作', 0.23536193682681614),
 ('协助', 0.23054774336433237),
 ('问题', 0.2303583752670681),
 ('维护', 0.22899960390855376),
 ('输出', 0.2238267976260162),
 ('规划', 0.22218998146245642),
 ('协调', 0.22187439854889215)]
cp=[('负责', 1.0),
 ('产品', 0.9828777172142323),
 ('能力', 0.8389266382948539),
 ('需求', 0.8151845462958417),
 ('设计', 0.7684764296502619),
 ('经验', 0.7284798960697255),
 ('沟通', 0.7248171355637048),
 ('分析', 0.7189121574523838),
 ('用户', 0.6179275117910479),
 ('团队', 0.5948828519492999),
 ('项目', 0.5905651400372843),
 ('数据', 0.5474441876413682),
 ('优化', 0.484530134900562),
 ('规划', 0.4745124568625211),
 ('运营', 0.4457568804684997),
 ('行业', 0.44272752891306333),
 ('开发', 0.4138308624747115),
 ('协调', 0.3977333613398284),
 ('系统', 0.39244721658230797),
 ('管理', 0.3756901286993115),
 ('功能', 0.37430916076942233),
 ('专业', 0.35641341890420536),
 ('体验', 0.35511095020263),
 ('落地', 0.34921538893601034),
 ('流程', 0.33547384013309745),
 ('技术', 0.3310134008494485),
 ('产品设计', 0.3295746223890505),
 ('平台', 0.3282832043155451),
 ('调研', 0.32424596675049744),
 ('方案', 0.3192359267832091),
 ('学习', 0.31793060270720486),
 ('问题', 0.3161223444542874),
 ('提升', 0.30697986880311934),
 ('迭代', 0.29379047353282184),
 ('独立', 0.28082590692990766),
 ('合作', 0.27630642030584235),
 ('跟进', 0.27006799280090565),
 ('市场', 0.2678540247879894),
 ('上线', 0.2665396696061901),
 ('互联网', 0.26454491112018896),
 ('客户', 0.2619398151741765),
 ('工具', 0.25935592839192956),
 ('测试', 0.25864984241149347),
 ('制定', 0.25750998441659545),
 ('理解', 0.2539172082209609),
 ('推进', 0.25051700090213525),
 ('原型', 0.2477194178459741),
 ('逻辑', 0.24558634131976367),
 ('协作', 0.24415282885693035),
 ('场景', 0.23896810178156677)]
js=[('负责', 1.0),
 ('开发', 0.9434210000168699),
 ('能力', 0.861561320199519),
 ('技术', 0.7585605454934402),
 ('经验', 0.749725523071853),
 ('设计', 0.7266027027253599),
 ('优化', 0.6890501774827604),
 ('团队', 0.6798884763966527),
 ('项目', 0.6548924558709842),
 ('沟通', 0.6374749038301564),
 ('产品', 0.6004042515171774),
 ('需求', 0.5505482785875663),
 ('分析', 0.5470709111610579),
 ('系统', 0.5172838577800254),
 ('问题', 0.4629465408643296),
 ('专业', 0.4625032607490329),
 ('学习', 0.4506994623664768),
 ('性能', 0.43471689937955726),
 ('算法', 0.402453787542955),
 ('计算机', 0.39471587602192776),
 ('平台', 0.36126053221255366),
 ('合作', 0.3457827688958696),
 ('应用', 0.3439336809398262),
 ('解决', 0.3421456646343201),
 ('代码', 0.33960255002379275),
 ('框架', 0.33570754271798436),
 ('数据', 0.3327717760612711),
 ('工具', 0.326919072958801),
 ('理解', 0.3114392586989087),
 ('独立', 0.30680308187320954),
 ('编写', 0.30554545053265564),
 ('维护', 0.3016007768770291),
 ('提升', 0.2945159267692843),
 ('基础', 0.2852010855550602),
 ('用户', 0.2828073203602893),
 ('测试', 0.2803876170851),
 ('架构', 0.2801132590905725),
 ('精神', 0.2800289466579738),
 ('职位', 0.2734872944605602),
 ('功能', 0.2691102093514971),
 ('流程', 0.2665518341559096),
 ('研究', 0.25994737341451335),
 ('质量', 0.2580063119714751),
 ('协作', 0.2512640947800819),
 ('行业', 0.23964428788253797),
 ('责任心', 0.23568491408227407),
 ('服务', 0.22981098142890052),
 ('掌握', 0.22593064287051884),
 ('职责', 0.22557743085049434),
 ('方案', 0.22513041333827355)]
zn=[('负责', 1.0),
 ('能力', 0.8937613634656522),
 ('沟通', 0.8098343743293479),
 ('管理', 0.7900960761466024),
 ('经验', 0.6333538678031954),
 ('协助', 0.6312638162316812),
 ('专业', 0.6111458984755764),
 ('团队', 0.584584316750034),
 ('分析', 0.5345636566696106),
 ('流程', 0.4741234859327806),
 ('部门', 0.4197990413927617),
 ('协调', 0.40575756922933953),
 ('财务', 0.3972668125078426),
 ('项目', 0.39411390505941507),
 ('行业', 0.38348308927608826),
 ('处理', 0.38244835447922254),
 ('组织', 0.3802540208554401),
 ('数据', 0.3684472942804176),
 ('企业', 0.3605697031466869),
 ('风险', 0.355240022683984),
 ('需求', 0.3506039901326333),
 ('员工', 0.3473677950970496),
 ('学习', 0.34178258145051515),
 ('维护', 0.34151059145365203),
 ('办公', 0.3353774291132426),
 ('软件', 0.325788761554313),
 ('活动', 0.30327691639193266),
 ('问题', 0.30146554706458906),
 ('优化', 0.2980457112566357),
 ('招聘', 0.292389266545568),
 ('产品', 0.29236972066095696),
 ('合作', 0.29230262960594483),
 ('执行', 0.290360296042367),
 ('责任心', 0.28969785960731725),
 ('制定', 0.2867561579919686),
 ('培训', 0.2822159905429868),
 ('客户', 0.28152023371962615),
 ('服务', 0.2815084578527057),
 ('支持', 0.27812383236319),
 ('税务', 0.27427026438622126),
 ('发展', 0.271469095052696),
 ('运营', 0.26792369380400893),
 ('领导', 0.2611684170310743),
 ('整理', 0.2532788746633541),
 ('行政', 0.2520835783989799),
 ('职位', 0.24851773224933763),
 ('系统', 0.24554881987807126),
 ('审核', 0.244997369822101),
 ('建设', 0.24086464485779374),
 ('意识', 0.24047748677826056)]
sc=[('负责', 1.0),
 ('能力', 0.8930063173361342),
 ('经验', 0.7900865028331618),
 ('沟通', 0.7215968038483632),
 ('产品', 0.6869086003773832),
 ('团队', 0.6231122617687439),
 ('行业', 0.5749041383814814),
 ('客户', 0.5143365206131567),
 ('分析', 0.4954473386839125),
 ('需求', 0.48963226241476093),
 ('市场', 0.46725624696280776),
 ('项目', 0.45847529777817364),
 ('合作', 0.4474038065462844),
 ('运营', 0.4449546369529082),
 ('专业', 0.4275465381943522),
 ('活动', 0.41283778319792397),
 ('管理', 0.408585149392997),
 ('平台', 0.40829965369951804),
 ('维护', 0.40223958080925826),
 ('销售', 0.3977571522756127),
 ('策划', 0.39021766772043304),
 ('数据', 0.385987246674322),
 ('制定', 0.3771016657377926),
 ('推广', 0.3693257957580094),
 ('方案', 0.35110087814591917),
 ('执行', 0.3502276384362736),
 ('优化', 0.3496928502421802),
 ('媒体', 0.3464312144032216),
 ('内容', 0.34493533054927283),
 ('资源', 0.3423522513549908),
 ('目标', 0.342008622864996),
 ('营销', 0.3411783372654012),
 ('策略', 0.3293717110823684),
 ('用户', 0.3256493140808874),
 ('学习', 0.315956065233484),
 ('渠道', 0.30708191914833355),
 ('提升', 0.30494924011401586),
 ('独立', 0.2910594759755432),
 ('服务', 0.27886052145871487),
 ('游戏', 0.2745838699459288),
 ('品牌', 0.27334932949991636),
 ('互联网', 0.27129039844170544),
 ('广告', 0.26698406786899087),
 ('培训', 0.2643062831328341),
 ('设计', 0.25878147993730155),
 ('发展', 0.25772045887832695),
 ('协调', 0.2499781444082835),
 ('信息', 0.24388406211245625),
 ('部门', 0.24270124438799803),
 ('创意', 0.23937990381493016)]
sj=[('设计', 1.0),
 ('负责', 0.9868112840831335),
 ('能力', 0.9218159709745561),
 ('团队', 0.7255987399762701),
 ('沟通', 0.7155481304232908),
 ('产品', 0.6929576582191743),
 ('经验', 0.6908870913261365),
 ('项目', 0.6128431103620205),
 ('游戏', 0.6001006977407548),
 ('需求', 0.573904557679883),
 ('专业', 0.5274061468747596),
 ('视觉', 0.4662427336477109),
 ('用户', 0.4542091837781454),
 ('优化', 0.4505492879398456),
 ('分析', 0.4319376665463708),
 ('风格', 0.41864639453878266),
 ('美术', 0.4063194820389438),
 ('制作', 0.3985657815014167),
 ('体验', 0.37837363217962566),
 ('合作', 0.36922633358128837),
 ('独立', 0.3483285302463873),
 ('行业', 0.3421222344297511),
 ('理解', 0.3397995065045306),
 ('创意', 0.32008401923365937),
 ('学习', 0.3143634375830912),
 ('运营', 0.3103132813290382),
 ('流程', 0.30605579081155604),
 ('开发', 0.2928282402505139),
 ('数据', 0.29039302047084453),
 ('软件', 0.28559251336040153),
 ('职位', 0.2823669012212117),
 ('协作', 0.2756864304375405),
 ('精神', 0.27550461229810236),
 ('审美', 0.27100151156387603),
 ('方案', 0.26949233502054176),
 ('活动', 0.2679902420946783),
 ('提升', 0.26570942449732027),
 ('作品', 0.26475837379856526),
 ('效果', 0.26217537372214395),
 ('交互', 0.26158873618452727),
 ('配合', 0.2609154435995524),
 ('制定', 0.26047868734064494),
 ('落地', 0.2541311181992492),
 ('策划', 0.247749238755074),
 ('整体', 0.2456629850508175),
 ('研究', 0.23914218279337224),
 ('场景', 0.23709830926646208),
 ('输出', 0.2358499236021255),
 ('技术', 0.2268148536748969),
 ('问题', 0.21428485483353157)]
xs=[('客户', 1.0),
 ('销售', 0.9458748644831652),
 ('负责', 0.9164857535796892),
 ('能力', 0.8337602495786579),
 ('沟通', 0.7196226221267741),
 ('经验', 0.7088564458295153),
 ('行业', 0.6998469974760682),
 ('维护', 0.6659295112185246),
 ('产品', 0.640585443828291),
 ('团队', 0.6019634109909293),
 ('需求', 0.5689216601343677),
 ('合作', 0.5679151102425471),
 ('市场', 0.5401621641833442),
 ('管理', 0.4746922985613423),
 ('目标', 0.4446598132215326),
 ('服务', 0.4210031148386374),
 ('资源', 0.411828531813973),
 ('专业', 0.40648564726698916),
 ('分析', 0.399475349445567),
 ('拓展', 0.36643146432245405),
 ('信息', 0.3646024435123889),
 ('培训', 0.3620747488376775),
 ('项目', 0.3549046362399807),
 ('关系', 0.34512393366713795),
 ('开发', 0.3366754847302504),
 ('发展', 0.3241874701714927),
 ('学习', 0.31687758560837626),
 ('渠道', 0.3065660769197867),
 ('制定', 0.30202903132614756),
 ('方案', 0.29585411061689354),
 ('福利', 0.2919414536448208),
 ('互联网', 0.29010874633253025),
 ('开拓', 0.28786541015711326),
 ('提成', 0.28417335355252016),
 ('企业', 0.2834413429555257),
 ('营销', 0.2817389384759257),
 ('挖掘', 0.2806529158756319),
 ('平台', 0.2802468647791837),
 ('底薪', 0.27926713447575774),
 ('业绩', 0.2748203628145329),
 ('商务', 0.272129902134857),
 ('计划', 0.2701623495225926),
 ('电话', 0.27001638564709585),
 ('部门', 0.2693123146733885),
 ('执行', 0.26172527371073695),
 ('跟进', 0.2568418975503235),
 ('推广', 0.25549311814833797),
 ('大专', 0.2548701713165364),
 ('协调', 0.254366948549159),
 ('薪资', 0.254004802060037)]
def cp_ciyu():
    gzyq_cy = (
        WordCloud()
            .add("", cp,word_size_range=[10, 90],shape=('diamond'))
            .set_global_opts(title_opts=opts.TitleOpts())
            )
    grid = (
        Grid(init_opts=opts.InitOpts(width='800px', height='500px'))
            .add(gzyq_cy, grid_opts=opts.GridOpts(pos_right='3%', pos_left='3%')))
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        cp_cy = "".join(f.readlines())
        return cp_cy

def js_ciyu():
    gzyq_cy = (
        WordCloud()
            .add("", js,word_size_range=[10, 90],shape=('diamond'))
            .set_global_opts(title_opts=opts.TitleOpts())
            )
    grid = (
        Grid(init_opts=opts.InitOpts(width='800px', height='500px'))
            .add(gzyq_cy, grid_opts=opts.GridOpts(pos_right='3%', pos_left='3%')))
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_cy = "".join(f.readlines())
        return js_cy

def sj_ciyu():
    gzyq_cy = (
        WordCloud()
            .add("", sj,word_size_range=[10, 90],shape=('diamond'))
            .set_global_opts(title_opts=opts.TitleOpts())
            )
    grid = (
        Grid(init_opts=opts.InitOpts(width='800px', height='500px'))
            .add(gzyq_cy, grid_opts=opts.GridOpts(pos_right='3%', pos_left='3%')))
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        sj_cy = "".join(f.readlines())
        return sj_cy

def yy_ciyu():
    gzyq_cy = (
        WordCloud()
            .add("", yy,word_size_range=[10, 90],shape=('diamond'))
            .set_global_opts(title_opts=opts.TitleOpts())
            )
    grid = (
        Grid(init_opts=opts.InitOpts(width='800px', height='500px'))
            .add(gzyq_cy, grid_opts=opts.GridOpts(pos_right='3%', pos_left='3%')))
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        yy_cy = "".join(f.readlines())
        return yy_cy

def zn_ciyu():
    gzyq_cy = (
        WordCloud()
            .add("", zn,word_size_range=[10, 90],shape=('diamond'))
            .set_global_opts(title_opts=opts.TitleOpts())
            )
    grid = (
        Grid(init_opts=opts.InitOpts(width='800px', height='500px'))
            .add(gzyq_cy, grid_opts=opts.GridOpts(pos_right='3%', pos_left='3%')))
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        zn_cy = "".join(f.readlines())
        return zn_cy

def xs_ciyu():
    gzyq_cy = (
        WordCloud()
            .add("", xs,word_size_range=[10, 90],shape=('diamond'))
            .set_global_opts(title_opts=opts.TitleOpts())
            )
    grid = (
        Grid(init_opts=opts.InitOpts(width='800px', height='500px'))
            .add(gzyq_cy, grid_opts=opts.GridOpts(pos_right='3%', pos_left='3%')))
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        xs_cy = "".join(f.readlines())
        return xs_cy

def sc_ciyu():
    gzyq_cy = (
        WordCloud()
            .add("", sc,word_size_range=[10, 90],shape=('diamond'))
            .set_global_opts(title_opts=opts.TitleOpts())
            )
    grid = (
        Grid(init_opts=opts.InitOpts(width='800px', height='500px'))
            .add(gzyq_cy, grid_opts=opts.GridOpts(pos_right='3%', pos_left='3%')))
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        sc_cy = "".join(f.readlines())
        return sc_cy

# ---------------------------------------------技术方向-----------------------------------------------------------
js_data=data[data["类别"]=="技术"]
def js_shu():
    jishu_data = [
        {"name": "技术",
         "children": [
             {"name": "后端开发（Java、C++、区块链）"}, {"name": "前端开发（web前端、flash、html）"},
             {"name": "数据挖掘"}, {"name": "测试工程师"},
             {"name": "运维工程师"}, {"name": "机器学习"}]}]
    # ,theme=ThemeType.VINTAGE
    hangyefenlei = (
        Tree(init_opts=opts.InitOpts(width="450px", height="500px", bg_color="rgba(156,168,184,0)"))
            .add("", data=jishu_data, symbol="rect", symbol_size=12,
                 is_roam=True, initial_tree_depth=1,
                 label_opts=opts.LabelOpts(color='#4A4453', position='top', font_family='Arial'))
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='500px', height='400px'))
            .add(hangyefenlei, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_shuzhuan = "".join(f.readlines())
        return js_shuzhuan
def js_shengmap():
    # 取出省份和省份数量做成字典
    jssheng_list = list(js_data['省份'])
    jssheng_dict = dict([[i, jssheng_list.count(i)] for i in jssheng_list])
    # 移除non值
    del jssheng_dict['无']
    # 职位省份分布
    provice = list(jssheng_dict.keys())
    provice_values = list(jssheng_dict.values())
    pieces = [{"min": 900, "max": 1200},
              {"min": 100, "max": 900},
              {"min": 0, "max": 100},
              ]
    # 画图
    sheng_map = (
        Map(init_opts=opts.InitOpts(
            width="700px", height="500px", bg_color="rgba(156,168,184,0)", ))
            .add("", data_pair=[list(z) for z in zip(provice, provice_values)],
                 maptype="china",
                 symbol="roundRect", is_selected=True, is_map_symbol_show=False)
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                pos_left='5%',
                pos_top='60%',
                is_piecewise=True,
                is_calculable=False,
                pieces=pieces,
                range_color=["#B0A7FF", "#FEFFA7", "#D68787"],
            )))
    grid = (
        Grid(init_opts=opts.InitOpts(width='690px', height='650px'))
            .add(sheng_map, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_sheng = "".join(f.readlines())
        return js_sheng
def js_city_sl():
    jscity_list = list(js_data['城市'])
    jscity_dict = dict([[i, jscity_list.count(i)] for i in jscity_list])
    # 移除non值
    del jscity_dict['无']
    # 职位城市分布
    cities = list(jscity_dict.keys())
    cities_values = list(jscity_dict.values())
    pieces = [{"min": 500, "max": 1200},
              {"min": 50, "max": 400},
              {"min": 0, "max": 50}
              ]
    city_sum = (
        Geo(init_opts=opts.InitOpts(width="500px", height="550px"))
            .add_schema(maptype="china",
                        itemstyle_opts=opts.ItemStyleOpts())
            .add(
            "",
            data_pair=[list(z) for z in zip(cities, cities_values)],
            type_=ChartType.EFFECT_SCATTER,
            symbol_size=7)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                pos_left='8%',
                pos_top='60%',
                is_piecewise=True,
                is_calculable=False,
                pieces=pieces,
                range_color=["#B0A7FF", "#FEFFA7", "#D68787"],
                range_size="7px",
            ),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='690px', height='650px'))
            .add(city_sum, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_csl = "".join(f.readlines())
        return js_csl
def js_zhucitu():
    # 取出城市数量做成字典
    jscity_list1 = list(js_data['城市'])
    jscity_dict1 = dict([[i, jscity_list1.count(i)] for i in jscity_list1])
    # 移除non值
    del jscity_dict1['无']
    jscity_dict1 = dict(sorted(jscity_dict1.items(), key=operator.itemgetter(1), reverse=True))
    # 职位城市分布
    cities1 = list(jscity_dict1.keys())[0:10]
    cities_values1 = list(jscity_dict1.values())[0:10]
    js_sum = (
        Bar(init_opts=opts.InitOpts(width='500px', height='500px'))
            .add_xaxis(cities1)
            .add_yaxis('', cities_values1, color="#9358B8")
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)
                                     ),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#B0A7FF"]
            )
        )
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(js_sum, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_zsl = "".join(f.readlines())
        return js_zsl
def jsxinzi():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = js_data.query("城市 == @city")
    shengfen_average = city_data.groupby('城市')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    shengfen_average['平均薪资（千/月）'] = shengfen_average['平均薪资（千/月）'].round(decimals=1)
    shengfen_average = shengfen_average.sort_values('平均薪资（千/月）', ascending=False)

    x_data = shengfen_average['城市'].values.tolist()
    y_data = shengfen_average['平均薪资（千/月）'].values.tolist()

    line = Line(init_opts=opts.InitOpts(width='750px', height='400px'))
    line.add_xaxis(x_data)
    line.add_yaxis('平均薪资（千/月）', y_data, color="#9358B8")
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='400px'))
            .add(line, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_line = "".join(f.readlines())
        return js_line
def jszuigao():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = js_data.query("城市 == @city")
    # 平均数
    xz_zg = city_data.groupby('城市')['最高薪资（千/月）'].mean().to_frame('最高薪资（千/月）').reset_index()
    xz_zg['最高薪资（千/月）'] = xz_zg['最高薪资（千/月）'].round(decimals=1)
    xz_zg = xz_zg.sort_values('最高薪资（千/月）', ascending=False)[:10]
    # 中位数
    xz_zw = city_data.groupby('城市')['最高薪资（千/月）'].median().to_frame('最高薪资（千/月）').reset_index()
    xz_zw['最高薪资（千/月）'] = xz_zw['最高薪资（千/月）'].round(decimals=1)
    xz_zw = xz_zw.sort_values('最高薪资（千/月）', ascending=False)[:10]
    x_data = xz_zw['城市'].values.tolist()
    pj_y_data = xz_zg['最高薪资（千/月）'].values.tolist()
    zw_y_data = xz_zw['最高薪资（千/月）'].values.tolist()
    # 准备x轴数据
    xin_zi = ['薪资平均', '薪资中位']
    x = [(lei, wages) for lei in x_data for wages in xin_zi]
    # 准备y轴数据
    y = sum(zip(pj_y_data, zw_y_data), ())
    # 准备ColumnDataSource
    source = ColumnDataSource(data=dict(x_axis=x, y_counts=y))
    # 准备tooltips 鼠标移入显示数据
    TOOLTIPS = [
        ("counts", "@y_counts" + "（千/月）"),
        ("描述", "@x_axis")]
    color = ["#FFA7A7", "#AAA3FF"]
    # 画布
    p = figure(
        x_range=FactorRange(*x),
        plot_height=350,
        title="主要城市最高薪资中位数和平均数差异",
        tooltips=TOOLTIPS
    )
    # 绘制图形 vbar 垂直柱状图
    p.vbar(
        x='x_axis',
        top="y_counts",
        width=0.8,
        source=source,
        fill_color=factor_cmap('x_axis',
                               palette=color,
                               factors=xin_zi,
                               start=1, end=2)
    )
    # factor_cmap 模块 每一类相同颜色，共2种颜色
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    # p.yaxis.axis_label = "薪资（千/月）"  # y轴名称
    p.axis.axis_label_text_font_style = 'bold'
    p.yaxis.major_label_text_font_size = '14px'
    return p
def jszuidi():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = js_data.query("城市 == @city")
    # 平均数
    xz_zd = city_data.groupby('城市')['最低薪资（千/月）'].mean().to_frame('最低薪资（千/月）').reset_index()
    xz_zd['最低薪资（千/月）'] = xz_zd['最低薪资（千/月）'].round(decimals=1)
    xz_zd = xz_zd.sort_values('最低薪资（千/月）', ascending=False)
    # 中位数
    xz_zw1 = city_data.groupby('城市')['最低薪资（千/月）'].median().to_frame('最低薪资（千/月）').reset_index()
    xz_zw1['最低薪资（千/月）'] = xz_zw1['最低薪资（千/月）'].round(decimals=1)
    xz_zw1 = xz_zw1.sort_values('最低薪资（千/月）', ascending=False)
    x_data1 = xz_zw1['城市'].values.tolist()
    pj_y_data1 = xz_zd['最低薪资（千/月）'].values.tolist()
    zw_y_data1 = xz_zw1['最低薪资（千/月）'].values.tolist()
    # 准备x轴数据
    xin_zi = ['薪资平均', '薪资中位']
    x = [(lei, wages) for lei in x_data1 for wages in xin_zi]
    # 准备y轴数据
    y = sum(zip(pj_y_data1, zw_y_data1), ())
    # 准备ColumnDataSource
    source = ColumnDataSource(data=dict(x_axis=x, y_counts=y))
    # 准备tooltips 鼠标移入显示数据
    TOOLTIPS = [
        ("counts", "@y_counts" + "（千/月）"),
        ("描述", "@x_axis")]
    color = ["#FBFD9F","#9FB1FD"]
    # 画布
    p = figure(
        x_range=FactorRange(*x),
        plot_height=350,
        title="主要城市最低薪资中位数和平均数差异",
        tooltips=TOOLTIPS
    )
    # 绘制图形 vbar 垂直柱状图
    p.vbar(
        x='x_axis',
        top="y_counts",
        width=0.8,
        source=source,
        fill_color=factor_cmap('x_axis',
                               palette=color,
                               factors=xin_zi,
                               start=1, end=2)
    )
    # factor_cmap 模块 每一类相同颜色，共2种颜色
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    # p.yaxis.axis_label = "薪资（千/月）"  # y轴名称
    p.axis.axis_label_text_font_style = 'bold'
    p.yaxis.major_label_text_font_size = '14px'
    return p
def nxxllx():
    # 获取不同工作年限的数量
    gznx_num = js_data['工作年限'].value_counts()
    gznx = gznx_num.index.tolist()
    num = [i for i in gznx_num]
    data_pair1 = [list(z) for z in zip(gznx, num)]
    # 获取不同学历要求的数量
    xueli_num = js_data['学历要求'].value_counts()
    xueli_e = xueli_num.index.tolist()
    num_e = [i for i in xueli_num]
    data_pair2 = [list(z) for z in zip(xueli_e, num_e)]
    # 获取不同工作类型的数量
    gzlx_num = js_data['工作类型'].value_counts()
    leixing_l = gzlx_num.index.tolist()
    num_l = [i for i in gzlx_num]
    data_pair2 = [list(z) for z in zip(leixing_l, num_l)]
    # 开始画图
    gznx_bar = (
        Bar()
            .add_xaxis(gznx)
            .add_yaxis("", num, color='#B0A7FF')
            .set_global_opts(title_opts=opts.TitleOpts(title="不同工作年限数量", pos_left="30%",
                                                       ))
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="average", type_="average")]))
    )

    xueli_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair1, rosetype="area", center=['25%', "75%"], radius=["10%", '25%'])
            .set_colors(["#b5c4b1", "#8696a7", "#9ca8b8", "#ececea", "#7a7281", "#fffaf4", "#a27e7e", "#ead0d1"])
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同工作类型数量占比",
                                                       pos_left="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色
                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))
    leixing_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair2, center=['75%', "75%"], radius=["15%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同学历要求数量占比",
                                                       pos_right="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色

                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False),

                             )
    )

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(gznx_bar, grid_opts=opts.GridOpts(pos_right="35%", pos_bottom='60%'))
    grid.add(xueli_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='60%'))
    grid.add(leixing_pie, grid_opts=opts.GridOpts(pos_right="50%", pos_top="60%"))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        nxxz = "".join(f.readlines())
        return nxxz

def js_ruzi():
    # 获取不同融资情况的数量
    rzqk_num = js_data['融资情况'].value_counts()
    rzqk = rzqk_num.index.tolist()
    rz_num = [i for i in rzqk_num]
    data_pair3 = [list(z) for z in zip(rzqk, rz_num)]

    # 融资情况不同，薪资中位情况
    rz_average = js_data.groupby('融资情况')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    rz_average['平均薪资（千/月）'] = rz_average['平均薪资（千/月）'].round(decimals=1)
    rz_average = rz_average.sort_values('平均薪资（千/月）', ascending=False)
    x_data = rz_average['融资情况'].values.tolist()
    y_data = rz_average['平均薪资（千/月）'].values.tolist()
    rz_pie = (
        Pie()
            .add("岗位数量占比", data_pair=data_pair3, rosetype="area", center=['65%', "50%"], radius=["10%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同融资情况数量占比",
                                                       pos_left="60%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="80%",
                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))

    rz_sum = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(x_data)
            .add_yaxis('', y_data, color="#BDA8FF")
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不同融资情况薪资差异", pos_left="12%", pos_top="10%",
                                      ),
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#BDA8FF"]))
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(rz_sum, grid_opts=opts.GridOpts(pos_right="60%", pos_top="20%"))
    grid.add(rz_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='20%'))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        jsrz = "".join(f.readlines())
        return jsrz

def js_gm():
    # 获取不同公司规模的数量
    gsgm_num = js_data['公司规模'].value_counts()
    gsgm = gsgm_num.index.tolist()
    gsgm_num = [i for i in gsgm_num]
    data_pair4 = [list(z) for z in zip(gsgm, gsgm_num)]

    # 公司规模不同，薪资中位情况
    gsgm_average = js_data.groupby('公司规模')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    gsgm_average['平均薪资（千/月）'] = gsgm_average['平均薪资（千/月）'].round(decimals=1)
    gsgm_average = gsgm_average.sort_values('平均薪资（千/月）', ascending=False)
    x_data = gsgm_average['公司规模'].values.tolist()
    y_data = gsgm_average['平均薪资（千/月）'].values.tolist()
    rz_pie = (
        Pie()
            .add("岗位数量占比", data_pair=data_pair4, rosetype="area", center=['65%', "50%"], radius=["10%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同公司规模数量占比",
                                                       pos_left="60%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="80%",
                                                       # 设置标题颜色
                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))

    rz_sum = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(x_data)
            .add_yaxis('', y_data, color="#F5F8B7")
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不同公司规模薪资差异（千/月）", pos_left="10%", pos_top="13%",
                                      ),
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#A7CBFF"]))
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(rz_sum, grid_opts=opts.GridOpts(pos_right="60%", pos_top="20%"))
    grid.add(rz_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='20%'))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        jsgm = "".join(f.readlines())
        return jsgm

def js_dingwei():
    gsdw = list(js_data['公司定位'].unique())
    gsdw_count = list(js_data['公司定位'].value_counts())
    zong = [list(z) for z in zip(gsdw, gsdw_count)]
    c1 = (
        WordCloud()
            .add(series_name="", data_pair=zong, word_size_range=[4, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        #     .render("basic_wordcloud.html")
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='500px', height='400px'))
            .add(c1, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_dw = "".join(f.readlines())
        return js_dw

def js_dwxz():
    dw = js_data[~js_data['公司定位'].isin(["无"])]
    dw = dw[~dw['公司定位'].isin(["不限"])]
    salary_average = dw.groupby('公司定位')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    salary_average['平均薪资（千/月）'] = salary_average['平均薪资（千/月）'].round(decimals=1)
    salary_average = salary_average.sort_values('平均薪资（千/月）', ascending=False)[:15]
    factors = salary_average['公司定位'].values.tolist()
    x = salary_average['平均薪资（千/月）'].values.tolist()

    fig = figure(
        title="所属公司定位平均薪资(千/月)",
        #     toolbar_location=None,
        tools="hover",
        y_range=factors,
        x_range=[0, 50],
        tooltips=[('平均薪资中位数', '￥@x' + "（千/月）")],
        plot_width=750,
        plot_height=500)

    fig.segment(0, factors, x, factors, line_width=3, line_color="#B9A7FF")
    fig.circle(x, factors, size=18, fill_color="#FEFFA7", line_color="#B9A7FF", line_width=4)
    fig.xgrid.grid_line_color = None
    fig.ygrid.grid_line_color = None
    return fig

def js_fl():

    js_data['岗位福利'] = js_data['岗位福利'].astype('str')
    fuli_sum = js_data['岗位福利'].sum()
    def wordcount():
        readlist = fuli_sum.split(",")
        dict1 = {}
        for every_world in readlist:
            if every_world in dict1:
                dict1[every_world] += 1
            else:
                dict1[every_world] = 1
        return dict1

    fuli_cipin = wordcount()
    fuli_cipin1 = {k: v for k, v in fuli_cipin.items() if v > int(10)}
    fuli_cppx = sorted(fuli_cipin1.items(), key=lambda x: x[1], reverse=True)

    c2 = (
        WordCloud()
            .add(series_name="", data_pair=fuli_cppx, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(c2, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_c2 = "".join(f.readlines())
        return js_c2

def js_gz():
    gz = [('工作', 1.0),
          ('经验', 0.9404404006653319),
          ('负责', 0.9000430233515043),
          ('开发', 0.8472295392205147),
          ('能力', 0.7722875858963815),
          ('优先', 0.7039699342576814),
          ('熟悉', 0.690082626025797),
          ('技术', 0.6856485157324603),
          ('设计', 0.6486344119907717),
          ('要求', 0.6457593071946648),
          ('优化', 0.6159088620081258),
          ('团队', 0.6076353405377367),
          ('项目', 0.5925630642816444),
          ('沟通', 0.5694618915055515),
          ('产品', 0.5441816908362828),
          ('学习', 0.5420253527154101),
          ('需求', 0.4933748894998458),
          ('分析', 0.4891160245626631),
          ('系统', 0.45563863594829423),
          ('业务', 0.44781954149454944),
          ('问题', 0.4137911497195212),
          ('专业', 0.4127884218287598),
          ('性能', 0.38840343931268667),
          ('算法', 0.3626638975326637),
          ('平台', 0.3253783998385903),
          ('计算机', 0.3195949484449985),
          ('应用', 0.3113967378925182),
          ('合作', 0.3082462170540091),
          ('解决', 0.3076531445097007),
          ('框架', 0.3054951889564982),
          ('代码', 0.3045755304069145),
          ('数据', 0.3015736234854905),
          ('工具', 0.29492291687197064),
          ('理解', 0.2802572464304946),
          ('编写', 0.2751798608148809),
          ('独立', 0.2740935118352163),
          ('维护', 0.2714026163569488),
          ('提升', 0.2660452031784063),
          ('基础', 0.2628121151652766),
          ('职位', 0.25491989580265817),
          ('用户', 0.25288485902063856),
          ('架构', 0.25249232958570644),
          ('测试', 0.25141407407942457),
          ('精神', 0.24616031293822224),
          ('功能', 0.24179926853944644),
          ('流程', 0.23814430214327237),
          ('研究', 0.233780740305019),
          ('质量', 0.23118095903841224),
          ('协作', 0.22333157713530874),
          ('行业', 0.21684591777179077),
          ('提供', 0.2148059171198309),
          ('责任心', 0.21314519989711034),
          ('编程', 0.2073404521073448),
          ('掌握', 0.20505049636410166),
          ('服务', 0.2031492376479594),
          ('职责', 0.20240837204261147),
          ('方案', 0.20199973412682704),
          ('软件', 0.19331262450582365),
          ('管理', 0.19318223194599413),
          ('领域', 0.19267198439225566),
          ('场景', 0.19197356279950822),
          ('体验', 0.19143460560939127),
          ('解决问题', 0.19077912051230925),
          ('核心', 0.18931418197719685),
          ('游戏', 0.18341505386932855),
          ('模块', 0.18049151311171238),
          ('效率', 0.17797460418529468),
          ('处理', 0.17742199863625188),
          ('深入', 0.17617980789387663),
          ('深度', 0.16958113675580566),
          ('原理', 0.16402876041357856),
          ('规范', 0.15710064732752227),
          ('计算机相关', 0.1564126262535577),
          ('模型', 0.15586100606876674),
          ('建设', 0.1557813934841552),
          ('知识', 0.15315644491990785),
          ('制定', 0.15174540928242347),
          ('数据结构', 0.15169492630437767),
          ('网络', 0.1513352388159173),
          ('机器', 0.15011875437152633),
          ('运维', 0.14783457734597216),
          ('落地', 0.1473828614003572),
          ('配合', 0.14715516580186486),
          ('实际', 0.1464992761172955),
          ('意识', 0.14449562094003618),
          ('构建', 0.14273286562637202),
          ('组件', 0.13979381102999108),
          ('环境', 0.1375095575134535),
          ('编码', 0.13646464011775772),
          ('部署', 0.1361430233616575),
          ('解决方案', 0.1353725443426511),
          ('逻辑', 0.13443116734797875),
          ('方向', 0.13375576076257004),
          ('语言', 0.13333857512512218),
          ('发展', 0.1295246513441984),
          ('数据库', 0.1267852298611131),
          ('岗位', 0.12665277982425874),
          ('客户端', 0.12654217577166219),
          ('智能', 0.12626445432833902),
          ('互联网', 0.12557059488726582)]
    c3 = (
        WordCloud()
            .add(series_name="", data_pair=gz, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(c3, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_c3 = "".join(f.readlines())
        return js_c3

# ---------------------------------------------产品方向-----------------------------------------------------------
cp_data=data[data["类别"]=="产品"]
def cp_shu():
    jishu_data = [
        {"name": "产品",
         "children": [
             {"name": "产品经理"}, {"name": "产品助理"},
             {"name": "移动产品经理"}, {"name": "电商产品经理"},
             {"name": "产品专员"}, {"name": "数据产品经理"}
         ]}]
    # ,theme=ThemeType.VINTAGE
    hangyefenlei = (
        Tree(init_opts=opts.InitOpts(width="450px", height="500px", bg_color="rgba(156,168,184,0)"))
            .add("", data=jishu_data, symbol="rect", symbol_size=12,
                 is_roam=True, initial_tree_depth=1,
                 label_opts=opts.LabelOpts(color='#4A4453', position='top', font_family='Arial'))
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='500px', height='400px'))
            .add(hangyefenlei, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_shuzhuan = "".join(f.readlines())
        return js_shuzhuan
def cp_shengmap():
    # 取出省份和省份数量做成字典
    jssheng_list = list(cp_data['省份'])
    jssheng_dict = dict([[i, jssheng_list.count(i)] for i in jssheng_list])
    # 移除non值
    del jssheng_dict['无']
    # 职位省份分布
    provice = list(jssheng_dict.keys())
    provice_values = list(jssheng_dict.values())
    pieces = [{"min": 900, "max": 1200},
              {"min": 100, "max": 900},
              {"min": 0, "max": 100},
              ]
    # 画图
    sheng_map = (
        Map(init_opts=opts.InitOpts(
            width="700px", height="500px", bg_color="rgba(156,168,184,0)", ))
            .add("", data_pair=[list(z) for z in zip(provice, provice_values)],
                 maptype="china",
                 symbol="roundRect", is_selected=True, is_map_symbol_show=False)
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                pos_left='5%',
                pos_top='60%',
                is_piecewise=True,
                is_calculable=False,
                pieces=pieces,
                range_color=["#B0A7FF", "#FEFFA7", "#D68787"],
            )))
    grid = (
        Grid(init_opts=opts.InitOpts(width='690px', height='650px'))
            .add(sheng_map, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_sheng = "".join(f.readlines())
        return js_sheng
def cp_city_sl():
    jscity_list = list(cp_data['城市'])
    jscity_dict = dict([[i, jscity_list.count(i)] for i in jscity_list])
    # 移除non值
    del jscity_dict['无']
    # 职位城市分布
    cities = list(jscity_dict.keys())
    cities_values = list(jscity_dict.values())
    pieces = [{"min": 500, "max": 1200},
              {"min": 50, "max": 400},
              {"min": 0, "max": 50}
              ]
    city_sum = (
        Geo(init_opts=opts.InitOpts(width="500px", height="550px"))
            .add_schema(maptype="china",
                        itemstyle_opts=opts.ItemStyleOpts())
            .add(
            "",
            data_pair=[list(z) for z in zip(cities, cities_values)],
            type_=ChartType.EFFECT_SCATTER,
            symbol_size=7)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                pos_left='8%',
                pos_top='60%',
                is_piecewise=True,
                is_calculable=False,
                pieces=pieces,
                range_color=["#B0A7FF", "#FEFFA7", "#D68787"],
                range_size="7px",
            ),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='690px', height='650px'))
            .add(city_sum, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_csl = "".join(f.readlines())
        return js_csl
def cp_zhucitu():
    # 取出城市数量做成字典
    jscity_list1 = list(cp_data['城市'])
    jscity_dict1 = dict([[i, jscity_list1.count(i)] for i in jscity_list1])
    # 移除non值
    del jscity_dict1['无']
    jscity_dict1 = dict(sorted(jscity_dict1.items(), key=operator.itemgetter(1), reverse=True))
    # 职位城市分布
    cities1 = list(jscity_dict1.keys())[0:10]
    cities_values1 = list(jscity_dict1.values())[0:10]
    js_sum = (
        Bar(init_opts=opts.InitOpts(width='500px', height='500px'))
            .add_xaxis(cities1)
            .add_yaxis('', cities_values1, color="#9358B8")
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)
                                     ),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#B0A7FF"]
            )
        )
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(js_sum, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_zsl = "".join(f.readlines())
        return js_zsl
def cpxinzi():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = cp_data.query("城市 == @city")
    shengfen_average = city_data.groupby('城市')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    shengfen_average['平均薪资（千/月）'] = shengfen_average['平均薪资（千/月）'].round(decimals=1)
    shengfen_average = shengfen_average.sort_values('平均薪资（千/月）', ascending=False)

    x_data = shengfen_average['城市'].values.tolist()
    y_data = shengfen_average['平均薪资（千/月）'].values.tolist()

    line = Line(init_opts=opts.InitOpts(width='750px', height='400px'))
    line.add_xaxis(x_data)
    line.add_yaxis('平均薪资（千/月）', y_data, color="#9358B8")
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='400px'))
            .add(line, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_line = "".join(f.readlines())
        return js_line
def cpzuigao():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = cp_data.query("城市 == @city")
    # 平均数
    xz_zg = city_data.groupby('城市')['最高薪资（千/月）'].mean().to_frame('最高薪资（千/月）').reset_index()
    xz_zg['最高薪资（千/月）'] = xz_zg['最高薪资（千/月）'].round(decimals=1)
    xz_zg = xz_zg.sort_values('最高薪资（千/月）', ascending=False)[:10]
    # 中位数
    xz_zw = city_data.groupby('城市')['最高薪资（千/月）'].median().to_frame('最高薪资（千/月）').reset_index()
    xz_zw['最高薪资（千/月）'] = xz_zw['最高薪资（千/月）'].round(decimals=1)
    xz_zw = xz_zw.sort_values('最高薪资（千/月）', ascending=False)[:10]
    x_data = xz_zw['城市'].values.tolist()
    pj_y_data = xz_zg['最高薪资（千/月）'].values.tolist()
    zw_y_data = xz_zw['最高薪资（千/月）'].values.tolist()
    # 准备x轴数据
    xin_zi = ['薪资平均', '薪资中位']
    x = [(lei, wages) for lei in x_data for wages in xin_zi]
    # 准备y轴数据
    y = sum(zip(pj_y_data, zw_y_data), ())
    # 准备ColumnDataSource
    source = ColumnDataSource(data=dict(x_axis=x, y_counts=y))
    # 准备tooltips 鼠标移入显示数据
    TOOLTIPS = [
        ("counts", "@y_counts" + "（千/月）"),
        ("描述", "@x_axis")]
    color = ["#FFA7A7", "#AAA3FF"]
    # 画布
    p = figure(
        x_range=FactorRange(*x),
        plot_height=350,
        title="主要城市最高薪资中位数和平均数差异",
        tooltips=TOOLTIPS
    )
    # 绘制图形 vbar 垂直柱状图
    p.vbar(
        x='x_axis',
        top="y_counts",
        width=0.8,
        source=source,
        fill_color=factor_cmap('x_axis',
                               palette=color,
                               factors=xin_zi,
                               start=1, end=2)
    )
    # factor_cmap 模块 每一类相同颜色，共2种颜色
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    # p.yaxis.axis_label = "薪资（千/月）"  # y轴名称
    p.axis.axis_label_text_font_style = 'bold'
    p.yaxis.major_label_text_font_size = '14px'
    return p
def cpzuidi():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = cp_data.query("城市 == @city")
    # 平均数
    xz_zd = city_data.groupby('城市')['最低薪资（千/月）'].mean().to_frame('最低薪资（千/月）').reset_index()
    xz_zd['最低薪资（千/月）'] = xz_zd['最低薪资（千/月）'].round(decimals=1)
    xz_zd = xz_zd.sort_values('最低薪资（千/月）', ascending=False)
    # 中位数
    xz_zw1 = city_data.groupby('城市')['最低薪资（千/月）'].median().to_frame('最低薪资（千/月）').reset_index()
    xz_zw1['最低薪资（千/月）'] = xz_zw1['最低薪资（千/月）'].round(decimals=1)
    xz_zw1 = xz_zw1.sort_values('最低薪资（千/月）', ascending=False)
    x_data1 = xz_zw1['城市'].values.tolist()
    pj_y_data1 = xz_zd['最低薪资（千/月）'].values.tolist()
    zw_y_data1 = xz_zw1['最低薪资（千/月）'].values.tolist()
    # 准备x轴数据
    xin_zi = ['薪资平均', '薪资中位']
    x = [(lei, wages) for lei in x_data1 for wages in xin_zi]
    # 准备y轴数据
    y = sum(zip(pj_y_data1, zw_y_data1), ())
    # 准备ColumnDataSource
    source = ColumnDataSource(data=dict(x_axis=x, y_counts=y))
    # 准备tooltips 鼠标移入显示数据
    TOOLTIPS = [
        ("counts", "@y_counts" + "（千/月）"),
        ("描述", "@x_axis")]
    color = ["#FBFD9F","#9FB1FD"]
    # 画布
    p = figure(
        x_range=FactorRange(*x),
        plot_height=350,
        title="主要城市最低薪资中位数和平均数差异",
        tooltips=TOOLTIPS
    )
    # 绘制图形 vbar 垂直柱状图
    p.vbar(
        x='x_axis',
        top="y_counts",
        width=0.8,
        source=source,
        fill_color=factor_cmap('x_axis',
                               palette=color,
                               factors=xin_zi,
                               start=1, end=2)
    )
    # factor_cmap 模块 每一类相同颜色，共2种颜色
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    # p.yaxis.axis_label = "薪资（千/月）"  # y轴名称
    p.axis.axis_label_text_font_style = 'bold'
    p.yaxis.major_label_text_font_size = '14px'
    return p
def cpnxxllx():
    # 获取不同工作年限的数量
    gznx_num = cp_data['工作年限'].value_counts()
    gznx = gznx_num.index.tolist()
    num = [i for i in gznx_num]
    data_pair1 = [list(z) for z in zip(gznx, num)]
    # 获取不同学历要求的数量
    xueli_num = cp_data['学历要求'].value_counts()
    xueli_e = xueli_num.index.tolist()
    num_e = [i for i in xueli_num]
    data_pair2 = [list(z) for z in zip(xueli_e, num_e)]
    # 获取不同工作类型的数量
    gzlx_num = cp_data['工作类型'].value_counts()
    leixing_l = gzlx_num.index.tolist()
    num_l = [i for i in gzlx_num]
    data_pair2 = [list(z) for z in zip(leixing_l, num_l)]
    # 开始画图
    gznx_bar = (
        Bar()
            .add_xaxis(gznx)
            .add_yaxis("", num, color='#B0A7FF')
            .set_global_opts(title_opts=opts.TitleOpts(title="不同工作年限数量", pos_left="30%",
                                                     ))
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="average", type_="average")]))
    )

    xueli_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair1, rosetype="area", center=['25%', "75%"], radius=["10%", '25%'])
            .set_colors(["#b5c4b1", "#8696a7", "#9ca8b8", "#ececea", "#7a7281", "#fffaf4", "#a27e7e", "#ead0d1"])
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同工作类型数量占比",
                                                       pos_left="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色
                                                ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))
    leixing_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair2, center=['75%', "75%"], radius=["15%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同学历要求数量占比",
                                                       pos_right="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色

                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False),

                             )
    )

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(gznx_bar, grid_opts=opts.GridOpts(pos_right="35%", pos_bottom='60%'))
    grid.add(xueli_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='60%'))
    grid.add(leixing_pie, grid_opts=opts.GridOpts(pos_right="50%", pos_top="60%"))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        nxxz = "".join(f.readlines())
        return nxxz

def cp_ruzi():
    # 获取不同融资情况的数量
    rzqk_num = cp_data['融资情况'].value_counts()
    rzqk = rzqk_num.index.tolist()
    rz_num = [i for i in rzqk_num]
    data_pair3 = [list(z) for z in zip(rzqk, rz_num)]

    # 融资情况不同，薪资中位情况
    rz_average = cp_data.groupby('融资情况')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    rz_average['平均薪资（千/月）'] = rz_average['平均薪资（千/月）'].round(decimals=1)
    rz_average = rz_average.sort_values('平均薪资（千/月）', ascending=False)
    x_data = rz_average['融资情况'].values.tolist()
    y_data = rz_average['平均薪资（千/月）'].values.tolist()
    rz_pie = (
        Pie()
            .add("岗位数量占比", data_pair=data_pair3, rosetype="area", center=['65%', "50%"], radius=["10%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同融资情况数量占比",
                                                       pos_left="60%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="80%",
                                                       # 设置标题颜色
                                                 ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))

    rz_sum = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(x_data)
            .add_yaxis('', y_data, color="#BDA8FF")
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不同融资情况薪资差异", pos_left="12%", pos_top="10%",
                 ),
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#BDA8FF"]))
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(rz_sum, grid_opts=opts.GridOpts(pos_right="60%", pos_top="20%"))
    grid.add(rz_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='20%'))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        jsrz = "".join(f.readlines())
        return jsrz

def cp_gm():
    # 获取不同公司规模的数量
    gsgm_num =cp_data['公司规模'].value_counts()
    gsgm = gsgm_num.index.tolist()
    gsgm_num = [i for i in gsgm_num]
    data_pair4 = [list(z) for z in zip(gsgm, gsgm_num)]

    # 公司规模不同，薪资中位情况
    gsgm_average = cp_data.groupby('公司规模')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    gsgm_average['平均薪资（千/月）'] = gsgm_average['平均薪资（千/月）'].round(decimals=1)
    gsgm_average = gsgm_average.sort_values('平均薪资（千/月）', ascending=False)
    x_data = gsgm_average['公司规模'].values.tolist()
    y_data = gsgm_average['平均薪资（千/月）'].values.tolist()
    rz_pie = (
        Pie()
            .add("岗位数量占比", data_pair=data_pair4, rosetype="area", center=['65%', "50%"], radius=["10%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同公司规模数量占比",
                                                       pos_left="60%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="80%",
                                                       # 设置标题颜色
                                                      ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))

    rz_sum = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(x_data)
            .add_yaxis('', y_data, color="#F5F8B7")
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不同公司规模薪资差异（千/月）", pos_left="10%", pos_top="13%",
                                      ),
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#A7CBFF"]))
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(rz_sum, grid_opts=opts.GridOpts(pos_right="60%", pos_top="20%"))
    grid.add(rz_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='20%'))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        jsgm = "".join(f.readlines())
        return jsgm

def cp_dingwei():
    gsdw = list(cp_data['公司定位'].unique())
    gsdw_count = list(cp_data['公司定位'].value_counts())
    zong = [list(z) for z in zip(gsdw, gsdw_count)]
    c1 = (
        WordCloud()
            .add(series_name="", data_pair=zong, word_size_range=[4, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        #     .render("basic_wordcloud.html")
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='500px', height='400px'))
            .add(c1, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_dw = "".join(f.readlines())
        return js_dw

def cp_dwxz():
    dw = cp_data[~cp_data['公司定位'].isin(["无"])]
    dw = dw[~dw['公司定位'].isin(["不限"])]
    salary_average = dw.groupby('公司定位')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    salary_average['平均薪资（千/月）'] = salary_average['平均薪资（千/月）'].round(decimals=1)
    salary_average = salary_average.sort_values('平均薪资（千/月）', ascending=False)[:15]
    factors = salary_average['公司定位'].values.tolist()
    x = salary_average['平均薪资（千/月）'].values.tolist()

    fig = figure(
        title="所属公司定位平均薪资(千/月)",
        #     toolbar_location=None,
        tools="hover",
        y_range=factors,
        x_range=[0, 35],
        tooltips=[('平均薪资中位数', '￥@x' + "（千/月）")],
        plot_width=700,
        plot_height=500)

    fig.segment(0, factors, x, factors, line_width=3, line_color="#B9A7FF")
    fig.circle(x, factors, size=18, fill_color="#FAF675", line_color="#B9A7FF", line_width=4)
    fig.xgrid.grid_line_color = None
    fig.ygrid.grid_line_color = None
    return fig

def cp_fl():

    cp_data['岗位福利'] = cp_data['岗位福利'].astype('str')
    fuli_sum = cp_data['岗位福利'].sum()
    def wordcount():
        readlist = fuli_sum.split(",")
        dict1 = {}
        for every_world in readlist:
            if every_world in dict1:
                dict1[every_world] += 1
            else:
                dict1[every_world] = 1
        return dict1

    fuli_cipin = wordcount()
    fuli_cipin1 = {k: v for k, v in fuli_cipin.items() if v > int(10)}
    fuli_cppx = sorted(fuli_cipin1.items(), key=lambda x: x[1], reverse=True)

    c2 = (
        WordCloud()
            .add(series_name="", data_pair=fuli_cppx, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(c2, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_c2 = "".join(f.readlines())
        return js_c2

def cp_gz():
    cp=[('经验', 1.0),
 ('工作', 0.9865414429636898),
 ('负责', 0.9184360682221432),
 ('产品', 0.8841658581303065),
 ('能力', 0.7602267784040088),
 ('需求', 0.7352860179047133),
 ('优先', 0.701121440127366),
 ('设计', 0.6934525951534525),
 ('沟通', 0.6569107399043199),
 ('分析', 0.6526494837331076),
 ('用户', 0.5579175417479082),
 ('团队', 0.5389191973803109),
 ('项目', 0.5359413406520456),
 ('业务', 0.5340912042910873),
 ('要求', 0.5252370488930735),
 ('数据', 0.4926535572738315),
 ('熟悉', 0.4662241931457012),
 ('优化', 0.44093601229569956),
 ('规划', 0.42665875762110816),
 ('行业', 0.4065957754707774),
 ('运营', 0.4026526791551803),
 ('开发', 0.3735854432330961),
 ('协调', 0.35763578568024423),
 ('系统', 0.3537257398329053),
 ('管理', 0.34275858539663134),
 ('功能', 0.33799332720927666),
 ('体验', 0.3222270700581005),
 ('落地', 0.3181361803530848),
 ('专业', 0.3173298260265034),
 ('流程', 0.3046083141348322),
 ('学习', 0.30222875204208616),
 ('平台', 0.3005769319736722),
 ('技术', 0.2994775392574831),
 ('产品设计', 0.2984425907134953),
 ('调研', 0.29357528691798657),
 ('方案', 0.2895345057347239),
 ('问题', 0.2885359103138055),
 ('提升', 0.2781258922601441),
 ('迭代', 0.2665715582362437),
 ('独立', 0.2578198420394902),
 ('互联网', 0.24934450642485215),
 ('合作', 0.24842009381632307),
 ('市场', 0.24511319039858004),
 ('跟进', 0.2442668742019767),
 ('上线', 0.24008605541995146),
 ('客户', 0.2382665883038846),
 ('工具', 0.23696078180740587),
 ('测试', 0.23433193983313672),
 ('制定', 0.23312093583619592),
 ('理解', 0.22937095641780522),
 ('推进', 0.22613053475114694),
 ('原型', 0.22417303411447542),
 ('逻辑', 0.22155788564514844),
 ('协作', 0.21822238289901016),
 ('场景', 0.21750178294952754),
 ('竞品', 0.21175646187728644),
 ('目标', 0.21142335156075687),
 ('协助', 0.20972909368780795),
 ('提供', 0.2094469767206228),
 ('挖掘', 0.20773024623588854),
 ('反馈', 0.2044219856797962),
 ('职位', 0.20381956939744203),
 ('撰写', 0.2018353774349711),
 ('深入', 0.1987804052172272),
 ('责任心', 0.1949538561398831),
 ('发展', 0.19419660285657386),
 ('部门', 0.19334708287349794),
 ('策略', 0.19288767708448432),
 ('方向', 0.1915290086167885),
 ('策划', 0.1875367082797239),
 ('游戏', 0.185322276717062),
 ('收集', 0.185196413183847),
 ('经理', 0.1811198607533197),
 ('核心', 0.17863093825693424),
 ('解决方案', 0.17821418126828864),
 ('输出', 0.1775968348236291),
 ('研究', 0.1718125532657177),
 ('思维', 0.1673913240362941),
 ('编写', 0.16728808810436738),
 ('精神', 0.16585935561828485),
 ('跟踪', 0.1648915701591097),
 ('服务', 0.16259165014524551),
 ('创新', 0.16254726054046612),
 ('内容', 0.16090271651784863),
 ('应用', 0.16011110595149017),
 ('意识', 0.15865455304452464),
 ('资源', 0.15850805838099777),
 ('关注', 0.15407126464296506),
 ('执行', 0.151898880688068),
 ('建设', 0.1467465836840702),
 ('交互', 0.14624513952617302),
 ('软件', 0.14387389864932293),
 ('实施', 0.14347279082982609),
 ('配合', 0.14146546859516454),
 ('体系', 0.1394356358903021),
 ('过程', 0.1391429580529659),
 ('领域', 0.13905780266227413),
 ('质量', 0.1379099298306802),
 ('确保', 0.13546392680207336),
 ('改进', 0.13401541270461473)]
    c3 = (
        WordCloud()
            .add(series_name="", data_pair=cp, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(c3, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_c3 = "".join(f.readlines())
        return js_c3


# ---------------------------------------------设计方向-----------------------------------------------------------
sj_data=data[data["类别"]=="设计"]
def sj_shu():
    jishu_data = [
        {"name": "设计",
         "children": [
             {"name": "UI设计"}, {"name": "平面设计"}, {"name": "网页设计"},
             {"name": "交互设计"}, {"name": "视觉分析师"},
             {"name": "游戏界面设计"}, {"name": "原画师"}
         ]}
    ]
    # ,theme=ThemeType.VINTAGE
    hangyefenlei = (
        Tree(init_opts=opts.InitOpts(width="450px", height="500px", bg_color="rgba(156,168,184,0)"))
            .add("", data=jishu_data, symbol="rect", symbol_size=12,
                 is_roam=True, initial_tree_depth=1,
                 label_opts=opts.LabelOpts(color='#4A4453', position='top', font_family='Arial'))
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='500px', height='400px'))
            .add(hangyefenlei, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_shuzhuan = "".join(f.readlines())
        return js_shuzhuan
def sj_shengmap():
    # 取出省份和省份数量做成字典
    jssheng_list = list(sj_data['省份'])
    jssheng_dict = dict([[i, jssheng_list.count(i)] for i in jssheng_list])
    # 移除non值
    del jssheng_dict['无']
    # 职位省份分布
    provice = list(jssheng_dict.keys())
    provice_values = list(jssheng_dict.values())
    pieces = [{"min": 900, "max": 1200},
              {"min": 100, "max": 900},
              {"min": 0, "max": 100},
              ]
    # 画图
    sheng_map = (
        Map(init_opts=opts.InitOpts(
            width="700px", height="500px", bg_color="rgba(156,168,184,0)", ))
            .add("", data_pair=[list(z) for z in zip(provice, provice_values)],
                 maptype="china",
                 symbol="roundRect", is_selected=True, is_map_symbol_show=False)
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                pos_left='5%',
                pos_top='60%',
                is_piecewise=True,
                is_calculable=False,
                pieces=pieces,
                range_color=["#B0A7FF", "#FEFFA7", "#D68787"],
            )))
    grid = (
        Grid(init_opts=opts.InitOpts(width='690px', height='650px'))
            .add(sheng_map, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_sheng = "".join(f.readlines())
        return js_sheng
def sj_city_sl():
    jscity_list = list(sj_data['城市'])
    jscity_dict = dict([[i, jscity_list.count(i)] for i in jscity_list])
    # 移除non值
    del jscity_dict['无']
    # 职位城市分布
    cities = list(jscity_dict.keys())
    cities_values = list(jscity_dict.values())
    pieces = [{"min": 500, "max": 1200},
              {"min": 50, "max": 400},
              {"min": 0, "max": 50}
              ]
    city_sum = (
        Geo(init_opts=opts.InitOpts(width="500px", height="550px"))
            .add_schema(maptype="china",
                        itemstyle_opts=opts.ItemStyleOpts())
            .add(
            "",
            data_pair=[list(z) for z in zip(cities, cities_values)],
            type_=ChartType.EFFECT_SCATTER,
            symbol_size=7)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                pos_left='8%',
                pos_top='60%',
                is_piecewise=True,
                is_calculable=False,
                pieces=pieces,
                range_color=["#B0A7FF", "#FEFFA7", "#D68787"],
                range_size="7px",
            ),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='690px', height='650px'))
            .add(city_sum, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_csl = "".join(f.readlines())
        return js_csl
def sj_zhucitu():
    # 取出城市数量做成字典
    jscity_list1 = list(sj_data['城市'])
    jscity_dict1 = dict([[i, jscity_list1.count(i)] for i in jscity_list1])
    # 移除non值
    del jscity_dict1['无']
    jscity_dict1 = dict(sorted(jscity_dict1.items(), key=operator.itemgetter(1), reverse=True))
    # 职位城市分布
    cities1 = list(jscity_dict1.keys())[0:10]
    cities_values1 = list(jscity_dict1.values())[0:10]
    js_sum = (
        Bar(init_opts=opts.InitOpts(width='500px', height='500px'))
            .add_xaxis(cities1)
            .add_yaxis('', cities_values1, color="#9358B8")
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)
                                     ),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#B0A7FF"]
            )
        )
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(js_sum, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_zsl = "".join(f.readlines())
        return js_zsl
def sjxinzi():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = sj_data.query("城市 == @city")
    shengfen_average = city_data.groupby('城市')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    shengfen_average['平均薪资（千/月）'] = shengfen_average['平均薪资（千/月）'].round(decimals=1)
    shengfen_average = shengfen_average.sort_values('平均薪资（千/月）', ascending=False)

    x_data = shengfen_average['城市'].values.tolist()
    y_data = shengfen_average['平均薪资（千/月）'].values.tolist()

    line = Line(init_opts=opts.InitOpts(width='750px', height='400px'))
    line.add_xaxis(x_data)
    line.add_yaxis('平均薪资（千/月）', y_data, color="#9358B8")
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='400px'))
            .add(line, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_line = "".join(f.readlines())
        return js_line
def sjzuigao():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = sj_data.query("城市 == @city")
    # 平均数
    xz_zg = city_data.groupby('城市')['最高薪资（千/月）'].mean().to_frame('最高薪资（千/月）').reset_index()
    xz_zg['最高薪资（千/月）'] = xz_zg['最高薪资（千/月）'].round(decimals=1)
    xz_zg = xz_zg.sort_values('最高薪资（千/月）', ascending=False)[:10]
    # 中位数
    xz_zw = city_data.groupby('城市')['最高薪资（千/月）'].median().to_frame('最高薪资（千/月）').reset_index()
    xz_zw['最高薪资（千/月）'] = xz_zw['最高薪资（千/月）'].round(decimals=1)
    xz_zw = xz_zw.sort_values('最高薪资（千/月）', ascending=False)[:10]
    x_data = xz_zw['城市'].values.tolist()
    pj_y_data = xz_zg['最高薪资（千/月）'].values.tolist()
    zw_y_data = xz_zw['最高薪资（千/月）'].values.tolist()
    # 准备x轴数据
    xin_zi = ['薪资平均', '薪资中位']
    x = [(lei, wages) for lei in x_data for wages in xin_zi]
    # 准备y轴数据
    y = sum(zip(pj_y_data, zw_y_data), ())
    # 准备ColumnDataSource
    source = ColumnDataSource(data=dict(x_axis=x, y_counts=y))
    # 准备tooltips 鼠标移入显示数据
    TOOLTIPS = [
        ("counts", "@y_counts" + "（千/月）"),
        ("描述", "@x_axis")]
    color = ["#FFA7A7", "#AAA3FF"]
    # 画布
    p = figure(
        x_range=FactorRange(*x),
        plot_height=350,
        title="主要城市最高薪资中位数和平均数差异",
        tooltips=TOOLTIPS
    )
    # 绘制图形 vbar 垂直柱状图
    p.vbar(
        x='x_axis',
        top="y_counts",
        width=0.8,
        source=source,
        fill_color=factor_cmap('x_axis',
                               palette=color,
                               factors=xin_zi,
                               start=1, end=2)
    )
    # factor_cmap 模块 每一类相同颜色，共2种颜色
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    # p.yaxis.axis_label = "薪资（千/月）"  # y轴名称
    p.axis.axis_label_text_font_style = 'bold'
    p.yaxis.major_label_text_font_size = '14px'
    return p
def sjzuidi():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = sj_data.query("城市 == @city")
    # 平均数
    xz_zd = city_data.groupby('城市')['最低薪资（千/月）'].mean().to_frame('最低薪资（千/月）').reset_index()
    xz_zd['最低薪资（千/月）'] = xz_zd['最低薪资（千/月）'].round(decimals=1)
    xz_zd = xz_zd.sort_values('最低薪资（千/月）', ascending=False)
    # 中位数
    xz_zw1 = city_data.groupby('城市')['最低薪资（千/月）'].median().to_frame('最低薪资（千/月）').reset_index()
    xz_zw1['最低薪资（千/月）'] = xz_zw1['最低薪资（千/月）'].round(decimals=1)
    xz_zw1 = xz_zw1.sort_values('最低薪资（千/月）', ascending=False)
    x_data1 = xz_zw1['城市'].values.tolist()
    pj_y_data1 = xz_zd['最低薪资（千/月）'].values.tolist()
    zw_y_data1 = xz_zw1['最低薪资（千/月）'].values.tolist()
    # 准备x轴数据
    xin_zi = ['薪资平均', '薪资中位']
    x = [(lei, wages) for lei in x_data1 for wages in xin_zi]
    # 准备y轴数据
    y = sum(zip(pj_y_data1, zw_y_data1), ())
    # 准备ColumnDataSource
    source = ColumnDataSource(data=dict(x_axis=x, y_counts=y))
    # 准备tooltips 鼠标移入显示数据
    TOOLTIPS = [
        ("counts", "@y_counts" + "（千/月）"),
        ("描述", "@x_axis")]
    color = ["#FBFD9F","#9FB1FD"]
    # 画布
    p = figure(
        x_range=FactorRange(*x),
        plot_height=350,
        title="主要城市最低薪资中位数和平均数差异",
        tooltips=TOOLTIPS
    )
    # 绘制图形 vbar 垂直柱状图
    p.vbar(
        x='x_axis',
        top="y_counts",
        width=0.8,
        source=source,
        fill_color=factor_cmap('x_axis',
                               palette=color,
                               factors=xin_zi,
                               start=1, end=2)
    )
    # factor_cmap 模块 每一类相同颜色，共2种颜色
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    # p.yaxis.axis_label = "薪资（千/月）"  # y轴名称
    p.axis.axis_label_text_font_style = 'bold'
    p.yaxis.major_label_text_font_size = '14px'
    return p
def sjnxxllx():
    # 获取不同工作年限的数量
    gznx_num = sj_data['工作年限'].value_counts()
    gznx = gznx_num.index.tolist()
    num = [i for i in gznx_num]
    data_pair1 = [list(z) for z in zip(gznx, num)]
    # 获取不同学历要求的数量
    xueli_num = sj_data['学历要求'].value_counts()
    xueli_e = xueli_num.index.tolist()
    num_e = [i for i in xueli_num]
    data_pair2 = [list(z) for z in zip(xueli_e, num_e)]
    # 获取不同工作类型的数量
    gzlx_num = sj_data['工作类型'].value_counts()
    leixing_l = gzlx_num.index.tolist()
    num_l = [i for i in gzlx_num]
    data_pair2 = [list(z) for z in zip(leixing_l, num_l)]
    # 开始画图
    gznx_bar = (
        Bar()
            .add_xaxis(gznx)
            .add_yaxis("", num, color='#B0A7FF')
            .set_global_opts(title_opts=opts.TitleOpts(title="不同工作年限数量", pos_left="30%",
                                                       ))
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="average", type_="average")]))
    )

    xueli_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair1, rosetype="area", center=['25%', "75%"], radius=["10%", '25%'])
            .set_colors(["#b5c4b1", "#8696a7", "#9ca8b8", "#ececea", "#7a7281", "#fffaf4", "#a27e7e", "#ead0d1"])
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同工作类型数量占比",
                                                       pos_left="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色
                                                      ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))
    leixing_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair2, center=['75%', "75%"], radius=["15%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同学历要求数量占比",
                                                       pos_right="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色

                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False),

                             )
    )

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(gznx_bar, grid_opts=opts.GridOpts(pos_right="35%", pos_bottom='60%'))
    grid.add(xueli_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='60%'))
    grid.add(leixing_pie, grid_opts=opts.GridOpts(pos_right="50%", pos_top="60%"))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        nxxz = "".join(f.readlines())
        return nxxz

def sj_ruzi():
    # 获取不同融资情况的数量
    rzqk_num = sj_data['融资情况'].value_counts()
    rzqk = rzqk_num.index.tolist()
    rz_num = [i for i in rzqk_num]
    data_pair3 = [list(z) for z in zip(rzqk, rz_num)]

    # 融资情况不同，薪资中位情况
    rz_average = sj_data.groupby('融资情况')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    rz_average['平均薪资（千/月）'] = rz_average['平均薪资（千/月）'].round(decimals=1)
    rz_average = rz_average.sort_values('平均薪资（千/月）', ascending=False)
    x_data = rz_average['融资情况'].values.tolist()
    y_data = rz_average['平均薪资（千/月）'].values.tolist()
    rz_pie = (
        Pie()
            .add("岗位数量占比", data_pair=data_pair3, rosetype="area", center=['65%', "50%"], radius=["10%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同融资情况数量占比",
                                                       pos_left="60%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="80%",
                                                       # 设置标题颜色
                                                      ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))

    rz_sum = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(x_data)
            .add_yaxis('', y_data, color="#BDA8FF")
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不同融资情况薪资差异", pos_left="10%", pos_top="13%",
                                      ),
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#BDA8FF"]))
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(rz_sum, grid_opts=opts.GridOpts(pos_right="60%", pos_top="20%"))
    grid.add(rz_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='20%'))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        jsrz = "".join(f.readlines())
        return jsrz

def sj_gm():
    # 获取不同公司规模的数量
    gsgm_num =sj_data['公司规模'].value_counts()
    gsgm = gsgm_num.index.tolist()
    gsgm_num = [i for i in gsgm_num]
    data_pair4 = [list(z) for z in zip(gsgm, gsgm_num)]

    # 公司规模不同，薪资中位情况
    gsgm_average = sj_data.groupby('公司规模')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    gsgm_average['平均薪资（千/月）'] = gsgm_average['平均薪资（千/月）'].round(decimals=1)
    gsgm_average = gsgm_average.sort_values('平均薪资（千/月）', ascending=False)
    x_data = gsgm_average['公司规模'].values.tolist()
    y_data = gsgm_average['平均薪资（千/月）'].values.tolist()
    rz_pie = (
        Pie()
            .add("岗位数量占比", data_pair=data_pair4, rosetype="area", center=['65%', "50%"], radius=["10%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同公司规模数量占比",
                                                       pos_left="60%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="80%",
                                                       # 设置标题颜色
                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))

    rz_sum = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(x_data)
            .add_yaxis('', y_data, color="#F5F8B7")
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不同公司规模薪资差异（千/月）", pos_left="10%", pos_top="13%",
                                      ),
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#A7CBFF"]))
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(rz_sum, grid_opts=opts.GridOpts(pos_right="60%", pos_top="20%"))
    grid.add(rz_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='20%'))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        jsgm = "".join(f.readlines())
        return jsgm

def sj_dingwei():
    gsdw = list(sj_data['公司定位'].unique())
    gsdw_count = list(sj_data['公司定位'].value_counts())
    zong = [list(z) for z in zip(gsdw, gsdw_count)]
    c1 = (
        WordCloud()
            .add(series_name="", data_pair=zong, word_size_range=[4, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        #     .render("basic_wordcloud.html")
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='500px', height='400px'))
            .add(c1, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_dw = "".join(f.readlines())
        return js_dw

def sj_dwxz():
    dw = sj_data[~sj_data['公司定位'].isin(["无"])]
    dw = dw[~dw['公司定位'].isin(["不限"])]
    salary_average = dw.groupby('公司定位')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    salary_average['平均薪资（千/月）'] = salary_average['平均薪资（千/月）'].round(decimals=1)
    salary_average = salary_average.sort_values('平均薪资（千/月）', ascending=False)[:15]
    factors = salary_average['公司定位'].values.tolist()
    x = salary_average['平均薪资（千/月）'].values.tolist()

    fig = figure(
        title="所属公司定位平均薪资(千/月)",
        #     toolbar_location=None,
        tools="hover",
        y_range=factors,
        x_range=[0, 35],
        tooltips=[('平均薪资中位数', '￥@x' + "（千/月）")],
        plot_width=700,
        plot_height=500)

    fig.segment(0, factors, x, factors, line_width=3, line_color="#B9A7FF")
    fig.circle(x, factors, size=18, fill_color="#FAF675", line_color="#B9A7FF", line_width=4)
    fig.xgrid.grid_line_color = None
    fig.ygrid.grid_line_color = None
    return fig

def sj_fl():

    sj_data['岗位福利'] = sj_data['岗位福利'].astype('str')
    fuli_sum = sj_data['岗位福利'].sum()
    def wordcount():
        readlist = fuli_sum.split(",")
        dict1 = {}
        for every_world in readlist:
            if every_world in dict1:
                dict1[every_world] += 1
            else:
                dict1[every_world] = 1
        return dict1

    fuli_cipin = wordcount()
    fuli_cipin1 = {k: v for k, v in fuli_cipin.items() if v > int(10)}
    fuli_cppx = sorted(fuli_cipin1.items(), key=lambda x: x[1], reverse=True)

    c2 = (
        WordCloud()
            .add(series_name="", data_pair=fuli_cppx, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(c2, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_c2 = "".join(f.readlines())
        return js_c2

def sj_gz():
    sj=[('工作', 1.0),
 ('经验', 0.8819478844696875),
 ('设计', 0.8469938098537412),
 ('负责', 0.837676522220606),
 ('能力', 0.7813557072916851),
 ('团队', 0.6114915655561438),
 ('沟通', 0.6049499932072138),
 ('产品', 0.591587334789786),
 ('优先', 0.5832912205281566),
 ('要求', 0.5792911060231719),
 ('项目', 0.5214058274453669),
 ('游戏', 0.5071891329864023),
 ('需求', 0.48334937279751605),
 ('专业', 0.4310139152093112),
 ('视觉', 0.3932789551048775),
 ('用户', 0.3832426572595731),
 ('优化', 0.3831410251039113),
 ('熟悉', 0.37877516852340704),
 ('分析', 0.36416254149019006),
 ('风格', 0.3545236750698295),
 ('美术', 0.3359161271908738),
 ('制作', 0.33583459005913363),
 ('体验', 0.32242255298957634),
 ('合作', 0.31022885047395843),
 ('行业', 0.2967190420999719),
 ('独立', 0.29600246675840197),
 ('理解', 0.28855482841569036),
 ('学习', 0.286815385094074),
 ('业务', 0.2860487591150086),
 ('提供', 0.2759650139174001),
 ('创意', 0.271729257848853),
 ('运营', 0.2627443791590061),
 ('流程', 0.2619183976043251),
 ('职位', 0.24796871507006926),
 ('数据', 0.24661094211226067),
 ('软件', 0.24649589969490887),
 ('开发', 0.24589948822100086),
 ('精神', 0.2321119429152345),
 ('协作', 0.23206863521293614),
 ('审美', 0.22890508872426676),
 ('方案', 0.22878681759813171),
 ('提升', 0.2275900298979938),
 ('作品', 0.22519689097191492),
 ('活动', 0.22518771814368369),
 ('交互', 0.22399316665014712),
 ('效果', 0.22263923420912493),
 ('制定', 0.22011793037681257),
 ('配合', 0.21858492481923683),
 ('落地', 0.2153986673319505),
 ('策划', 0.208009623629154),
 ('整体', 0.20756377861391448),
 ('研究', 0.20145816451145315),
 ('场景', 0.2009198824285773),
 ('输出', 0.1993563972864339),
 ('技术', 0.19418213847202095),
 ('互联网', 0.18496206077293978),
 ('问题', 0.1830456602640001),
 ('目标', 0.17995442227746072),
 ('平台', 0.17796084085031297),
 ('基础', 0.17680094295795365),
 ('责任心', 0.17193868126490772),
 ('管理', 0.17066886584657903),
 ('内容', 0.17061801721860798),
 ('关注', 0.16945641118868135),
 ('跟进', 0.16274671120422035),
 ('趋势', 0.1594351705308899),
 ('执行', 0.15763200730810395),
 ('方向', 0.1573849240294098),
 ('思维', 0.15656225194350107),
 ('规范', 0.1559454442864986),
 ('系统', 0.15530670096851965),
 ('意识', 0.15299097747069618),
 ('工具', 0.15198743313203586),
 ('界面', 0.15154287762143348),
 ('功底', 0.15022810010490945),
 ('手绘', 0.1497201754155671),
 ('协助', 0.1482942820556511),
 ('质量', 0.14745405663744832),
 ('创新', 0.1466075264081844),
 ('简历', 0.1450204371616326),
 ('市场', 0.14427021877943857),
 ('职责', 0.14349095543370327),
 ('资源', 0.14331660164420074),
 ('结合', 0.14165587840977698),
 ('细节', 0.1411603882827049),
 ('岗位', 0.1404116722643502),
 ('策略', 0.13931926793385474),
 ('品牌', 0.13921495539890807),
 ('保证', 0.13539569622412542),
 ('功能', 0.13313443246220755),
 ('角色', 0.13270259686026953),
 ('深入', 0.13199570530364008),
 ('协调', 0.13154191236826696),
 ('色彩', 0.13101327308927957),
 ('逻辑', 0.12823300820521202),
 ('动画', 0.12558114193965633),
 ('规划', 0.1255056489376615),
 ('方法', 0.12284269779847605),
 ('解决方案', 0.1197353265214424),
 ('表现', 0.1169417196225506)]
    c3 = (
        WordCloud()
            .add(series_name="", data_pair=cp, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(c3, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_c3 = "".join(f.readlines())
        return js_c3

# ---------------------------------------------运营方向-----------------------------------------------------------
yy_data=data[data["类别"]=="运营"]
def yy_shu():
    jishu_data = [
        {"name": "运营",
         "children": [
             {"name": "产品运营"}, {"name": "编辑"}, {"name": "用户运营"}, {"name": "文案策划"},
             {"name": "内容运营"}, {"name": "新媒体运营"},
             {"name": "数据运营"}
         ]},
    ]
    # ,theme=ThemeType.VINTAGE
    hangyefenlei = (
        Tree(init_opts=opts.InitOpts(width="450px", height="500px", bg_color="rgba(156,168,184,0)"))
            .add("", data=jishu_data, symbol="rect", symbol_size=12,
                 is_roam=True, initial_tree_depth=1,
                 label_opts=opts.LabelOpts(color='#4A4453', position='top', font_family='Arial'))
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='500px', height='400px'))
            .add(hangyefenlei, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_shuzhuan = "".join(f.readlines())
        return js_shuzhuan
def yy_shengmap():
    # 取出省份和省份数量做成字典
    jssheng_list = list(yy_data['省份'])
    jssheng_dict = dict([[i, jssheng_list.count(i)] for i in jssheng_list])
    # 移除non值
    del jssheng_dict['无']
    # 职位省份分布
    provice = list(jssheng_dict.keys())
    provice_values = list(jssheng_dict.values())
    pieces = [{"min": 900, "max": 1600},
              {"min": 100, "max": 900},
              {"min": 0, "max": 100},
              ]
    # 画图
    sheng_map = (
        Map(init_opts=opts.InitOpts(
            width="700px", height="500px", bg_color="rgba(156,168,184,0)", ))
            .add("", data_pair=[list(z) for z in zip(provice, provice_values)],
                 maptype="china",
                 symbol="roundRect", is_selected=True, is_map_symbol_show=False)
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                pos_left='5%',
                pos_top='60%',
                is_piecewise=True,
                is_calculable=False,
                pieces=pieces,
                range_color=["#B0A7FF", "#FEFFA7", "#D68787"],
            )))
    grid = (
        Grid(init_opts=opts.InitOpts(width='690px', height='650px'))
            .add(sheng_map, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_sheng = "".join(f.readlines())
        return js_sheng
def yy_city_sl():
    jscity_list = list(yy_data['城市'])
    jscity_dict = dict([[i, jscity_list.count(i)] for i in jscity_list])
    # 移除non值
    del jscity_dict['无']
    # 职位城市分布
    cities = list(jscity_dict.keys())
    cities_values = list(jscity_dict.values())
    pieces = [{"min": 500, "max": 1200},
              {"min": 50, "max": 400},
              {"min": 0, "max": 50}
              ]
    city_sum = (
        Geo(init_opts=opts.InitOpts(width="500px", height="550px"))
            .add_schema(maptype="china",
                        itemstyle_opts=opts.ItemStyleOpts())
            .add(
            "",
            data_pair=[list(z) for z in zip(cities, cities_values)],
            type_=ChartType.EFFECT_SCATTER,
            symbol_size=7)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(
                is_show=True,
                pos_left='8%',
                pos_top='60%',
                is_piecewise=True,
                is_calculable=False,
                pieces=pieces,
                range_color=["#B0A7FF", "#FEFFA7", "#D68787"],
                range_size="7px",
            ),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='690px', height='650px'))
            .add(city_sum, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_csl = "".join(f.readlines())
        return js_csl
def yy_zhucitu():
    # 取出城市数量做成字典
    jscity_list1 = list(yy_data['城市'])
    jscity_dict1 = dict([[i, jscity_list1.count(i)] for i in jscity_list1])
    # 移除non值
    del jscity_dict1['无']
    jscity_dict1 = dict(sorted(jscity_dict1.items(), key=operator.itemgetter(1), reverse=True))
    # 职位城市分布
    cities1 = list(jscity_dict1.keys())[0:10]
    cities_values1 = list(jscity_dict1.values())[0:10]
    js_sum = (
        Bar(init_opts=opts.InitOpts(width='500px', height='500px'))
            .add_xaxis(cities1)
            .add_yaxis('', cities_values1, color="#9358B8")
            .reversal_axis()
            .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)
                                     ),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#B0A7FF"]
            )
        )
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(js_sum, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_zsl = "".join(f.readlines())
        return js_zsl
def yyxinzi():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = yy_data.query("城市 == @city")
    shengfen_average = city_data.groupby('城市')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    shengfen_average['平均薪资（千/月）'] = shengfen_average['平均薪资（千/月）'].round(decimals=1)
    shengfen_average = shengfen_average.sort_values('平均薪资（千/月）', ascending=False)

    x_data = shengfen_average['城市'].values.tolist()
    y_data = shengfen_average['平均薪资（千/月）'].values.tolist()

    line = Line(init_opts=opts.InitOpts(width='750px', height='400px'))
    line.add_xaxis(x_data)
    line.add_yaxis('平均薪资（千/月）', y_data, color="#9358B8")
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='400px'))
            .add(line, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_line = "".join(f.readlines())
        return js_line
def yyzuigao():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = yy_data.query("城市 == @city")
    # 平均数
    xz_zg = city_data.groupby('城市')['最高薪资（千/月）'].mean().to_frame('最高薪资（千/月）').reset_index()
    xz_zg['最高薪资（千/月）'] = xz_zg['最高薪资（千/月）'].round(decimals=1)
    xz_zg = xz_zg.sort_values('最高薪资（千/月）', ascending=False)[:10]
    # 中位数
    xz_zw = city_data.groupby('城市')['最高薪资（千/月）'].median().to_frame('最高薪资（千/月）').reset_index()
    xz_zw['最高薪资（千/月）'] = xz_zw['最高薪资（千/月）'].round(decimals=1)
    xz_zw = xz_zw.sort_values('最高薪资（千/月）', ascending=False)[:10]
    x_data = xz_zw['城市'].values.tolist()
    pj_y_data = xz_zg['最高薪资（千/月）'].values.tolist()
    zw_y_data = xz_zw['最高薪资（千/月）'].values.tolist()
    # 准备x轴数据
    xin_zi = ['薪资平均', '薪资中位']
    x = [(lei, wages) for lei in x_data for wages in xin_zi]
    # 准备y轴数据
    y = sum(zip(pj_y_data, zw_y_data), ())
    # 准备ColumnDataSource
    source = ColumnDataSource(data=dict(x_axis=x, y_counts=y))
    # 准备tooltips 鼠标移入显示数据
    TOOLTIPS = [
        ("counts", "@y_counts" + "（千/月）"),
        ("描述", "@x_axis")]
    color = ["#FFA7A7", "#AAA3FF"]
    # 画布
    p = figure(
        x_range=FactorRange(*x),
        plot_height=350,
        title="主要城市最高薪资中位数和平均数差异",
        tooltips=TOOLTIPS
    )
    # 绘制图形 vbar 垂直柱状图
    p.vbar(
        x='x_axis',
        top="y_counts",
        width=0.8,
        source=source,
        fill_color=factor_cmap('x_axis',
                               palette=color,
                               factors=xin_zi,
                               start=1, end=2)
    )
    # factor_cmap 模块 每一类相同颜色，共2种颜色
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    # p.yaxis.axis_label = "薪资（千/月）"  # y轴名称
    p.axis.axis_label_text_font_style = 'bold'
    p.yaxis.major_label_text_font_size = '14px'
    return p
def yyzuidi():
    city = ["北京", "上海", "广州", "深圳", "杭州", "成都", "武汉"]
    city_data = yy_data.query("城市 == @city")
    # 平均数
    xz_zd = city_data.groupby('城市')['最低薪资（千/月）'].mean().to_frame('最低薪资（千/月）').reset_index()
    xz_zd['最低薪资（千/月）'] = xz_zd['最低薪资（千/月）'].round(decimals=1)
    xz_zd = xz_zd.sort_values('最低薪资（千/月）', ascending=False)
    # 中位数
    xz_zw1 = city_data.groupby('城市')['最低薪资（千/月）'].median().to_frame('最低薪资（千/月）').reset_index()
    xz_zw1['最低薪资（千/月）'] = xz_zw1['最低薪资（千/月）'].round(decimals=1)
    xz_zw1 = xz_zw1.sort_values('最低薪资（千/月）', ascending=False)
    x_data1 = xz_zw1['城市'].values.tolist()
    pj_y_data1 = xz_zd['最低薪资（千/月）'].values.tolist()
    zw_y_data1 = xz_zw1['最低薪资（千/月）'].values.tolist()
    # 准备x轴数据
    xin_zi = ['薪资平均', '薪资中位']
    x = [(lei, wages) for lei in x_data1 for wages in xin_zi]
    # 准备y轴数据
    y = sum(zip(pj_y_data1, zw_y_data1), ())
    # 准备ColumnDataSource
    source = ColumnDataSource(data=dict(x_axis=x, y_counts=y))
    # 准备tooltips 鼠标移入显示数据
    TOOLTIPS = [
        ("counts", "@y_counts" + "（千/月）"),
        ("描述", "@x_axis")]
    color = ["#FBFD9F","#9FB1FD"]
    # 画布
    p = figure(
        x_range=FactorRange(*x),
        plot_height=350,
        title="主要城市最低薪资中位数和平均数差异",
        tooltips=TOOLTIPS
    )
    # 绘制图形 vbar 垂直柱状图
    p.vbar(
        x='x_axis',
        top="y_counts",
        width=0.8,
        source=source,
        fill_color=factor_cmap('x_axis',
                               palette=color,
                               factors=xin_zi,
                               start=1, end=2)
    )
    # factor_cmap 模块 每一类相同颜色，共2种颜色
    p.y_range.start = 0
    p.x_range.range_padding = 0.1
    p.xaxis.major_label_orientation = 1
    # p.yaxis.axis_label = "薪资（千/月）"  # y轴名称
    p.axis.axis_label_text_font_style = 'bold'
    p.yaxis.major_label_text_font_size = '14px'
    return p
def yynxxllx():
    # 获取不同工作年限的数量
    gznx_num = yy_data['工作年限'].value_counts()
    gznx = gznx_num.index.tolist()
    num = [i for i in gznx_num]
    data_pair1 = [list(z) for z in zip(gznx, num)]
    # 获取不同学历要求的数量
    xueli_num = yy_data['学历要求'].value_counts()
    xueli_e = xueli_num.index.tolist()
    num_e = [i for i in xueli_num]
    data_pair2 = [list(z) for z in zip(xueli_e, num_e)]
    # 获取不同工作类型的数量
    gzlx_num = yy_data['工作类型'].value_counts()
    leixing_l = gzlx_num.index.tolist()
    num_l = [i for i in gzlx_num]
    data_pair2 = [list(z) for z in zip(leixing_l, num_l)]
    # 开始画图
    gznx_bar = (
        Bar()
            .add_xaxis(gznx)
            .add_yaxis("", num, color='#B0A7FF')
            .set_global_opts(title_opts=opts.TitleOpts(title="不同工作年限数量", pos_left="30%",
                                                        ))
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(name="average", type_="average")]))
    )

    xueli_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair1, rosetype="area", center=['25%', "75%"], radius=["10%", '25%'])
            .set_colors(["#b5c4b1", "#8696a7", "#9ca8b8", "#ececea", "#7a7281", "#fffaf4", "#a27e7e", "#ead0d1"])
            .set_series_opts(
            # 是否显示标签
            label_opts=opts.LabelOpts(is_show=True),
            tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同工作类型数量占比",
                                                       pos_left="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色
                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))
    leixing_pie = (
        Pie()
            .add("岗位占比", data_pair=data_pair2, center=['75%', "75%"], radius=["15%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同学历要求数量占比",
                                                       pos_right="15%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="45%",
                                                       # 设置标题颜色

                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False),

                             )
    )

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(gznx_bar, grid_opts=opts.GridOpts(pos_right="35%", pos_bottom='60%'))
    grid.add(xueli_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='60%'))
    grid.add(leixing_pie, grid_opts=opts.GridOpts(pos_right="50%", pos_top="60%"))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        nxxz = "".join(f.readlines())
        return nxxz

def yy_ruzi():
    # 获取不同融资情况的数量
    rzqk_num = yy_data['融资情况'].value_counts()
    rzqk = rzqk_num.index.tolist()
    rz_num = [i for i in rzqk_num]
    data_pair3 = [list(z) for z in zip(rzqk, rz_num)]

    # 融资情况不同，薪资中位情况
    rz_average = yy_data.groupby('融资情况')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    rz_average['平均薪资（千/月）'] = rz_average['平均薪资（千/月）'].round(decimals=1)
    rz_average = rz_average.sort_values('平均薪资（千/月）', ascending=False)
    x_data = rz_average['融资情况'].values.tolist()
    y_data = rz_average['平均薪资（千/月）'].values.tolist()
    rz_pie = (
        Pie()
            .add("岗位数量占比", data_pair=data_pair3, rosetype="area", center=['65%', "50%"], radius=["10%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同融资情况数量占比",
                                                       pos_left="60%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="80%",
                                                       # 设置标题颜色
                                                      ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))

    rz_sum = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(x_data)
            .add_yaxis('', y_data, color="#BDA8FF")
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不同融资情况薪资差异（千/月）", pos_left="10%", pos_top="13%"),
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#BDA8FF"]))
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(rz_sum, grid_opts=opts.GridOpts(pos_right="60%", pos_top="20%"))
    grid.add(rz_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='20%'))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        jsrz = "".join(f.readlines())
        return jsrz

def yy_gm():
    # 获取不同公司规模的数量
    gsgm_num =yy_data['公司规模'].value_counts()
    gsgm = gsgm_num.index.tolist()
    gsgm_num = [i for i in gsgm_num]
    data_pair4 = [list(z) for z in zip(gsgm, gsgm_num)]

    # 公司规模不同，薪资中位情况
    gsgm_average = yy_data.groupby('公司规模')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    gsgm_average['平均薪资（千/月）'] = gsgm_average['平均薪资（千/月）'].round(decimals=1)
    gsgm_average = gsgm_average.sort_values('平均薪资（千/月）', ascending=False)
    x_data = gsgm_average['公司规模'].values.tolist()
    y_data = gsgm_average['平均薪资（千/月）'].values.tolist()
    rz_pie = (
        Pie()
            .add("岗位数量占比", data_pair=data_pair4, rosetype="area", center=['65%', "50%"], radius=["10%", '25%'])
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True),
                             tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"))
            .set_global_opts(title_opts=opts.TitleOpts(title="不同公司规模数量占比",
                                                       pos_left="60%",
                                                       # 组件距离容器上方的像素值
                                                       pos_bottom="80%",
                                                       # 设置标题颜色
                                                       ),
                             # 图例配置项，参数 是否显示图里组件
                             legend_opts=opts.LegendOpts(is_show=False)))

    rz_sum = (
        Bar(init_opts=opts.InitOpts())
            .add_xaxis(x_data)
            .add_yaxis('', y_data, color="#F5F8B7")
            .reversal_axis()
            .set_global_opts(
            title_opts=opts.TitleOpts(title="不同公司规模薪资差异（千/月）", pos_left="10%", pos_top="13%",
                                      ),
            xaxis_opts=opts.AxisOpts(is_show=True),
            yaxis_opts=opts.AxisOpts(is_show=True,
                                     axisline_opts=opts.AxisLineOpts(is_show=False),
                                     axistick_opts=opts.AxisTickOpts(is_show=False)),
            visualmap_opts=opts.VisualMapOpts(
                is_show=False,
                max_=2,
                range_color=["#A7CBFF"]))
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": "#B85858",
                }},
            label_opts=opts.LabelOpts(is_show=True, position="right")
        ))

    grid = Grid(init_opts=opts.InitOpts())
    grid.add(rz_sum, grid_opts=opts.GridOpts(pos_right="60%", pos_top="20%"))
    grid.add(rz_pie, grid_opts=opts.GridOpts(pos_left="60%", pos_top='20%'))  # 改center
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        jsgm = "".join(f.readlines())
        return jsgm

def yy_dingwei():
    gsdw = list(yy_data['公司定位'].unique())
    gsdw_count = list(yy_data['公司定位'].value_counts())
    zong = [list(z) for z in zip(gsdw, gsdw_count)]
    c1 = (
        WordCloud()
            .add(series_name="", data_pair=zong, word_size_range=[4, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        #     .render("basic_wordcloud.html")
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='500px', height='400px'))
            .add(c1, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_dw = "".join(f.readlines())
        return js_dw

def yy_dwxz():
    dw = yy_data[~yy_data['公司定位'].isin(["无"])]
    dw = dw[~dw['公司定位'].isin(["不限"])]
    salary_average = dw.groupby('公司定位')['平均薪资（千/月）'].median().to_frame('平均薪资（千/月）').reset_index()
    salary_average['平均薪资（千/月）'] = salary_average['平均薪资（千/月）'].round(decimals=1)
    salary_average = salary_average.sort_values('平均薪资（千/月）', ascending=False)[:15]
    factors = salary_average['公司定位'].values.tolist()
    x = salary_average['平均薪资（千/月）'].values.tolist()

    fig = figure(
        title="所属公司定位平均薪资(千/月)",
        #     toolbar_location=None,
        tools="hover",
        y_range=factors,
        x_range=[0, 40],
        tooltips=[('平均薪资中位数', '￥@x' + "（千/月）")],
        plot_width=700,
        plot_height=500)

    fig.segment(0, factors, x, factors, line_width=3, line_color="#B9A7FF")
    fig.circle(x, factors, size=18, fill_color="#FAF675", line_color="#B9A7FF", line_width=4)
    fig.xgrid.grid_line_color = None
    fig.ygrid.grid_line_color = None
    return fig

def yy_fl():

    yy_data['岗位福利'] = yy_data['岗位福利'].astype('str')
    fuli_sum =yy_data['岗位福利'].sum()
    def wordcount():
        readlist = fuli_sum.split(",")
        dict1 = {}
        for every_world in readlist:
            if every_world in dict1:
                dict1[every_world] += 1
            else:
                dict1[every_world] = 1
        return dict1

    fuli_cipin = wordcount()
    fuli_cipin1 = {k: v for k, v in fuli_cipin.items() if v > int(10)}
    fuli_cppx = sorted(fuli_cipin1.items(), key=lambda x: x[1], reverse=True)

    c2 = (
        WordCloud()
            .add(series_name="", data_pair=fuli_cppx, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(c2, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_c2 = "".join(f.readlines())
        return js_c2

def yy_gz():
    yy=[('工作', 1.0),
 ('经验', 0.9229680834079103),
 ('负责', 0.8840926509072183),
 ('运营', 0.7607759950350962),
 ('能力', 0.7595471301015462),
 ('优先', 0.713256817685494),
 ('产品', 0.5662178571972764),
 ('沟通', 0.5555457470353317),
 ('要求', 0.5458324436963141),
 ('用户', 0.5415847994816706),
 ('内容', 0.5305910575961162),
 ('团队', 0.5246734543168456),
 ('数据', 0.4621681221864703),
 ('分析', 0.45821810968077903),
 ('熟悉', 0.43972373731492587),
 ('行业', 0.4302783201190071),
 ('平台', 0.4295071063247053),
 ('需求', 0.42377370607742043),
 ('优化', 0.4137233575431205),
 ('策划', 0.4054403419807016),
 ('活动', 0.37883020561084846),
 ('策略', 0.37172449352264436),
 ('提升', 0.3631020127763003),
 ('业务', 0.35992761377839816),
 ('项目', 0.3585901297842335),
 ('制定', 0.3319193385719559),
 ('管理', 0.3272380859277059),
 ('专业', 0.3232668303569004),
 ('目标', 0.2927493709595519),
 ('合作', 0.28433821794548586),
 ('职位', 0.28026160029426284),
 ('媒体', 0.2730145010773525),
 ('落地', 0.2622377057020245),
 ('执行', 0.2595907481086684),
 ('方案', 0.25575859211758917),
 ('视频', 0.25265269074991975),
 ('学习', 0.2510515720141759),
 ('提供', 0.24767889300078091),
 ('撰写', 0.24599425640735847),
 ('文案', 0.2445754296523318),
 ('设计', 0.2434176620381343),
 ('独立', 0.24235844328486866),
 ('营销', 0.2324738627694721),
 ('资源', 0.22234087529212126),
 ('互联网', 0.22150325173094088),
 ('挖掘', 0.22136974656896002),
 ('市场', 0.22007072267520636),
 ('推广', 0.21532535010405288),
 ('协作', 0.20968759906605033),
 ('职责', 0.20871794738407878),
 ('问题', 0.20740444742489425),
 ('协助', 0.20523583703616718),
 ('维护', 0.20458899139417316),
 ('输出', 0.20077981129397454),
 ('规划', 0.19894874873605226),
 ('流程', 0.1983588502937899),
 ('协调', 0.19682746307986643),
 ('游戏', 0.19324986090119528),
 ('思维', 0.1911276361492817),
 ('责任心', 0.18218500134186286),
 ('文字', 0.1816276283474798),
 ('品牌', 0.1775663296937375),
 ('结合', 0.17751702463675276),
 ('热点', 0.17476403876181806),
 ('增长', 0.1746216256734714),
 ('创意', 0.17200087580572174),
 ('效果', 0.17199433182173343),
 ('搭建', 0.1689454855776984),
 ('方向', 0.16621055124249215),
 ('发展', 0.16230005657601693),
 ('制作', 0.16119649262400954),
 ('部门', 0.16112843757697112),
 ('客户', 0.15989214272183744),
 ('渠道', 0.15898181208394507),
 ('跟进', 0.1582015661743318),
 ('体验', 0.15775178245469854),
 ('编辑', 0.15500397968060375),
 ('关注', 0.15431284777270957),
 ('体系', 0.15331836903992493),
 ('逻辑', 0.15314432058106436),
 ('指标', 0.15274725848156198),
 ('精神', 0.15176441602781154),
 ('活跃', 0.15157533392384473),
 ('理解', 0.15106189509092147),
 ('意识', 0.15101338093537287),
 ('服务', 0.15056433372565114),
 ('转化', 0.14751363027145448),
 ('功底', 0.14740560533734245),
 ('推进', 0.1466683795786485),
 ('反馈', 0.14593166375404787),
 ('配合', 0.14313559625069802),
 ('整体', 0.14275101867852838),
 ('信息', 0.14144942035273267),
 ('收集', 0.14052826407367863),
 ('玩法', 0.13954597757180387),
 ('迭代', 0.13542263312170066),
 ('定期', 0.13460997670229896),
 ('岗位', 0.1332982445346663),
 ('传播', 0.13079640410501647),
 ('软件', 0.1304162414580835)]
    c3 = (
        WordCloud()
            .add(series_name="", data_pair=cp, word_size_range=[6, 66])
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title="", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
    )
    grid = (
        Grid(init_opts=opts.InitOpts(width='650px', height='450px'))
            .add(c3, grid_opts=opts.GridOpts(pos_right='5%', pos_left='5%'))
    )
    grid.render("example.html")
    with open("example.html", encoding="utf8", mode="r") as f:
        js_c3 = "".join(f.readlines())
        return js_c3









