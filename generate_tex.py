import json
import re

def generate_tex():
    # 读取模板JSON
    with open('template.json', 'r', encoding='utf-8') as f:
        template = json.load(f)
    
    # 读取用户输入JSON
    with open('user_input.json', 'r', encoding='utf-8') as f:
        user_input = json.load(f)
    
    print("User input:", user_input)  # 调试输出
    
    # 生成LaTeX内容
    latex_content = []
    
    # 添加导言区
    latex_content.extend(template['preamble'])
    
    # 添加文档开始部分
    latex_content.extend(template['document_start'])
    
    # 格式化整个latex_content，替换所有双大括号包围的占位符
    for i, line in enumerate(latex_content):
        if '{{' in line and '}}' in line:
            print(f"Original line: {line}")  # 调试输出
            try:
                # 使用正则表达式替换占位符
                new_line = re.sub(r'\{\{(\w+)}}', lambda m: user_input.get(m.group(1), m.group(0)), line)
                latex_content[i] = new_line
                print(f"Formatted line: {new_line}")  # 调试输出
            except Exception as e:
                print(f"Error in line: {line}")
                print(f"Error: {e}")
    
    # 添加各个章节
    for section in template['sections']:
        latex_content.append(f"\\section*{{【{section['name']}】}}")
        print(f"Original content: {section['content']}")  # 调试输出
        try:
            # 使用正则表达式替换占位符
            content = re.sub(r'\{\{(\w+)}}', lambda m: user_input.get(m.group(1), m.group(0)), section['content'])
            latex_content.append(content)
            print(f"Formatted content: {content}")  # 调试输出
        except Exception as e:
            print(f"Error in section {section['name']}")
            print(f"Error: {e}")
        latex_content.append("")  # 添加空行
    
    # 添加文档结束部分
    latex_content.extend(template['document_end'])
    
    # 将LaTeX内容写入文件
    with open('output.tex', 'w', encoding='utf-8') as f:
        f.write('\n'.join(latex_content))
    
    print("LaTeX content generated successfully.")  # 调试输出
    
    # 打印生成的LaTeX内容（前几行和后几行）
    print("Generated LaTeX content (first 10 lines):")
    print('\n'.join(latex_content[:10]))
    print("...")
    print("Generated LaTeX content (last 10 lines):")
    print('\n'.join(latex_content[-10:]))
