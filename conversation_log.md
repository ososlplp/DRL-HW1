# 深度強化學習 - 對話紀錄

> 此紀錄用於記錄與 AI 助手的對話過程，方便日後上傳至 GitHub。

---

## 2026-03-11

### 對話 1 - 開始紀錄

**User:** 請把我們接下來的對話紀錄下來，我之後要丟到 GitHub 上面。

**Assistant:** 已建立 `conversation_log.md` 對話紀錄檔，後續對話都會持續更新到這個檔案中。

---

### 對話 2 - HW1-1 & HW1-2 作業需求

**User:** 作業內容如下：
- **HW1-1: 網格地圖開發** — 開發 nxn 網格地圖（n=5~9），使用 Flask 網頁應用，用戶可點擊設定起點（綠色）、終點（紅色）、n-2 個障礙物（灰色）。
- **HW1-2: 策略顯示與價值評估** — 顯示每格隨機生成的行動箭頭作為策略，使用策略評估推導出 V(s)。

**Assistant:** 擬定了實作計畫，建立以下檔案：
- `app.py` — Flask 後端，含策略評估演算法（γ=0.9, θ=1e-6）
- `templates/index.html` — 前端互動頁面（滑桿選 n、點擊設定起終點與障礙物、策略評估按鈕）
- `static/style.css` — 現代深色主題 UI（漸層背景、玻璃擬態網格、動畫效果）
- `requirements.txt` — Flask 依賴

---

### 對話 3 - 安裝 Python 與啟動

**User:** 幫我自動下載安裝 Python。

**Assistant:** 
1. 偵測到電腦未安裝獨立 Python（僅有 Windows Store 替代指標）
2. 自動下載 Python 3.12.9 安裝程式
3. 靜默安裝並加入 PATH
4. 安裝 Flask 套件
5. 成功啟動 Flask 伺服器於 `http://127.0.0.1:5000`

---

### 對話 4 - HW1-3 價值迭代

**User:** HW1-3 要求：
- 實現價值迭代算法計算最佳政策
- 推導每個格子的最佳行動，取代隨機行動
- 顯示最佳政策下的 V(s)
- 提供可視化功能

**Assistant:** 
1. 在 `app.py` 新增 `/value_iteration` POST API：
   - 使用價值迭代（取所有動作的 max Q 值）收斂後得到 V*(s)
   - 從 V* 推導最佳政策（argmax Q）
2. 在前端新增橘色「價值迭代」按鈕
3. 點擊後會呼叫後端 API，顯示最佳策略箭頭與 V(s) 值
4. API 測試結果：5×5 網格、3 個對角障礙物，僅需 9 次迭代即收斂

---

### 對話 5 - 建立 README 並上傳 GitHub

**User:** 幫我彙整功課寫成 README.md 並上傳到 GitHub。

**Assistant:** 
1. 建立 `README.md`，包含：作業說明、技術架構、專案結構、快速開始、使用方式、演算法說明
2. 偵測到電腦未安裝 Git，自動下載安裝 MinGit
3. 透過 GitHub API 建立 `ososlplp/DRL-HW1` 公開 repo
4. 初始化 git、commit 7 個檔案、push 到 `main` 分支
5. GitHub repo：https://github.com/ososlplp/DRL-HW1

---

*（後續對話將持續追加在此檔案中）*
