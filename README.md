# 🗺️ Grid World Policy Evaluation

> 深度強化學習 HW1 — 國立中興大學

一個使用 Flask 建構的互動式網格世界（Grid World）應用程式，實作了**策略評估（Policy Evaluation）**和**價值迭代（Value Iteration）**演算法。

---

## 📋 作業內容

### HW1-1：網格地圖開發
- 開發 **n×n** 網格地圖（n = 5 ~ 9），使用 Flask 網頁應用程式
- 使用者可透過滑鼠點擊指定：
  - 🟢 **起點**（綠色）
  - 🔴 **終點**（紅色）
  - ⬛ **障礙物**（灰色，最多 n-2 個）

### HW1-2：策略顯示與價值評估
- 為每個格子隨機生成一個行動方向（↑↓←→）作為策略
- 使用**策略評估（Policy Evaluation）**迭代計算每個狀態的價值函數 V(s)

### HW1-3：價值迭代與最佳政策
- 實現**價值迭代（Value Iteration）**演算法
- 計算最佳價值函數 V*(s)
- 從 V* 推導出最佳政策 π*，以箭頭顯示

---

## 🛠️ 技術架構

| 項目 | 技術 |
|------|------|
| 後端 | Python / Flask |
| 前端 | HTML / CSS / JavaScript |
| 演算法 | Policy Evaluation, Value Iteration |

### 參數設定

| 參數 | 值 |
|------|------|
| Discount Factor (γ) | 0.9 |
| 收斂閾值 (θ) | 1e-6 |
| 到達終點 Reward | +1 |
| 其他 Reward | 0 |

---

## 📂 專案結構

```
.
├── app.py                  # Flask 後端主程式
├── requirements.txt        # Python 依賴套件
├── templates/
│   └── index.html          # 前端頁面
├── static/
│   └── style.css           # 樣式表
├── conversation_log.md     # 開發對話紀錄
└── README.md               # 本文件
```

---

## 🚀 快速開始

### 🌐 GitHub Pages 線上版 (推薦)

您可以直接造訪本專案的靜態網頁版（於瀏覽器端執行演算法，不需安裝任何環境）：
👉 **[線上展示連結 (Live Demo)](https://ososlplp.github.io/DRL-HW1/)**

---

### 💻 本地執行 (Flask 後端版)

如果您想在本地執行 Flask 應用程式：

#### 1. 安裝依賴

```bash
pip install -r requirements.txt
```

#### 2. 啟動伺服器

```bash
python app.py
```

#### 3. 開啟瀏覽器

前往 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📖 使用方式

1. **調整網格大小**：使用滑桿選擇 n（5 ~ 9）
2. **設定起點**：點擊任一格子（變為綠色）
3. **設定終點**：點擊另一格子（變為紅色）
4. **設定障礙物**：點擊其他格子（變為灰色，n-2 個）
5. **策略評估**：點擊「策略評估」按鈕 → 顯示隨機策略箭頭與 V(s)
6. **價值迭代**：點擊「價值迭代」按鈕 → 顯示最佳策略箭頭與 V*(s)
7. **重置**：點擊「重置」按鈕清除所有設定

---

## 🧮 演算法說明

### 策略評估（Policy Evaluation）

給定一個固定的隨機策略 π，迭代計算：

$$V(s) = R(s, \pi(s), s') + \gamma \cdot V(s')$$

直到收斂（Δ < θ）。

### 價值迭代（Value Iteration）

使用 Bellman Optimality Equation 迭代：

$$V(s) = \max_{a} \left[ R(s, a, s') + \gamma \cdot V(s') \right]$$

收斂後，最佳策略為：

$$\pi^*(s) = \arg\max_{a} \left[ R(s, a, s') + \gamma \cdot V(s') \right]$$

---

## 📝 開發紀錄

詳見 [conversation_log.md](conversation_log.md)，記錄了完整的開發對話過程。
