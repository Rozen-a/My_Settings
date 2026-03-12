# Cursor配置

## 1. Rules

1. 始终使用简体中文回答我，除非我主动要求使用其他语言
2. 请用简洁的风格回复，避免不必要的重复或赘述。
3. 使用matplotlib绘图时，只要图中使用了中文，就设置中文字体，若当前文件中已设置中文显示则不再重复设置
4. 使用matplotlib绘图时，使用英文，注意只是图中元素使用英文，代码中注释等不影响绘图的内容仍保持中文

## 2. 调整侧边栏

打开设置搜索 Orientation 修改为 vertical

![image-20260309175718118](https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260309175718264.png)

成功变成侧边栏

<img src="https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260309181802094.png" alt="image-20260309181801994" style="zoom:50%;" />

侧边栏位置调整：

<img src="https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260309181949508.png" alt="image-20260309181949353" style="zoom:67%;" />

## 3. Python 中文乱码

**方式1：**`setting.json`中添加配置

```javascript
// 配置python语言正常输出中文的环境
"code-runner.executorMap":{ 
    "python":"set PYTHONIOENCODING=utf8 && python"
}
```

**方式2：**导入 `fix_encoding` 模块

```python
import fix_encoding
```

模块完整代码：

```python
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
```

**方式3：**设置系统环境变量

**Windows 系统：**

1. **通过图形界面设置：**
    - 右键"此电脑" → 属性 → 高级系统设置
    - 环境变量 → 用户变量 → 新建
    - 添加以下变量：
        - 变量名：`PYTHONIOENCODING`
        - 变量值：`utf-8`
        - 变量名：`PYTHONUTF8`
        - 变量值：`1`

---

**验证是否生效**

运行以下测试代码：

```python
import fix_encoding  # 不使用导包方式解决则不要这一行
print("中文测试：你好，世界！")
print("特殊字符：©®™€£¥")
```

如果正常显示中文，说明配置成功。

## 4. 自动换行

#### 4.1 Notebook 输出设置

| 设置项                                    | 配置值              | 说明                     |
| ----------------------------------------- | ------------------- | ------------------------ |
| `Notebook › Output: Word Wrap`            | ✅ 勾选              | 输出内容自动换行         |
| `Notebook › Output: Scrollbar Visibility` | `auto` 或 `visible` | 控制滚动条显示           |
| `Notebook › Output: Line Limit`           | 设置数字（如 100）  | 限制输出行数，超出可滚动 |

<img src="https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260309181506871.png" alt="image-20260309181506560" style="zoom: 67%;" />

#### 4.2 代码编辑器自动换行

| 设置项                       | 配置值                | 说明             |
| ---------------------------- | --------------------- | ---------------- |
| `Editor: Word Wrap`          | `on`                  | 开启自动换行     |
| `Editor: Word Wrap Column`   | 设置数字（如 80/120） | 指定换行列数     |
| `Editor: Word Wrap Minified` | ✅ 勾选                | 最小化文件也换行 |

<img src="https://gitee.com/rozen_gitee/typora-img/raw/master/img/20260309181717695.png" alt="image-20260309181717601" style="zoom: 67%;" />

