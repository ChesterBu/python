li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
dic = {'k1': [], 'k2': []}

if __name__ == '__main__':

    for i in li:
        if i > 60:
            dic['k1'].append(i)
        else:
            dic['k2'].append(i)
    # print(dic)

    menu = {
        '北京': {
            '海淀': {
                '五道口': {
                    'soho': {},
                    '网易': {},
                    'google': {}
                },
                '中关村': {
                    '爱奇艺': {},
                    '汽车之家': {},
                    'youku': {},
                },
                '上地': {
                    '百度': {},
                },
            },
            '昌平': {
                '沙河': {
                    '老男孩': {},
                    '北航': {},
                },
                '天通苑': {},
                '回龙观': {},
            },
            '朝阳': {},
            '东城': {},
        },
        '上海': {
            '闵行': {
                "人民广场": {
                    '炸鸡店': {}
                }
            },
            '闸北': {
                '火车战': {
                    '携程': {}
                }
            },
            '浦东': {},
        },
        '山东': {},
    }
    layers = [menu, ]

    while True:
        current_layers = layers[-1]
        for key in current_layers:
            print(key)
        choice = input('>>').strip()
        if choice == 'b':
            layers.pop(-1)
            continue
        if choice == 'q':
            break
        if choice not in current_layers:
            continue
        layers.append(current_layers[choice])
