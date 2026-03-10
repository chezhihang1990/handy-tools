# -*- coding: utf-8 -*-
"""
实用工具集合
包含Excel、PDF、文件处理等常用工具函数
"""

import os
import pandas as pd
from pathlib import Path
import json
import csv
from typing import List, Dict, Any, Optional
import datetime


class ExcelTools:
    """Excel处理工具类"""

    @staticmethod
    def merge_excel_files(files: List[str], output_file: str) -> bool:
        """
        合并多个Excel文件

        Args:
            files: Excel文件路径列表
            output_file: 输出文件路径

        Returns:
            是否成功
        """
        try:
            dfs = []
            for file in files:
                if file.endswith('.xlsx'):
                    df = pd.read_excel(file)
                    dfs.append(df)
                elif file.endswith('.csv'):
                    df = pd.read_csv(file, encoding='utf-8')
                    dfs.append(df)

            if dfs:
                result = pd.concat(dfs, ignore_index=True)
                result.to_excel(output_file, index=False)
                return True
            return False
        except Exception as e:
            print(f"合并失败: {e}")
            return False

    @staticmethod
    def excel_to_csv(excel_file: str, output_folder: str) -> bool:
        """将Excel转换为CSV"""
        try:
            df = pd.read_excel(excel_file)
            output_file = os.path.join(output_folder,
                                       Path(excel_file).stem + '.csv')
            df.to_csv(output_file, index=False, encoding='utf-8-sig')
            return True
        except Exception as e:
            print(f"转换失败: {e}")
            return False

    @staticmethod
    def filter_excel(excel_file: str, column: str, value: Any,
                     output_file: str) -> bool:
        """筛选Excel数据"""
        try:
            df = pd.read_excel(excel_file)
            filtered = df[df[column] == value]
            filtered.to_excel(output_file, index=False)
            return True
        except Exception as e:
            print(f"筛选失败: {e}")
            return False


class PDFTools:
    """PDF处理工具类"""

    @staticmethod
    def merge_pdf(files: List[str], output_file: str) -> bool:
        """
        合并PDF文件

        Args:
            files: PDF文件路径列表
            output_file: 输出文件路径

        Returns:
            是否成功
        """
        try:
            from PyPDF2 import PdfMerger
            merger = PdfMerger()
            for pdf in files:
                merger.append(pdf)
            merger.write(output_file)
            merger.close()
            return True
        except Exception as e:
            print(f"合并失败: {e}")
            return False

    @staticmethod
    def pdf_to_images(pdf_file: str, output_folder: str) -> List[str]:
        """将PDF转换为图片"""
        try:
            from pdf2image import convert_from_path
            images = convert_from_path(pdf_file)
            output_files = []
            for i, img in enumerate(images):
                output_file = os.path.join(
                    output_folder,
                    f"{Path(pdf_file).stem}_page_{i+1}.jpg"
                )
                img.save(output_file, 'JPEG')
                output_files.append(output_file)
            return output_files
        except Exception as e:
            print(f"转换失败: {e}")
            return []


class FileTools:
    """文件处理工具类"""

    @staticmethod
    def batch_rename(folder: str, prefix: str, start_num: int = 1) -> int:
        """批量重命名文件"""
        count = 0
        try:
            files = sorted(os.listdir(folder))
            for i, file in enumerate(files):
                ext = os.path.splitext(file)[1]
                new_name = f"{prefix}_{start_num + i:03d}{ext}"
                old_path = os.path.join(folder, file)
                new_path = os.path.join(folder, new_name)
                os.rename(old_path, new_path)
                count += 1
        except Exception as e:
            print(f"重命名失败: {e}")
        return count

    @staticmethod
    def clean_empty_folders(folder: str) -> int:
        """清理空文件夹"""
        count = 0
        try:
            for root, dirs, files in os.walk(folder, topdown=False):
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    if not os.listdir(dir_path):
                        os.rmdir(dir_path)
                        count += 1
        except Exception as e:
            print(f"清理失败: {e}")
        return count

    @staticmethod
    def find_duplicates(folder: str) -> List[str]:
        """查找重复文件"""
        duplicates = []
        try:
            file_hashes = {}
            for root, _, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    file_hash = FileTools._get_file_hash(file_path)
                    if file_hash in file_hashes:
                        duplicates.append(file_path)
                    else:
                        file_hashes[file_hash] = file_path
        except Exception as e:
            print(f"查找失败: {e}")
        return duplicates

    @staticmethod
    def _get_file_hash(file_path: str) -> str:
        """获取文件哈希值"""
        import hashlib
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()


class DataTools:
    """数据处理工具类"""

    @staticmethod
    def json_to_excel(json_file: str, output_file: str) -> bool:
        """JSON转Excel"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            df = pd.DataFrame(data)
            df.to_excel(output_file, index=False)
            return True
        except Exception as e:
            print(f"转换失败: {e}")
            return False

    @staticmethod
    def csv_merge_with_key(folder: str, key_column: str,
                            output_file: str) -> bool:
        """按关键字段合并CSV"""
        try:
            files = [f for f in os.listdir(folder) if f.endswith('.csv')]
            dfs = []
            for file in files:
                df = pd.read_csv(os.path.join(folder, file), encoding='utf-8')
                dfs.append(df)

            if dfs:
                result = pd.merge(dfs[0], dfs[1], on=key_column, how='outer')
                for df in dfs[2:]:
                    result = pd.merge(result, df, on=key_column, how='outer')
                result.to_excel(output_file, index=False)
                return True
            return False
        except Exception as e:
            print(f"合并失败: {e}")
            return False


def main():
    """示例用法"""
    print("实用工具集合")
    print("=" * 50)
    print("1. Excel处理工具")
    print("2. PDF处理工具")
    print("3. 文件处理工具")
    print("4. 数据处理工具")
    print("=" * 50)
    print("\n使用示例:")
    print("# 合并Excel文件")
    print("ExcelTools.merge_excel_files(['file1.xlsx', 'file2.xlsx'], 'merged.xlsx')")
    print("\n# 合并PDF文件")
    print("PDFTools.merge_pdf(['doc1.pdf', 'doc2.pdf'], 'merged.pdf')")
    print("\n# 批量重命名")
    print("FileTools.batch_rename('/path/to/folder', 'photo', 1)")
    print("\n# 查找重复文件")
    print("FileTools.find_duplicates('/path/to/folder')")


if __name__ == "__main__":
    main()
