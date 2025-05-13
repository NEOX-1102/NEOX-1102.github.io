import csv, yaml

# 分类关键词
category_keywords = {
    'electronics': ['电', '手机', '电脑', '配件', '数码', '充电', '耳机', '电视', '音响'],
    'fashion': ['服', '衣', '裤', '裙', '鞋', '帽', '饰', '袜', '包', '围巾'],
    'home': ['家', '家具', '家纺', '床', '沙发', '桌', '椅', '装饰', '厨', '卫'],
    'beauty': ['美', '妆', '护肤', '洗发', '沐浴', '面膜', '香水', '剃须'],
    'baby': ['婴', '孕', '奶', '童', '宝宝', '儿童', '推车', '尿裤'],
    'sports': ['运动', '球', '跑步', '健身', '瑜伽', '户外', '登山', '自行车'],
    'auto': ['车', '汽车', '轮胎', '机油', '导航', '座垫', '车载'],
    'toys': ['玩具', '积木', '娃娃', '礼品', '模型', '拼图'],
    'office': ['办公', '文具', '笔', '纸', '打印', '文件', '桌面', '书架'],
    'food': ['食品', '饮料', '零食', '糖', '饼干', '茶', '酒', '果汁'],
    'lighting': ['灯', '照明', '台灯', '吊灯', '壁灯', 'LED'],
    'building': ['建材', '五金', '工具', '螺丝', '管', '砖', '门窗'],
    'health': ['健康', '医疗', '药', '血压', '按摩', '护理', '体温', '保健'],
    'packaging': ['包装', '盒', '袋', '印刷', '标签', '纸箱'],
    'machinery': ['机械', '设备', '泵', '阀', '机床', '压缩机', '发动机'],
}

cats = {k: [] for k in category_keywords}

with open('goods.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name = row['goodsName']
        img_url = row['goodsImg']
        item = {
            'id': row['goodsId'],
            'name': name,
            'img': img_url,
            'image': img_url,  # 直接用商品详情页链接
            'price': row['shopPrice'],
            'desc': row['goodsDesc'],
        }
        for cat, keywords in category_keywords.items():
            if any(kw in name for kw in keywords):
                cats[cat].append(item)
                break

with open('_data/products.yml', 'w', encoding='utf-8') as f:
    yaml.dump(cats, f, allow_unicode=True) 