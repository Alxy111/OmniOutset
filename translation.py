# 提取一个公共字典，方便多代号共用
dict_hans = {
    ("*", "At least one face must be selected!"): "必须选中至少一个面！",
    ("*", "Please select boundary edges first!"): "请先选中轮廓边！",
    ("*", "OmniOutset Tools"): "OmniOutset 工具",
    ("*", "Smart Face Extrude"): "智能面挤出 (Face)",
    ("*", "Equidistant Edge Extrude"): "等距边挤出 (Edge)",
    ("*", "Smart Face Extrude & Outset"): "智能面挤出与外扩",
    ("*", "Extrude Distance"): "法向挤出距离",
    ("*", "Outward Offset"): "外扩偏移距离",
    ("*", "Z Axis Offset"): "Z 轴平移",
}

dict_hant = {
    ("*", "At least one face must be selected!"): "必須選中至少一個面！",
    ("*", "Please select boundary edges first!"): "請先選中輪廓邊！",
    ("*", "OmniOutset Tools"): "OmniOutset 工具",
    ("*", "Smart Face Extrude"): "智能面擠出 (Face)",
    ("*", "Equidistant Edge Extrude"): "等距邊擠出 (Edge)",
    ("*", "Smart Face Extrude & Outset"): "智能面擠出與外擴",
    ("*", "Extrude Distance"): "法向擠出距離",
    ("*", "Outward Offset"): "外擴偏移距離",
    ("*", "Z Axis Offset"): "Z 軸平移",
}

translations_dict = {
    "zh_HANS": dict_hans, # 新版简体中文代号
    "zh_CN": dict_hans,   # 旧版/底层简体中文代号 (双保险)
    
    "zh_HANT": dict_hant, # 新版繁体中文代号
    "zh_TW": dict_hant,   # 旧版/底层繁体中文代号 (双保险)
    
    "ja_JP": {
        ("*", "At least one face must be selected!"): "少なくとも1つの面を選択する必要があります！",
        ("*", "Please select boundary edges first!"): "まず境界エッジを選択してください！",
        ("*", "OmniOutset Tools"): "OmniOutset ツール",
        ("*", "Smart Face Extrude"): "スマート面押し出し (Face)",
        ("*", "Equidistant Edge Extrude"): "等距離エッジ押し出し (Edge)",
        ("*", "Smart Face Extrude & Outset"): "スマート面押し出し＆アウトセット",
        ("*", "Extrude Distance"): "押し出し距離",
        ("*", "Outward Offset"): "外側へのオフセット距離",
        ("*", "Z Axis Offset"): "Z軸オフセット",
    },
    "ko_KR": {
        ("*", "At least one face must be selected!"): "하나 이상의 면을 선택해야 합니다!",
        ("*", "Please select boundary edges first!"): "먼저 경계 에지를 선택하십시오!",
        ("*", "OmniOutset Tools"): "OmniOutset 도구",
        ("*", "Smart Face Extrude"): "스마트 면 돌출 (Face)",
        ("*", "Equidistant Edge Extrude"): "등거리 에지 돌출 (Edge)",
        ("*", "Smart Face Extrude & Outset"): "스마트 면 돌출 및 아웃셋",
        ("*", "Extrude Distance"): "돌출 거리",
        ("*", "Outward Offset"): "바깥쪽 오프셋 거리",
        ("*", "Z Axis Offset"): "Z축 오프셋",
    }
}