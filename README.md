# UTF-8 Converter
## python 实现批量讲文本文件转为UTF-8 编码

|         参数         | 说明                                              |
| :------------------: | ------------------------------------------------- |
|     -i / --input     | 输入文件或者文件目录                              |
| -o / --output_folder | 输出目录                                          |
|    -s / --suffix     | 需要转化的文件类型列表，如： .txt .json .c .py 等 |
|   -v /  --verbose    | 输出详细处理文件                                  |
|     -h / --help      | 参数说明                                          |

### Requirement:

- Python >= 3.6
- chardet 
- alive_progress



### 安装

```
pip install utf2conv
```

### 使用

```
python -m utf2conv -i 输入文件/文件夹 -o 输出文件夹 -t 匹配文件格式

python -m utf2conv \
	-i /root/code \
	-o /root/code_u8 \
	-t .txt .c .cpp .py .json 
```

### TODO

- [ ] 发布二进制可执行文件
- [ ] windows / unix  换行转换
- [ ] 中文简繁体转换
