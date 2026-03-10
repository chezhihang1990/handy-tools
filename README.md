# 🛠️ Handy Tools - 实用工具集合

<div align="center">

**一个强大、易用的Python工具库**

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/chezhihang1990/handy-tools?style=social)](https://github.com/chezhihang1990/handy-tools)

</div>

## ✨ 项目介绍

Handy Tools 是一个功能强大的Python工具集合，专门为日常办公和数据处理场景设计。它提供了Excel、PDF、文件处理等多种实用功能，帮助您提高工作效率，减少重复劳动。

## 🎯 核心功能

### 📊 Excel处理工具
- ✅ **批量合并** - 一键合并多个Excel/CSV文件
- ✅ **格式转换** - Excel与CSV互相转换
- ✅ **数据筛选** - 按条件快速筛选Excel数据

### 📄 PDF处理工具
- ✅ **PDF合并** - 将多个PDF文件合并为一个
- ✅ **图片提取** - 将PDF页面转换为高质量图片

### 📁 文件处理工具
- ✅ **批量重命名** - 按规则批量重命名文件
- ✅ **清理空文件夹** - 自动删除空目录
- ✅ **查找重复文件** - 快速发现重复文件

### 📈 数据处理工具
- ✅ **JSON转Excel** - JSON数据快速转换为Excel
- ✅ **CSV智能合并** - 按关键字段合并多个CSV文件

## 🚀 快速开始

### 安装依赖

```bash
pip install pandas openpyxl PyPDF2 pdf2image
```

### 基本使用

```python
from utils import ExcelTools, PDFTools, FileTools, DataTools

# 合并Excel文件
ExcelTools.merge_excel_files(['file1.xlsx', 'file2.xlsx'], 'merged.xlsx')

# 合并PDF文件
PDFTools.merge_pdf(['doc1.pdf', 'doc2.pdf'], 'merged.pdf')

# 批量重命名文件
FileTools.batch_rename('/path/to/folder', 'photo', 1)

# JSON转Excel
DataTools.json_to_excel('data.json', 'output.xlsx')
```

## 📖 详细文档

### Excel处理示例

```python
# 合并多个Excel文件
files = ['report_1.xlsx', 'report_2.xlsx', 'report_3.xlsx']
ExcelTools.merge_excel_files(files, 'all_reports.xlsx')

# 筛选数据
ExcelTools.filter_excel('data.xlsx', 'status', 'completed', 'done.xlsx')

# Excel转CSV
ExcelTools.excel_to_csv('data.xlsx', './output')
```

### PDF处理示例

```python
# 合并PDF
PDFTools.merge_pdf(['part1.pdf', 'part2.pdf', 'part3.pdf'], 'complete.pdf')

# PDF转图片
images = PDFTools.pdf_to_images('document.pdf', './images')
```

### 文件处理示例

```python
# 批量重命名
count = FileTools.batch_rename('/photos', 'vacation', 1)
print(f"已重命名 {count} 个文件")

# 查找重复文件
duplicates = FileTools.find_duplicates('/documents')
print(f"发现 {len(duplicates)} 个重复文件")
```

### 数据处理示例

```python
# JSON转Excel
DataTools.json_to_excel('api_response.json', 'data.xlsx')

# 按字段合并CSV
DataTools.csv_merge_with_key('./csv_files', 'user_id', 'merged_data.xlsx')
```

## 💡 使用场景

- 📊 **财务报表** - 批量合并月度/季度报表
- 📄 **文档管理** - 合并多页PDF文档
- 📁 **资料整理** - 批量重命名和组织文件
- 📈 **数据分析** - 快速处理和转换数据格式

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启Pull Request

## 📝 更新日志

### v1.0.0 (2026-03-10)
- ✨ 初始版本发布
- ✅ 添加Excel处理工具
- ✅ 添加PDF处理工具
- ✅ 添加文件处理工具
- ✅ 添加数据处理工具

## 💬 联系方式

如有问题或建议，欢迎通过以下方式联系：

- 提交 [Issue](https://github.com/chezhihang1990/handy-tools/issues)
- 发送邮件

---

<div align="center">

## ❤️ 感谢支持

如果您觉得这个项目对您有帮助，欢迎打赏支持，激励我继续开发更多实用功能！

</div>

## 💰 打赏方式

### 微信支付

<div align="center">
  <img src="https://raw.githubusercontent.com/chezhihang1990/handy-tools/main/wechat_qr.png" width="200" alt="微信收款码">
  <p>微信扫码打赏</p>
</div>

### 支付宝

**收款账号:** `chezhihang@126.com`

<div align="center">
  <p>支付宝转账打赏</p>
</div>

---

<div align="center">

**您的支持是我持续更新的动力！** 🙏

Made with ❤️ by [chezhihang1990](https://github.com/chezhihang1990)

</div>
