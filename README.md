# list-all-folder-recurive-py

遞迴列出使用者指定目錄下所有檔案的絕對路徑,並將結果存成文字檔。

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
python list_files.py -d <目錄路徑> [-o <輸出檔路徑>]
```

### 參數

| 參數 | 全名 | 必填 | 預設值 | 說明 |
| --- | --- | --- | --- | --- |
| `-d` | `--directory` | 是 | — | 要掃描的目錄路徑 |
| `-o` | `--output` | 否 | `./output/output.txt` | 輸出檔路徑,資料夾不存在時會自動建立 |

### 範例

```bash
python list_files.py -d ./my_folder
python list_files.py -d ./my_folder -o ./result/files.txt
```

## 輸出格式

每行一個檔案的絕對路徑,依字母順序排序:

```text
/path/to/file1
/path/to/file2
...
```

## 回傳碼

- `0`:成功
- `1`:`-d` 指定的路徑不是有效目錄

## 注意事項

- 會列出所有檔案,包含 `.git` 等隱藏資料夾內的檔案。
- 只列出檔案,不列出資料夾本身。
