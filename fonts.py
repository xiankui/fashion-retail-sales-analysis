from matplotlib.font_manager import fontManager

# 打印所有已注册字体
print([f.name for f in fontManager.ttflist if 'hei' in f.name.lower()])

# 查找包含中文的字体
chinese_fonts = [f.name for f in fontManager.ttflist if any('CJK' in lang for lang in f.get_languages())]
print(chinese_fonts)