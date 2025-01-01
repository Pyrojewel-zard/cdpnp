import shutil
import os

def copy_file_to_network(src, dst_folder):
    try:
        # 确保目标文件夹存在
        os.makedirs(dst_folder, exist_ok=True)
        # 提取文件名
        file_name = os.path.basename(src)
        # 拼接目标文件的完整路径
        dst = os.path.join(dst_folder, file_name)
        # 如果目标文件已存在，则先删除
        if os.path.exists(dst):
            os.remove(dst)
        # 复制文件
        shutil.copy2(src, dst)
        print(f'File copied from {src} to {dst} successfully.')
    except PermissionError as e:
        print(f'Permission error: {e}')
    except FileNotFoundError as e:
        print(f'File not found: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

# 本地文件路径
file_src_list = [
    'D:\\OneDrive_bupt\\OneDrive - bupt.edu.cn\\00研究生工作\\无源器件建模\\张昌锴-2024-8月-电感变压器建模研究.pptx',
    'D:\\OneDrive_bupt\\OneDrive - bupt.edu.cn\\00研究生工作\\点胶贴片机\\点胶贴片机2024八月.pptx'
]

# 网络位置路径（这些路径现在是文件夹）
file_dst_folders = [
    '\\\\10.112.84.146\\科研项目Projects\\RSMGroup\\建模组',
    '\\\\10.112.84.146\\科研项目Projects\\半自动点胶贴片机'
]

for file_src, dst_folder in zip(file_src_list, file_dst_folders):
    copy_file_to_network(file_src, dst_folder)
