# Tangalar laboratoriyasi

1, 2 va 5 so'mlik tangalar (cheksiz miqdorda) bilan 100 so'mni necha xil usulda yig'ish mumkin?
Bu LeetCode 518 (Coin Change II) masalasi. Tartib ahamiyatsiz: 5 + 2 + 1 va 1 + 2 + 5 bitta usul.

**Jonli sahifa:** https://sharopovamaftuna318-star.github.io/tangalar-muammosi/

## Javob: 541 xil usul

Javob uch mustaqil usul bilan topiladi va hammasida bir xil chiqadi.

### 1. Hosil qiluvchi funksiya

- 1 so'mlik: (1 + x + x² + x³ + …) = 1 / (1 − x)
- 2 so'mlik: (1 + x² + x⁴ + x⁶ + …) = 1 / (1 − x²)
- 5 so'mlik: (1 + x⁵ + x¹⁰ + x¹⁵ + …) = 1 / (1 − x⁵)

G(x) = 1 / ((1 − x)(1 − x²)(1 − x⁵)) yoyilmasida x¹⁰⁰ ning koeffitsienti **541** ga teng.

### 2. Dinamik dasturlash

```python
def change(n, coins):
    dp = [1] + [0] * n
    for c in coins:
        for s in range(c, n + 1):
            dp[s] += dp[s - c]
    return dp[n]

change(100, [1, 2, 5])  # 541
```

Bosqichlar: {1} → 1, {1, 2} → 51, {1, 2, 5} → 541.

### 3. Yopiq formula

k ta beshlik olinsa, qolgan 100 − 5k so'm 1 va 2 so'mliklar bilan ⌊(100 − 5k)/2⌋ + 1 xil usulda to'ldiriladi:

Σ (k = 0..20) = 51 + 48 + 46 + 43 + 41 + 38 + 36 + 33 + 31 + 28 + 26 + 23 + 21 + 18 + 16 + 13 + 11 + 8 + 6 + 3 + 1 = **541**

## Fayllar

| Fayl | Vazifasi |
|------|----------|
| `index.html` | Interaktiv veb-interfeys: grafiklar, formulalar, barcha 541 kombinatsiya ro'yxati |
| `main.py` | Terminal versiyasi (Python, faqat standart kutubxona) |

## Ishga tushirish

```
python main.py
```
