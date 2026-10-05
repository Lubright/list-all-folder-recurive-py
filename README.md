# list-all-folder-recurive-py

在指定的輸入目錄底下,遞迴找出所有名稱為「目標資料夾名稱」的資料夾,並將這些資料夾的絕對路徑存成文字檔。

Repository: https://github.com/Lubright/list-all-folder-recurive-py

## 需求

- Python 3.6+
- 僅使用標準函式庫(`argparse`、`os`、`sys`),無需安裝額外套件

## 安裝

```bash
git clone https://github.com/Lubright/list-all-folder-recurive-py.git
cd list-all-folder-recurive-py
```

## 使用方式

```bash
python list_files.py -d <輸入目錄> -t <目標資料夾名稱> [-o <輸出檔路徑>]
```

### 參數

| 參數 | 全名 | 必填 | 預設值 | 說明 |
| --- | --- | --- | --- | --- |
| `-d` | `--directory` | 是 | — | 輸入目錄(在此目錄底下搜尋) |
| `-t` | `--target` | 是 | — | 目標資料夾名稱 |
| `-o` | `--output` | 否 | `./output/output.txt` | 輸出檔路徑,資料夾不存在時會自動建立 |

### 範例

假設目錄結構如下:

```text
my_folder/
├── abc/
│   └── logs/
│       └── 1.log
└── b/
    └── x/
        └── logs/
```

```bash
python list_files.py -d ./my_folder -t logs
python list_files.py -d ./my_folder -t logs -o ./result/folders.txt
```

輸出內容(僅含目標資料夾本身的路徑,不含其中的檔案):

```text
/path/to/my_folder/abc/logs
/path/to/my_folder/b/x/logs
```

## 輸出格式

每行一個目標資料夾的絕對路徑,依字母順序排序:

```text
/path/to/abc/target
/path/to/b/target
...
```

## 回傳碼

- `0`:成功(沒有找到任何目標資料夾時,輸出檔會是空的)
- `1`:`-d` 指定的路徑不是有效目錄

## 注意事項

- 目標資料夾名稱採完整字串比對(區分大小寫),可出現在輸入目錄底下任何深度。
- 輸入目錄本身不會被視為目標資料夾。
- 找到目標資料夾後不會再往其內部搜尋,因此巢狀的同名資料夾(例如 `node_modules/@babel/core/node_modules`)不會被列出,也能避免掃描龐大的內容。
- 只列出資料夾路徑,不列出其中的檔案。
