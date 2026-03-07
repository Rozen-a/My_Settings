# -*- coding: utf-8 -*-
"""
中文编码修复工具
在文件开头导入此模块即可解决 Windows 系统中文乱码问题

使用方法：
    import fix_encoding  # 在文件开头导入即可
    或
    from fix_encoding import fix_stdout_encoding
    fix_stdout_encoding()
"""

import sys
import os


def fix_stdout_encoding():
    """
    修复 Windows 系统标准输出编码问题，解决中文乱码
    在程序开始时调用此函数即可
    """
    if sys.platform == 'win32':
        try:
            # 方法1：设置控制台代码页为 UTF-8
            os.system('chcp 65001 >nul 2>&1')
            
            # 方法2：重新包装标准输出流
            import io
            if hasattr(sys.stdout, 'buffer'):
                sys.stdout = io.TextIOWrapper(
                    sys.stdout.buffer, 
                    encoding='utf-8',
                    errors='replace',
                    line_buffering=True
                )
            if hasattr(sys.stderr, 'buffer'):
                sys.stderr = io.TextIOWrapper(
                    sys.stderr.buffer, 
                    encoding='utf-8',
                    errors='replace',
                    line_buffering=True
                )
        except Exception:
            # 如果设置失败，尝试设置环境变量
            try:
                os.environ['PYTHONIOENCODING'] = 'utf-8'
            except:
                pass


# 自动执行修复（当导入此模块时）
fix_stdout_encoding()


