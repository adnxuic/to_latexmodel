import webview
import os
import json
from typing import Any, Dict

from generate_tex import generate_tex

class Api:
    def generate_latex(self, data: Dict[str, Any]) -> str:
        print("Received user input:", data)
        # 保存用户输入为JSON文件
        with open('user_input.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print("User input saved:", data)  # 调试输出
        
        # 生成LaTeX文件
        generate_tex()
        
        return "LaTeX file generated successfully!"

if __name__ == '__main__':
    api = Api()
    html_path = os.path.join(os.path.dirname(__file__), 'maingui.html')
    window = webview.create_window('LaTeX Template Editor', url=html_path, js_api=api)
    webview.start()
