def analyze_text(text):
    # 初始化字典用于统计字符频率
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    # 按频率降序排序
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    
    # 打印结果
    for char, freq in sorted_chars:
        print(f"字符 '{char}' 出现频率：{freq}")

# 测试程序
if __name__ == "__main__":
    input_text = input("请输入要分析的字符串：")
    analyze_text(input_text)
