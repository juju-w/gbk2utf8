# UTF-8 编码转换工具

|         参数         | 说明                                            |
| :------------------: | ----------------------------------------------- |
|     -i / --input     | 输入文件或者文件目录                            |
| -o / --output_folder | 输出目录                                        |
|    -s / --suffix     | 需要转化的文件后缀名，如： .txt .json .c .py 等 |
|   -v /  --verbose    | 输出详细处理文件                                |
|     -h / --help      | 参数说明                                        |

### Requirement:

- Python >= 3.6
- chardet 
- alive_progress
## 安装

```
pip install utf8conv
```

## 使用
### python 使用

```shell
# 帮助
python -m utf8conv -h

# 基本使用
python -m utf8conv -i 输入文件/目录 -o 输出目录 -t 格式列表

# 使用示例,转化code 目录下 .txt .json .c .cpp .py 为utf-8 格式
python -m utf8conv \
	-i /root/code \
	-o /root/code_u8 \
	-s .txt .json .c .cpp .py
	
	
# 转化文本文件
python -m utf8conv -i /root/code/abc.cpp -o ./
```
### 二进制可执行文件

## TODO List
- [ ] 编译可执行文件
- [ ] 换行CRLF(windows) --> LF(unix)
- [ ] GUI 界面版本
- [ ] 异常捕捉
- [ ] 简繁体切换
