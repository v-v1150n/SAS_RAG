# SAS_RAG

## 目錄結構
- `chemical_data/`: 儲存化學物清單相關數據。
- `config/`: 配置文件目錄。

## 文件說明

- `Chat_bots.py`: Chat bot 執行檔。
- `load_csv.py`: 處理化學物清單的來源 CSV 檔，將 CSV 檔轉換為 TXT 檔，另存到 `txt_file` 內。
- `retriever_chain.py`: 將 LLM 與向量資料庫串接，並加上 Nemo Guardrail 的保護。
- `splitters.py`: 用來確認轉換後的化學物清單需要切多大的文字塊。
- `vectorstore.py`: 將切割後的化學物清單存為向量資料庫。

## 使用說明

1. **執行 Chat Bot**
    ```bash
    python Chat_bots.py
    ```

2. **處理化學物清單 CSV**
    ```bash
    python load_csv.py
    ```

3. **建立檢索鏈**
    ```bash
    python retriever_chain.py
    ```

4. **確認文字塊大小**
    ```bash
    python splitters.py
    ```

5. **建立向量資料庫**
    ```bash
    python vectorstore.py
    ```